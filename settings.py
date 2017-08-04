# -*- coding: utf-8 -*-
import os

APP_DIR = os.path.dirname(os.path.realpath(__file__))
DATABASE = 'sqlite:///{}'.format(os.path.join(APP_DIR, 'app.db'))
DEBUG = True
SECRET_KEY = 'development'

GOOGLE_KEY = ('562441629138-ss41vp0n0lhbb4vmfi8ggl4ngsma8o5u.apps.' +
              'googleusercontent.com')
GOOGLE_SECRET = 'bDUdnlF6158qf2Q8ZMH2E9mV'

GITHUB_KEY = '4f91894890edfb1a645e'
GITHUB_SECRET = '5fbcfd40d3e8f0bbc5582f45027bb50b9cbb9b09'

FACEBOOK_KEY = '509948979193573'
FACEBOOK_SECRET = '87b057823af02b6a7e0b459a6eeb69e5'
