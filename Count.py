from Unit import Unit

class Count(Unit):
    def __init__(self, id: int,what: str,name: str="Count"):
        super().__init__(id,name)
        self.__what = what

    def describe(self):
        return super().describe() + "\n what :" + self.__what
        

