import pytest
from pickle_db import PickleDB
import os

CACHE_FILE = 'tests/cache.lock'
NAME = 'Wayne'
CITY = 'Gothan'


def delete_cache():
    if os.path.exists(CACHE_FILE):
        os.remove(CACHE_FILE)


def test_pickle_db():
    delete_cache()
    db = PickleDB(CACHE_FILE)
    db.name = NAME
    assert os.path.exists(CACHE_FILE)


def test_load_pickle_db():
    db = PickleDB(CACHE_FILE)
    db.name = NAME
    assert db.name == NAME
    delete_cache()


def test_pickle_save_content():
    db = PickleDB(CACHE_FILE)
    db.clean_cache()
    db.name = NAME
    size_without_name = db.sizeof()
    db.city = CITY
    size_with_name = db.sizeof()

    assert size_without_name != size_with_name


def test_pickle_delete_content():
    db = PickleDB(CACHE_FILE)
    db.clean_cache()

    db.name = NAME
    db.city = CITY
    size_with_name = db.sizeof()
    del db.name
    size_without_name = db.sizeof()

    assert size_without_name != size_with_name