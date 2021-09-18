[![License](http://img.shields.io/:license-apache-blue.svg?style=flat-square)](http://www.apache.org/licenses/LICENSE-2.0.html)
[![PyPI Downloads](http://img.shields.io/pypi/dm/pickle-db.svg)](https://pypi.python.org/pypi/pickle-db)


# PickleDB

Save attributes of one Object in one pickle file to reload object state after python program
was closed.

You can use to save singletons of settings or progress state of one program.

This project was basead in DBM :D

# Features

* auto manager file
* save pickle in differents protocol
* reload object with same state before panic problem
* share setings/state bettween multiple aplications
* delete/create/update attribute from object auto will be saved in file


## To install

```
    pip install pickle-db
```

## Usage


```
    # create cache
    $ python
    >> from pickle_db import PickleDB
    >> db = PickleDB("cache.pcl")
    >> db.name = "Wayne"
    >> exit()

    # list file created by pickle_db
    $ ls
    cache.pcl

    # reload file create by pickle_db
    $ python
    >> from pickle_db import PickleDB
    >> db = PickleDB("cache.pcl")
    >> db.name
    "Wayne"
```
