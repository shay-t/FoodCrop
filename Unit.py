from abc import ABC, abstractmethod 
from Describable import Describable

class Unit(Describable):

    def __init__(self,id: int,name: str):
        super().__init__()
        self.id = id 
        self.name=name

    def describe(self) -> str:
        return "id : " + str(self.id) + " name : " + self.name

#*****************************

