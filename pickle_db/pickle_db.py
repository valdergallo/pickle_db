import pickle
import os
import logging

DEBUG = False


def debug_print(*args):
    if DEBUG:
        print(args)


class FileManager(object):
    def __init__(self, file_name, save_protocol):
        self.file_name = file_name
        self.save_protocal = save_protocol

    def save(self, context):
        with open(self.file_name, "wb") as out:
            debug_print("Save", context, out)
            pickle.dump(context, out, protocol=self.save_protocal)

    def load(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "rb") as out:
                data_load = pickle.load(out)
                debug_print("Load", data_load, out)
                return data_load
        return {}


class PickleDB(object):
    def __init__(self, file_name, save_protocol=2, debug=False):
        global DEBUG
        DEBUG = debug

        self.__cache = FileManager(file_name=file_name, save_protocol=save_protocol)
        self.__context = {}
        self.__load()

    def __load(self):
        context = self.__cache.load()
        self.__context = context
        self.__dict__.update(context)

    def __setattr__(self, name, value):
        debug_print("Set: ", name, value)
        if "__" not in name:
            self.__context[name] = value
            self.__cache.save(self.__context)
        super(PickleDB, self).__setattr__(name, value)

    def __getattr__(self, name):
        return self.__dict__.get(name)

    def __delattr__(self, name):
        debug_print("Delete: ", name)
        if "__" not in name:
            self.__context.pop(name, "")
            self.__cache.save(self.__context)
        super(PickleDB, self).__delattr__(name)

    def clean_cache(self):
        self.__context = {}
        self.__cache.save(self.__context)

    def sizeof(self):
        if os.path.exists(self.__cache.file_name):
            return os.path.getsize(self.__cache.file_name)
        return 0

