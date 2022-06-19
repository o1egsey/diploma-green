import os
from pathlib import Path
import django_heroku
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-(i#8asp8(qzqr3!o=lj*0g-w@ms!ckd+v8rfud9%a0h)h33a1s'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_dump_load_utf8',

    'store',
    'basket',
    'account',
    'orders',
    'mptt',
    'checkout',




]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'treeShop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'store.context_processors.categories',
                'basket.context_processors.basket',
            ],
        },
    },
]

WSGI_APPLICATION = 'treeShop.wsgi.application'

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'greenspace',
        'USER': 'postgres',
        'PASSWORD': '1488',
        'HOST': 'localhost',
        'PORT': '5433',
    }

}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

django_heroku.settings(
    locals()
)

BASKET_SESSION_ID = "basket"

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#UserModel
AUTH_USER_MODEL = 'account.Customer'
LOGIN_REDIRECT_URL = '/account/dashboard'
LOGIN_URL = '/account/login/'

PASSWORD_RESET_TIMEOUT_DAYS = 2


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.ukr.net'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'greenspace1@ukr.net'
EMAIL_HOST_PASSWORD = 'EW8ODeBijt2NkCF5'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
