from .base import *

DEBUG = False
SECRET_KEY = env('SECRET_KEY')

try:
    from .local import *
except ImportError:
    pass
