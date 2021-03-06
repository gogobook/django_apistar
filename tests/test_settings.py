import os

DIRNAME = os.path.dirname(__file__)

SECRET_KEY = 'o=v^sgst0up0^znuce#97(6o5uwxi+nv!ur@b(6(js50808(%&'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django_apistar.authentication',
    'tests',
)

APISTAR_SETTINGS = {'DATABASES': DATABASES}
APISTAR_ROUTE_CONF = 'tests'
DEBUG = False
