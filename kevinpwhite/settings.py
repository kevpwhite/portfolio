"""
Django settings for kevinpwhite project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import environ
import os

######################
### Custom settings###
######################
# .env settings
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

# Comment these out for development deployment.
CSRF_TRUSTED_ORIGINS = os.environ.get('CSRF_TRUSTED_ORIGINS').split(",")
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_REFERRER_POLICY = "strict-origin"
SECURE_BROWSER_XSS_FILTER = True
CAPTCHA_FONT_SIZE=42
CAPTCHA_IMAGE_SIZE=[200,48]
CAPTCHA_BACKGROUND_COLOR="#ffffff"
#Honeypot settings
HONEYPOT_FIELD_NAME = 'user_name'
HONEYPOT_VALUE = 'kevinpwhite'

# Site ID is needed for this
SITE_ID = 1

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 0

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(",")

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'portfolio',
    'blog',
    'mptt',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'captcha',
    'honeypot',
    'django_ckeditor_5',
]

MIDDLEWARE = [
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

JAZZMIN_SETTINGS = {
    "site_title": "Portfolio Admin",
    "site_header": "Portfolio Administration",
    "site_brand": "Kevin P White",
    "site_logo": "images/logo.webp",
    "login_logo": "images/logo.webp",
    "login_logo_dark": None,
    "site_icon": None,
    "welcome_sign": "Welcome to Portfolio Admin",
    "copyright": "Kevin P White",

    "icons": {
        "auth": "fas fa-lock",
        "auth.User": "fas fa-user",
        "auth.Group": "fa-solid fa-users",
        "sites.Site": "fas fa-globe",
    },

    "topmenu_links": [
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Live Site", "url": "https://techprohq.com", "new_window": True},
        {"model": "auth.User"},
    ],

    # Further settings can be added or adjusted as needed...
}

# CKEditor Configs
customColorPalette = [
        {
            'color': 'hsl(4, 90%, 58%)',
            'label': 'Red'
        },
        {
            'color': 'hsl(340, 82%, 52%)',
            'label': 'Pink'
        },
        {
            'color': 'hsl(291, 64%, 42%)',
            'label': 'Purple'
        },
        {
            'color': 'hsl(262, 52%, 47%)',
            'label': 'Deep Purple'
        },
        {
            'color': 'hsl(231, 48%, 48%)',
            'label': 'Indigo'
        },
        {
            'color': 'hsl(207, 90%, 54%)',
            'label': 'Blue'
        },
    ]

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': [
            'heading', '|', 'outdent', 'indent', '|', 
            'bold', 'italic', 'link', 'underline', 'strikethrough', 
            'code', 'subscript', 'superscript', 'highlight', '|', 
            'codeBlock', 'bulletedList', 'numberedList', 'todoList', '|', 
            'blockQuote', 'imageUpload', 'mediaEmbed', 'sourceEditing', '|', 
            'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 
            'removeFormat', 'insertTable'
        ],
        'image': {
            'toolbar': [
                'toggleImageCaption', '|', 'imageTextAlternative', '|', 
                'imageStyle:alignLeft', 'imageStyle:alignRight', 
                'imageStyle:alignCenter', '|', 'imageStyle:side', 
                'imageStyle:inline', '|'
            ],
            'styles': [
                'full', 'side', 'alignLeft', 'alignRight', 'alignCenter'
            ]
        },
        'table': {
            'contentToolbar': [
                'tableColumn', 'tableRow', 'mergeTableCells', 
                'tableProperties', 'tableCellProperties'
            ],
            'tableProperties': {
                'borderColors': 'customColorPalette',
                'backgroundColors': 'customColorPalette'
            },
            'tableCellProperties': {
                'borderColors': 'customColorPalette',
                'backgroundColors': 'customColorPalette'
            }
        },
        'heading': {
            'options': [
                {'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph'},
                {'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1'},
                {'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2'},
                {'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3'}
            ]
        },
        'htmlSupport': {
            'allow': [
                {'name': '/.*/', 'attributes': True, 'classes': True, 'styles': True}
            ]
        },
        'extraAllowedContent': 'iframe[*]{*}(*)',  # Allow iframes with all attributes
        'mediaEmbed': {
            'previewsInData': True
        },
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3', '|', 
            'bulletedList', 'numberedList', '|', 'blockQuote', 
            'imageUpload'
        ]
    },
    'list': {
        'properties': {
            'styles': True,
            'startIndex': True,
            'reversed': True,
        }
    }
}


ROOT_URLCONF = env('ROOT_URLCONF')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = env('WSGI_APPLICATION')

DATABASES = {
    "default": {
        "ENGINE": env('SQL_ENGINE'),
        "NAME": env('POSTGRES_DB'),
        "USER": env('POSTGRES_USER'),
        "PASSWORD": env('POSTGRES_PASSWORD'),
        "HOST": env('SQL_HOST'),
        "PORT": env('SQL_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# CKEditor file upload path
CKEDITOR_UPLOAD_PATH = "uploads/ckeditor/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email settings
SERVER_EMAIL = env('EMAIL_ADDRESS')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_PASSWORD = env('EMAIL_PASSWORD')
EMAIL_HOST_USER = SERVER_EMAIL
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')

ADMINS = [
    (env('EMAIL_ADMIN'), env('EMAIL_ADDRESS')),
]