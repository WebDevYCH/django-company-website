import os
import sys
import datetime

from django.utils.translation import gettext_lazy  as _
from dotenv import load_dotenv, find_dotenv
from django_replicated.settings import *
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'extra_apps'))
import logging.config
from agrosite.environment import EnvironmentChecker
LOGGING_CONFIG = None

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            # exact format is not important, this is the minimum information
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        }
    },
    'loggers': {
        # root logger
        '': {
            'level': 'INFO',
            'handlers': ['console'],
        },
    },
})

logger = logging.getLogger(__name__)
load_dotenv(verbose=True, dotenv_path=find_dotenv())
ENVIRONMENT = os.environ.get('ENVIRONMENT')

if not ENVIRONMENT:
    if 'test' in sys.argv:
        logger.info('No ENVIRONMENT variable found but test detected. Setting ENVIRONMENT=TEST_VALUE')
        ENVIRONMENT = EnvironmentChecker.TEST_VALUE
    else:
        raise NameError('ENVIRONMENT environment variable is required')

# SECURITY WARNING: keep the secret key used in production secret!
environment_checker = EnvironmentChecker(environment_value=ENVIRONMENT)
SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    raise NameError('SECRET_KEY environment variable is required')
# SECURITY WARNING: don't run with debug turned on in production!

# Application definition
ARTICLE_PAGINATE_BY = 8

BOOK_MOVIE_PAGINATE_BY = 8
LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True



HAYSTACK_SEARCH_RESULTS_PER_PAGE = 7
INSTALLED_APPS = [
    # Extend the INSTALLED_APPS setting by listing additional applications here
    'django.contrib.sites',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.humanize',
    
    'comment',
    'notice',
    'setting',
    'notifications',
    'myzone',
    'home',
    'likeunlike',
    'careers',
    'contactus',
    'about',
    'services',
    'accounts',
    
    'xadmin',
    'haystack',
    'mdeditor',
    'ckeditor',
    'crispy_forms',
    'rest_framework',
    'django_summernote',

    'storages',
    'django_rq',
    'scheduler',
    'compressor',

    'blog',
    'portfolio',
    'servermanager',
    
    'cacheops',
    'django_extensions',
    'django_nose',
    # Django Elasticsearch integration
    # 'django_elasticsearch_dsl',

    # # Django REST framework Elasticsearch integration (this package)
    # 'django_elasticsearch_dsl_drf',
]
SITE_ID = 1
DEBUG = environment_checker.is_debug()
IS_PRODUCTION = environment_checker.is_production()
IS_BUILD = environment_checker.is_build()
TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS')
if IS_PRODUCTION:
    if not ALLOWED_HOSTS:
        raise NameError('ALLOWED_HOSTS environment variable is required when running on a production environment')
    ALLOWED_HOSTS = [allowed_host.strip() for allowed_host in ALLOWED_HOSTS.split(',')]
else:
    if ALLOWED_HOSTS:
        logger.info('ALLOWED_HOSTS environment variable ignored.')
    ALLOWED_HOSTS = ['*']
JWT_ALGORITHM = os.environ.get('JWT_ALGORITHM', 'HS256')

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'agrosite.middleware.TimezoneMiddleware',
    'blog.middleware.OnlineMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


CKEDITOR_CONFIGS = {
    'comment_ckeditor': {
        'toolbar': 'custom',
        'toolbar_custom': [
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ["TextColor", "BGColor", 'RemoveFormat'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink'],
            ["Smiley", "SpecialChar", 'Blockquote','CodeSnippet'],
        ],
        'width': 'auto',
        'height': '180',
        'tabSpaces': 4,
        'removePlugins': 'elementspath',
        'resize_enabled': False,

        'extraPlugins': ','.join(['codesnippet', 'uploadimage', 'widget', 'lineutils', ]),
    },

    'default': {
        'toolbar': 'custom',
        'toolbar_custom': [
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript'],
            ["TextColor", "BGColor", 'RemoveFormat'],
            ['NumberedList', 'BulletedList'],
            ['Link', 'Unlink'],
            ["Smiley", "SpecialChar", 'Blockquote'],
        ],
        'width': 'auto',
        'height': '180',
        'tabSpaces': 4,
        'removePlugins': 'elementspath',
        'resize_enabled': False,
    }
}

# ELASTICSEARCH_DSL = {
#     'default': {
#         'hosts': 'esearch1:9200'
#     },
# }
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'agrosite.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
DJANGO_NOTIFICATIONS_CONFIG = {
    'USE_JSONFIELD': True
}
PAGINATE_BY = 10
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DATE_TIME_FORMAT = '%Y-%m-%d'
SILENCED_SYSTEM_CHECKS = ['mysql.E001']

ROOT_URLCONF = "agrosite.urls"
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'blog.context_processors.seo_processor',
            ]
        },
    }
]

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.rq import RqIntegration


WSGI_APPLICATION = "agrosite.wsgi.application"

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE" : "django.db.backends.sqlite3",
#         "NAME": os.path.join(BASE_DIR, "db.sqlite3")
#     }
# } 
if IS_BUILD or TESTING:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    RDS_DB_NAME = os.environ.get('RDS_DB_NAME')
    RDS_USERNAME = os.environ.get('RDS_USERNAME')
    RDS_PASSWORD = os.environ.get('RDS_PASSWORD')
    RDS_PORT = os.environ.get('RDS_PORT')
    RDS_HOSTNAME = os.environ.get('RDS_HOSTNAME')

    RDS_HOSTNAME_WRITER = os.environ.get('RDS_HOSTNAME_WRITER', RDS_HOSTNAME)
    RDS_HOSTNAME_READER = os.environ.get('RDS_HOSTNAME_READER', RDS_HOSTNAME_WRITER)
    


    writer_db_config = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': RDS_DB_NAME,
        'USER': RDS_USERNAME,
        'PASSWORD': RDS_PASSWORD,
        'HOST': RDS_HOSTNAME_WRITER,
        'PORT': RDS_PORT,
    }

    DATABASES = {
        
        'default': writer_db_config,
        'Reader': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': RDS_DB_NAME,
            'USER': RDS_USERNAME,
            'PASSWORD': RDS_PASSWORD,
            'HOST': RDS_HOSTNAME_READER,
            'PORT': RDS_PORT,
        },
        'slave':writer_db_config,
        
    }
    
    # DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
# }
    DATABASE_ROUTERS = ['django_replicated.router.ReplicationRouter']

    REPLICATED_DATABASE_SLAVES = ['slave','Reader', ]

    MIDDLEWARE.append('django_replicated.middleware.ReplicationMiddleware')

    REPLICATED_VIEWS_OVERRIDES = {
        '/admin/*': 'master',
        '/article/*': 'master',
        '/': 'master',
        '/careers/*': 'master',
        '/logout/':'master'
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

AWS_TRANSLATE_REGION = os.environ.get('AWS_TRANSLATE_REGION', 'eu-central-1')
AWS_TRANSLATE_MAX_LENGTH = os.environ.get('AWS_TRANSLATE_MAX_LENGTH', 10000)
OS_TRANSLATION_STRATEGY_NAME = 'default'
OS_TRANSLATION_CONFIG = {
    'default': {
        'STRATEGY': 'agrotranslation.strategies.amazon.AmazonTranslate',
        'TEXT_MAX_LENGTH': AWS_TRANSLATE_MAX_LENGTH,
        'DEFAULT_TRANSLATION_LANGUAGE_CODE': 'en'
    },
    'testing': {
        'STRATEGY': 'agrotranslation.strategies.tests.MockAmazonTranslate',
        'TEXT_MAX_LENGTH': 40,
        'DEFAULT_TRANSLATION_LANGUAGE_CODE': 'en'
    }
}
AUTH_USER_MODEL = 'accounts.Employer'
AUTHENTICATION_BACKENDS = ['accounts.user_login_backend.EmailOrUsernameModelBackend']
LOGIN_URL = '/login/'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


LIKES_MODELS = {
    "blog.Article": {
        'serializer': 'article.api.serializers.ArticleSerializer'
    },
    "careers.Job": { },
}


UNICODE_JSON = True

# The sentry DSN for error reporting
SENTRY_DSN = os.environ.get('SENTRY_DSN')
if IS_PRODUCTION:
    if not SENTRY_DSN:
        raise NameError('SENTRY_DSN environment variable is required when running on a production environment')
    sentry_sdk.init(
        dsn="https://8892e599055947fda909ad6f13810175@o377184.ingest.sentry.io/5198925",
        integrations=[DjangoIntegration(), RqIntegration()],

        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True
    )
else:
    if SENTRY_DSN:
        logger.info('SENTRY_DSN environment variable ignored.')
        
LANGUAGES = [
    ('es', _('Spanish')),
    ('en', _('English')),
    ('de', _('German')),
    ('nl', _('Dutch')),
    ('da', _('Danish')),
    ('hu', _('Hungarian')),
    ('sv', _('Swedish')),
    ('fr', _('French')),
    ('it', _('Italian')),
    ('tr', _('Turkish')),
    ('pt-br', _('Portuguese, Brazilian')),
]

MEDIA_ROOT = os.environ.get('MEDIA_ROOT', './media')

MEDIA_URL = os.environ.get('MEDIA_URL', '/media/')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'agrosite/static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

PROXY_URL = os.environ.get('PROXY_URL', '')

REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.environ.get('REDIS_PORT', '6379'))
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')

redis_protocol = 'redis://' if IS_PRODUCTION else 'redis://'

redis_password = '' if not REDIS_PASSWORD else ':%s' % REDIS_PASSWORD

REDIS_LOCATION = '%(protocol)s%(password)s@%(host)s:%(port)d' % {'protocol': redis_protocol,
                                                                    'password': redis_password,
                                                                    'host': REDIS_HOST,
                                                                    'port': REDIS_PORT}

RQ_SHOW_ADMIN_LINK = False

REDIS_DEFAULT_CACHE_LOCATION = '%(redis_location)s/%(db)d' % {'redis_location': REDIS_LOCATION, 'db': 0}
REDIS_RQ_DEFAULT_JOBS_CACHE_LOCATION = '%(redis_location)s/%(db)d' % {'redis_location': REDIS_LOCATION, 'db': 1}
REDIS_RQ_HIGH_JOBS_CACHE_LOCATION = '%(redis_location)s/%(db)d' % {'redis_location': REDIS_LOCATION, 'db': 2}
REDIS_RQ_LOW_JOBS_CACHE_LOCATION = '%(redis_location)s/%(db)d' % {'redis_location': REDIS_LOCATION, 'db': 3}


CACHES = {
    'default': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_DEFAULT_CACHE_LOCATION,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "ob-api-"
    },
    'rq-default-jobs': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_RQ_DEFAULT_JOBS_CACHE_LOCATION,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "ob-api-rq-default-job-"
    },
    'rq-high-jobs': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_RQ_HIGH_JOBS_CACHE_LOCATION,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "ob-api-rq-high-job-"
    },
    'rq-low-jobs': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_RQ_LOW_JOBS_CACHE_LOCATION,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "ob-api-rq-low-job-"
    },
}

CACHEOPS_REDIS_DB = int(os.environ.get('CACHEOPS_REDIS_DB', '1'))

CACHEOPS_REDIS = '%(redis_location)s/%(db)d' % {'redis_location': REDIS_LOCATION, 'db': CACHEOPS_REDIS_DB}

CACHEOPS_DEFAULTS = {
    'timeout': 60 * 60
}

CACHEOPS = {
    # Don't cache anything automatically
    '*.*': {},
}

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other
    'compressor.finders.CompressorFinder',
)
COMPRESS_ENABLED = True
# COMPRESS_OFFLINE = True


COMPRESS_CSS_FILTERS = [
    # creates absolute urls from relative ones
    'compressor.filters.css_default.CssAbsoluteFilter',
    # css minimizer
    'compressor.filters.cssmin.CSSMinFilter'
]
COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter'
]

RQ_QUEUES = {
    'default': {
        'USE_REDIS_CACHE': 'rq-default-jobs',
    },
    'high': {
        'USE_REDIS_CACHE': 'rq-high-jobs',
    },
    'low': {
        'USE_REDIS_CACHE': 'rq-low-jobs',
    },
}

if IS_BUILD:
    NOSE_ARGS = [
        '--cover-erase',
        '--cover-package=.',
        '--with-spec', '--spec-color',
        '--with-coverage', '--cover-xml',
        '--verbosity=1', '--nologcapture']
else:
    NOSE_ARGS = [
        '--cover-erase',
        '--cover-package=.',
        '--with-spec', '--spec-color',
        '--with-coverage', '--cover-html',
        '--cover-html-dir=reports/cover', '--verbosity=1', '--nologcapture', '--nocapture']
FAILED_JOB_THRESHOLD = 20
ACTIVE_JOB_THRESHOLD = 50
ACTIVE_WORKER_THRESHOLD = 5
ALERT_HOOK_URL = os.environ.get('ALERT_HOOK_URL')

EMAIL_BACKEND = 'django_amazon_ses.EmailBackend'
AWS_SES_REGION = os.environ.get('AWS_SES_REGION')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
SERVICE_EMAIL_ADDRESS = os.environ.get('SERVICE_EMAIL_ADDRESS')
EMAIL_HOST = os.environ.get('EMAIL_HOST')

# AWS Storage config

AWS_PUBLIC_MEDIA_LOCATION = os.environ.get('AWS_PUBLIC_MEDIA_LOCATION')
AWS_STATIC_LOCATION = 'static'
AWS_PRIVATE_MEDIA_LOCATION = os.environ.get('AWS_PRIVATE_MEDIA_LOCATION')
AWS_DEFAULT_ACL = None

if TESTING:
    OS_TRANSLATION_STRATEGY_NAME = 'testing'
    MIN_UNIQUE_TOP_POST_REACTIONS_COUNT = 1
    MIN_UNIQUE_TOP_POST_COMMENTS_COUNT = 1
    MIN_UNIQUE_TRENDING_POST_REACTIONS_COUNT = 1

if IS_PRODUCTION:
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME')
    AWS_S3_ENCRYPTION = True
    AWS_S3_SIGNATURE_VERSION = 's3v4'
    AWS_S3_HOST = os.environ.get('AWS_S3_HOST', 's3.amazonaws.com')
    AWS_S3_CUSTOM_DOMAIN = '%s.%s' % (AWS_STORAGE_BUCKET_NAME, AWS_S3_HOST)

    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=86400',
    }

    STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)

    MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_PUBLIC_MEDIA_LOCATION)

    STATICFILES_STORAGE = 'agrosite.storage_backends.S3StaticStorage'

    DEFAULT_FILE_STORAGE = 'agrosite.storage_backends.S3PublicMediaStorage'

    PRIVATE_FILE_STORAGE = 'agrosite.storage_backends.S3PrivateMediaStorage'
else:
    STATIC_URL = '/static/'
    
# ONE SIGNAL
ONE_SIGNAL_APP_ID = os.environ.get('ONE_SIGNAL_APP_ID')
ONE_SIGNAL_API_KEY = os.environ.get('ONE_SIGNAL_API_KEY')

