from .pickle_db import PickleDB


def get_version():
    return "0.1.1"


__all__ = ["get_version", "PickleDB"]
