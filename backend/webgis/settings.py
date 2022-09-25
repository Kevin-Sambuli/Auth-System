import os
import environ
from datetime import timedelta
from django.contrib import staticfiles

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")

ALLOWED_HOSTS = []

# Application definition
if DEBUG:
    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    EMAIL_HOST_USER = 'sambulikevin@gmail.com'
    EMAIL_PORT = env("EMAIL_PORT")
    EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
    EMAIL_USE_TLS = env("EMAIL_USE_TLS")
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
else:
    EMAIL_BACKEND = env("EMAIL_BACKEND")
    EMAIL_HOST_USER = env("EMAIL_HOST_USER")
    EMAIL_HOST = env("EMAIL_HOST")
    EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
    EMAIL_USE_TLS = env("EMAIL_USE_TLS")
    EMAIL_PORT = env("EMAIL_PORT")
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# SERVER_EMAIL = 'ardhiland@lis.com'

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
]

THIRD_PARTY_APPS = [
    'rest_framework_gis',
    'rest_framework',
    'leaflet',
    'djgeojson',
    'corsheaders',
    'djoser'

]

PROJECT_APPS = ['accounts']

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'webgis.urls'

# user custom model setting
AUTH_USER_MODEL = 'accounts.Account'
#
# LOGIN_REDIRECT_URL = "home"
# LOGOUT_REDIRECT_URL = "home"

# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.AllowAllUsersModelBackend',
#     # 'accounts.backends.CaseInsensitiveModelBackend',
# )


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        # 'DIRS': [os.path.join(BASE_DIR, 'build')],
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

WSGI_APPLICATION = 'webgis.wsgi.application'

# Database
# docker database
# DATABASES = {
#     'default': {
#         'ENGINE': env("PG_ENGINE"),
#         'NAME': env("PG_NAME"),
#         'USER': env("PG_USER"),
#         'PASSWORD': env("PG_PASS"),
#         'HOST': env("PG_DB_HOST"),
#         'PORT': env("PG_PORT"),
#     }
# }

# local database
DATABASES = {
    'default': {
        'ENGINE': env("PG_ENGINE"),
        'NAME': env("PG_NAME"),
        'USER': env("PG_USER_LOCAL"),
        'PASSWORD': env("PG_PASS_LOCAL"),
        'HOST': env("PG_HOST_LOCAL"),
        'PORT': env("PG_PORT"),
    },
    # 'openstreetmap': {
    #     'ENGINE': env("PG_ENGINE"),
    #     'NAME': env("PG_NAME_OSM"),
    #     'USER': env("PG_USER_LOCAL"),
    #     'PASSWORD': env("PG_PASS_LOCAL"),
    #     'HOST': env("PG_HOST_LOCAL"),
    #     'PORT': env("PG_PORT"),
    # }
}

# PASSWORD_RESET_TIMEOUT = 10

# heroku
# DATABASES = {
#     'default': {
#         'ENGINE': env("PG_ENGINE"),
#         'NAME': env("PG_DATABASE_NAME"),
#         'USER': env("POSTGRES_USER"),
#         'PASSWORD': env("POSTGRES_PASS"),
#         'HOST': env("PG_HOST"),
#         'PORT': env("PG_PORT"),
#     },
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'build/static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DJOSER = {
    'LOGIN_FIELD': 'email',
    'USER_CREATE_PASSWORD_RETYPE': True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True,
    'SEND_CONFIRMATION_EMAIL': True,
    'SEND_ACTIVATION_EMAIL': True,
    'SET_PASSWORD_RETYPE': True,
    'SET_USERNAME_RETYPE': True,
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}',
    'SERIALIZERS': {
        'user_create': 'accounts.serializers.AccountSerializer',
        'user': 'accounts.serializers.AccountSerializer',
        'user_delete': 'djoser.serializers.UserDeleteSerializer',
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}


CORS_ALLOW_ALL_ORIGINS = True

# CORS_ALLOWED_ORIGINS = [
#     "https://example.com",
#     "https://sub.example.com",
#     "http://localhost:8080",
#     "http://127.0.0.1:9000",
# ]