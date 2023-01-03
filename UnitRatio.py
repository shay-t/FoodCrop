from Unit import Unit

class UnitRatio(Unit):
    def __init__(self, id: int, name: str, unit1 : Unit , unit2 : Unit):
        super().__init__(id, name)
        self.unit1 = unit1
        self.unit2 = unit2
    def describe(self) -> str:
        return super().describe() +"\n la description de la premiere unité " +self.unit1.describe()+"\n la description de la deuxieme unité" +self.unit2.describe()