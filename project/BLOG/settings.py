from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'django-insecure-w@g#t5khnt%m^km#i3w5cttr(49bxfc2wmgi=_o#$av$v)*$ni'

DEBUG = True

ALLOWED_HOSTS = [
    '*'
    # '192.168.1.8',
    # '192.168.137.1',
    # '172.21.240.1',
    # '192.168.1.1',
    # '192.168.1.3',
    # '127.0.0.1',
    # 'localhost'
]



INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # My apps
    'authors.AuthorsConfig',
    'categories.CategoriesConfig',
    'posts.PostsConfig',
    'accounts.AccountsConfig',
    'suggestions.SuggestionsConfig',
    'api.ApiConfig',
    # Others apps
    'django_summernote',
    'rest_framework',
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

ROOT_URLCONF = 'BLOG.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [Path(BASE_DIR, 'Support/FrontEnd/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
            'filters': 'Support.Code.django.TemplatesTags.basic',
            }

        },
    },
]

WSGI_APPLICATION = 'BLOG.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



REST_FRAMEWORK  = {
    'DEFAULT_AUTHENTICATION_CLASSES' : (
        'rest_framework_simplejwt.authentication.JWTAuthentication' ,
    )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=4),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=5),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
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



LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True



STATIC_URL = '/static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# My configurations

STATICFILES_DIRS = [Path(BASE_DIR, 'Support/FrontEnd/static')]
STATIC_ROOT = Path('static')
MEDIA_ROOT = Path(BASE_DIR,'Support/FrontEnd/media')
MEDIA_URL = '/media/'

SESSION_COOKIE_AGE = 60*60*24*7
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_UNIQUE_EMAIL = True

AUTH_USER_MODEL = 'accounts.User'

LOGIN_REDIRECT_URL = 'account_page'

LOGIN_URL = 'login'


if DEBUG:
    INSTALLED_APPS += [
        "debug_toolbar",
    ]

    INTERNAL_IPS = [
        "127.0.0.1",
    ]

    MIDDLEWARE += [
       "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]