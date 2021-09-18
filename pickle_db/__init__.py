from .pickle_db import PickleDB


def get_version():
    return "0.1.0"


__all__ = ["get_version", "PickleDB"]
