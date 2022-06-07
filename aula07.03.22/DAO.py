import pickle
from abc import ABC

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

class Cliente:
    def __int__(self, codigo: int, nome: str):
        super().__init__(nome)
        self.__codigo = codigo

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo


class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('clientes.pkl')

    def add(self, cliente: Cliente):
        if (isinstance(cliente.codigo, int)) and (cliente is not None) and isinstance(cliente, Cliente):
            super().add(cliente.codigo, cliente)

    def get(selfself, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself,key: int):
        if isinstance(key, int):
            return super().remove(key)



