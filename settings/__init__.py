import logging.config
from .base import *

try:
    from .local import *  # noqa
except ImportError:
    exit('User, fill in local.py, please!'
         '\nUse command: "cp settings/local.py.default settings/local.py"'
         '\nSet valid database connection data and other parameters in local.py')

try:
    logging.config.dictConfig(LOGGING)
except NameError:
    exit('Define LOGGING in settings')
