from gevent import monkey
import sys

try:
    del sys.modules['ssl']
except KeyError:
    pass

if monkey.is_module_patched('socket') is False:
    monkey.patch_socket()

if monkey.is_module_patched('ssl') is False:
    monkey.patch_ssl()

from ._connection import Connection

__version__ = '0.0.7.2'
