from .base import *
import environ

env = environ.Env()
environ.Env.read_env()

DEBUG = False
SECRET_KEY = env('SECRET_KEY')

try:
    from .local import *
except ImportError:
    pass
