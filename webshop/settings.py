"""
Django settings for webshop project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import dj_database_url
from decouple import config
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!ha15@q#p11dbwkd$(rev&hutx2ohqrwfr0rc_d^sox@ub)ee7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['.vercel.app', '.now.sh','127.0.0.1']
#ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://onetechshop-opuzg67t3-fahimahamed101.vercel.app']
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'category',
    'accounts',
    'store',
    'carts',
       'orders',
       'django.contrib.sites',
        'allauth',
        'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
'allauth.socialaccount.providers.facebook',  
'cloudinary_storage',
   
    'cloudinary',
]
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'fahim1213456',
    'API_KEY': '554889398149233',
    'API_SECRET': 'xOh9Pctuw1UhBuRrj_XuP79ubbA'
}
SITE_ID = 5
ACCOUNT_EMAIL_REQUIRED=True ,
ACCOUNT_USERNAME_REQURIED=True
LOGIN_REDIRECT_URL = "/"
 
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SOCIALACCOUNT_LOGIN_ON_GET =True
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS =True
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"

AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]
SOCIALACCOUNT_PROVIDERS = {
   
    "google": {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
       
     
        # These are provider-specific settings that can only be
        # listed here:
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        }
    },
    'facebook':
{'METHOD': 'oauth2',
'SCOPE': ['email','public_profile', 'user_friends'],
'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
'FIELDS': [
'id',
'email',
'name',
'first_name',
'last_name',
'verified',
'locale',
'timezone',
'link',
'gender',
'updated_time'],
'EXCHANGE_TOKEN': True,
'LOCALE_FUNC': lambda request: 'kr_KR',
'VERIFIED_EMAIL': False,
'VERSION': 'v2.4'}}

ROOT_URLCONF = 'webshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                 'category.context_processors.menu_links',
                'carts.context_processors.counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'webshop.wsgi.application'
AUTH_USER_MODEL= 'accounts.Account'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR /'media'
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}
CROS_ORIGIN_ALLOW_ALL = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# SMTP configuration
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
"""DATABASES = {
      'default': {
       'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}"""
DATABASES = {
    'default': dj_database_url.parse(os.getenv('DATABASE_URL'), conn_max_age=600),
}
"""DATABASES = {
   'default': {
        'ENGINE': "django.db.backends.postgresql_psycopg2",
        
        
        
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
       

    }
}"""


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
#STATICFILES_DIRS = [
#    BASE_DIR / "static",]
    
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')
#STATIC_ROOT = "/static/"
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field


"""
from django.contrib.auth.models import User
DJANGO_SU_NAME = config('DJANGO_SU_NAME')
DJANGO_SU_EMAIL = config('DJANGO_SU_EMAIL')
DJANGO_SU_PASSWORD = config('DJANGO_SU_PASSWORD')

try:
    superuser = User.objects.create_superuser(
        username=DJANGO_SU_NAME,
        email=DJANGO_SU_EMAIL,
        password=DJANGO_SU_PASSWORD)
    superuser.save()
except IntegrityError:
    print(f"Super User with username {DJANGO_SU_NAME} is already present")
except Exception as e:
    print(e)"""