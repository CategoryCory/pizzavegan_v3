from .base import *

DEBUG = False
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = ['pizzavegan.com', 'www.pizzavegan.com', ]

try:
    from .local import *
except ImportError:
    pass
