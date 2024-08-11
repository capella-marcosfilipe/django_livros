'''
Settings file for production environment. 
'''

from .settings import *
from dotenv import load_dotenv
import os

load_dotenv()

# When DEBUG is true and ALLOWED_HOSTS empty, it will allow local address.
DEBUG = False

SECRET_KEY = str(os.getenv('SECRET_KEY'))

# Allow localhost for now. Change to production environment when available.
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}