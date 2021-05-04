
from abc import ABCMeta, abstractmethod

class Computador(metaclass=ABCMeta):


    @property
    def getInformacoes(self):
        pass


    @abstractmethod
    def cadastrar(self):
        pass


