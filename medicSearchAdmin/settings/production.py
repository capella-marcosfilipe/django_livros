from .settings import *
from dotenv import load_dotenv
import os

load_dotenv()

DEBUG = False

SECRET_KEY = str(os.getenv('SECRET_KEY'))

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}