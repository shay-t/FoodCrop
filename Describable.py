from abc import ABC, abstractmethod, abstractclassmethod
from hashlib import new

class Describable(ABC):
    def __init__(self) :
        pass
    @abstractmethod
    def describe(self) -> str:
        pass
