from Unit import Unit
class Weight(Unit):
    def __init__(self, id: int, multiplier: float,  name :str ="Weight"):
        super().__init__(id, name)
        self.__multiplier = multiplier


    def describe(self):
        return super().describe() + "\n multiplier :" + str(self.__multiplier)


