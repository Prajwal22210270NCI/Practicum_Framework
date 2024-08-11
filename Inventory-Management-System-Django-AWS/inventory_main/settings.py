"""
Django settings for inventory_main project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
#from django_aws_integrate.cred import get_secret #Calling AWS Secrets manager service from my own library
#from django_aws_integrate.logs import log_activity #Calling AWS Cloud trail service from my own library
#from .cred import get_secret # Old implementation before creating my library
#from .logs import log_activity ## Old implementation before creating my library

#log_activity() #Calling CloudTrail Function

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&ign@k70phz7dcm60#6s7$@+%ng*pdqm4f!j^sb1=fekzv@v(+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*', '6byu74162b.execute-api.eu-west-1.amazonaws.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dashboard.apps.DashboardConfig', #Dashbaord App Registered
    'user.apps.UserConfig', #Users App Registered
    'crispy_forms', #Styling User Registeration Form
    'crispy_bootstrap4',
#    'storages', # For using AWS S3
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

ROOT_URLCONF = 'inventory_main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'inventory_main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

#secret_dict = get_secret() # Calling AWS Secrets Manager for DB Credentials
 
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.'+ secret_dict['engine'], #Integrated Amazon RDS MySQL into Django and replaced default sqllite3 database 
#         'NAME': secret_dict['dbname'],
#         'USER': secret_dict['username'],
#         'PASSWORD': secret_dict['password'],
#         'HOST': secret_dict['host'], # Amazon RDS Host Public Address
#         'PORT': secret_dict['port'],
#     }
# }

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql', #Integrated Amazon RDS MySQL into Django and replaced default sqllite3 database 
         'NAME': 'projectprajwal',
         'USER': 'admin',
         'PASSWORD': 'India#2345$',
         'HOST': 'projectprajwal.clyw8o2ieoxc.eu-west-1.rds.amazonaws.com', # Amazon RDS Host Public Address
         'PORT': '3306',
     }
 }

# Default SQLite3 configuration
# DATABASES = { 
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


# Define the logging directory
LOGGING_DIR = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(LOGGING_DIR):
    os.makedirs(LOGGING_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGGING_DIR, 'django_requests.log'),
            'formatter': 'verbose',
        },
        'sql_injection_file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOGGING_DIR, 'sql_injection.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'security': {
            'handlers': ['sql_injection_file'],
            'level': 'WARNING',
            'propagate': False,
        },
    },
}


STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

STATIC_ROOT = (BASE_DIR/"asert/")

MEDIA_ROOT = (BASE_DIR/'media')

MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'dashboard-index'

AWS_ACCESS_KEY_ID = 'XXXXXXX'
AWS_SECRET_ACCESS_KEY = 'XXXXXXXXX'
AWS_REGION = 'XXXXX'
AWS_S3_REGION_NAME = 'eu-west-1' #S3 Bucket Region
AWS_STORAGE_BUCKET_NAME = 'XXXXXX' #S3 Bucket
AWS_S3_SIGNATURE_NAME = 's3v4'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL =  None
AWS_S3_VERITY = True
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage' #Boto3 client used to use S3 storage instead of Django local storage

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
