from app import site
from flask_oauthlib.client import OAuth, OAuthException

oauth = OAuth(site)

google = oauth.remote_app(
    'google',
    consumer_key=site.config.get('GOOGLE_KEY'),
    consumer_secret=site.config.get('GOOGLE_SECRET'),
    request_token_params={'scope': 'email profile'},
    base_url='https://www.googleapis.com/oauth2/v3/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth'
)

github = oauth.remote_app(
    'github',
    consumer_key=site.config.get('GITHUB_KEY'),
    consumer_secret=site.config.get('GITHUB_SECRET'),
    request_token_params={'scope': 'user:email'},
    base_url='https://api.github.com/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
)

facebook = oauth.remote_app(
    'facebook',
    consumer_key=site.config.get('FACEBOOK_KEY'),
    consumer_secret=site.config.get('FACEBOOK_SECRET'),
    request_token_params={'scope': 'email'},
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_method='GET',
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
)
