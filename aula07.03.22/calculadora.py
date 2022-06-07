import pickle

class DAO(ABC):
    def __init__(self, datasource=''):
        self.datasource = datasource
        self. objectcash = {}
        try:
            self__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.objectcash, open(self.datasource, 'wb'))

    def __load(self):
        self.objectcash = pickle.load(open(self.datasouce, 'rb'))

    def add(self, key, obj):
        self.objectcash[key] = obj
        self.__dump()

    def get(self, key):
        try:
            return self.objectcash[key]
        except KeyError:
            pass

    def remove(self, key):
        try:
            self.objectcash.pop(key)
            self.__dump()
        except KeyError:
            pass

    def get_all(self):
        return self.objectcash.values()




