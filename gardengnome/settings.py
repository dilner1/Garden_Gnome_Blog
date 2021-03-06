from pathlib import Path
import os
import dj_database_url
if os.path.isfile('env.py'):
    import env

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['localhost', 'garden-gnome-blog.herokuapp.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'django_summernote',
    'crispy_forms',
    'blog',
]

SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

ACCOUNT_FORMS = {
    'login': 'allauth.account.forms.LoginForm',
    'signup': 'allauth.account.forms.SignupForm',
    'add_email': 'allauth.account.forms.AddEmailForm',
    'change_password': 'allauth.account.forms.ChangePasswordForm',
    'set_password': 'allauth.account.forms.SetPasswordForm',
    'reset_password': 'allauth.account.forms.ResetPasswordForm',
    'reset_password_from_key': 'allauth.account.forms.ResetPasswordKeyForm',
    'disconnect': 'allauth.socialaccount.forms.DisconnectForm',
}

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'gardengnome.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gardengnome.wsgi.application'

if os.environ.get("DATABASE_URL"):
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL', ))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

# DATABASES = {
#    'default': dj_database_url.parse('postgres://naeqhqcjxgofxy:be9995d0531ecc0c5218f83c7d8bc894f39a054e4993d5a0ed5acb7f0cc5168f@ec2-54-228-97-176.eu-west-1.compute.amazonaws.com:5432/d1elh9tr3gflbl')
# }


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
        'NAME':
            'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

CRISPY_TEMPLATE_PACK = 'bootstrap3'

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
