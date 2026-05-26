"""
Django settings for proxy_pjt project.
"""
from pathlib import Path
import os
from importlib.util import find_spec
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")
load_dotenv(BASE_DIR.parent.parent / ".env")

GMS_API = os.getenv("GMS_API") or os.getenv("GMS_KEY")
GMS_URL = "https://gms.ssafy.io/gmsapi/api.openai.com/v1"
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-5-nano")
IMAGE_MODEL_NAME = os.getenv("IMAGE_MODEL_NAME", "gpt-image-1-mini")
MODEL_SERVER_URL = os.getenv("MODEL_SERVER_URL", "http://localhost:8081/api/v1")

SECRET_KEY = 'django-insecure-dd2!4+a6)y-d^^t@3ls^rgh-ewuskah%zviz97(exono0tf+*a'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'proxies',
    'rest_framework',
    'django.contrib.auth',
    'django.contrib.contenttypes',
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
]

if find_spec('corsheaders'):
    INSTALLED_APPS.insert(0, 'corsheaders')
    MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

ROOT_URLCONF = 'proxy_pjt.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {},
    },
]
WSGI_APPLICATION = 'proxy_pjt.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_TZ = True

CORS_ALLOW_ALL_ORIGINS = True
