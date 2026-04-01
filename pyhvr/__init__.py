"""Module docstring text"""
__version__ = "0.1.0"
from pyhvr.pyhvr_client import Client


def client(username, password, uri, verify=True):
    return Client(username=username, password=password, uri=uri, setup_mode=False, verify=verify)


def client_setup_mode(uri):
    return Client(uri=uri, setup_mode=True)
