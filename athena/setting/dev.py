from athena.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#4k3rs$@cv0i#8dr6oh1_1mf&p(-q((ql6&hd61_37#j_soc7#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = BASE_DIR /'static'
MEDIA_ROOT = BASE_DIR /'media'
STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

X_FRAME_OPTIONS='SAMEORIGIN'