from app import *
from models import *
from auth import *
import feedparser


@site.before_request
def before_request():
    g.db = database
    g.db.connect()


@site.after_request
def after_request(response):
    g.db.close()
    return response


@site.route('/')
@login_required
def index():
    return render_template('index.html')


@site.route('/login', methods=['GET'])
def login():
    next_url = request.args.get('next')
    provider = request.args.get('provider', '')
    callback_url = url_for('oauth_authorized', provider=provider,
                           next=next_url or None, _external=True)
    if provider == 'google':
        return google.authorize(callback=callback_url)

    elif provider == 'github':
        return github.authorize(callback=callback_url)

    elif provider == 'facebook':
        return facebook.authorize(callback=callback_url)

    if current_user.is_authenticated:
        return redirect(next_url or url_for('index'))

    return render_template('login.html')


@site.route('/oauth_authorized/<provider>')
def oauth_authorized(provider):
    next_url = request.args.get('next') or url_for('index')

    if provider == 'github':
        resp = github.authorized_response()
    elif provider == 'google':
        resp = google.authorized_response()
    elif provider == 'facebook':
        resp = facebook.authorized_response()

    if resp is None:
        flash(u'Denied the request to sign in.')
        return redirect(url_for('login'))

    if resp is OAuthException:
        flash('Error with OAuth')
        redirect(url_for('login'))

    access_token = resp['access_token']

    session['oauth_token'] = (access_token, '')

    if provider == 'github':
        user_info = github.get('/user').data
        user_email = github.get('/user/emails').data[0]['email']
        user_id = user_info['id']
        user_name = user_info['login']

    elif provider == 'google':
        token_confirm = google.get('https://www.googleapis.com/oauth2/v3' +
                                   '/tokeninfo?access_token={0}'
                                   .format(access_token)).data
        user_email = token_confirm['email']
        user_id = token_confirm['sub']
        user_name = user_email.split('@')[0]

    elif provider == 'facebook':
        user_info = facebook.get('/me').data
        user_email = facebook.get('/me?fields=email').data['email']
        user_id = user_info['id']
        user_name = user_info['name']

    flash('You were signed in as %s' % user_name)
    user = User.select().where(User.social_id == user_id).first()
    if user is None:
        user = User.create(social_id=user_id,
                           nickname=user_name,
                           email=user_email)

    login_user(user)

    return redirect(next_url)


@github.tokengetter
@facebook.tokengetter
@google.tokengetter
def get_oauth_token():
    return session.get('oauth_token')


@site.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@login_manager.user_loader
def load_user(user_id):
    try:
        return User.get(User.id == user_id)
    except User.DoesNotExist:
        session.clear()
        return AnonymousUser()


@site.route('/newfeed/', methods=['GET', 'POST'])
@login_required
def new_feed():
    if request.method == 'POST':
        parser = feedparser.parse(request.form['feed_url'])
        if not parser.bozo:
            if any(parser.feed):
                cur_user = current_user._get_current_object()

                if 'title' in parser.feed:
                    title = parser.feed.title
                else:
                    title = "No title in feed"

                if 'description' in parser.feed:
                    description = parser.feed.description
                else:
                    description = "No feed description"

                url = request.form['feed_url']

                new_feed = Feed.create(user=cur_user, url=url, title=title,
                                       description=description)
            else:
                flash('Not a valid feed')

        else:
            flash('Not a valid feed')

    return render_template('newfeed.html')


@site.route('/deletefeed/')
def delete_feed():
    feed = request.args.get('feed')
    try:
        to_delete = Feed.get(Feed.id == feed)
        to_delete.delete_instance()
    except Feed.DoesNotExist:
        pass
    return redirect(url_for('index'))


@site.route('/rss/<feed>')
def rss(feed):
    try:
        show_feed = Feed.get(Feed.id == feed)
    except Feed.DoesNotExist:
        return redirect(url_for('index'))

    parser = feedparser.parse(show_feed.url)
    entries = parser.entries

    return render_template('rss.html', feed=show_feed, entries=entries)


if __name__ == '__main__':
    database.connect()
    database.create_tables([User, Feed], True)
    database.close()
    site.run()
