from IndicatorGroup import IndicatorGroup
from Unit import Unit
from Describable import Describable
class Indicator(Describable) :
    def __init__(self, id : str, frequency : int, frequencyDesc: str, geoLocation: str, indicatorGroup: IndicatorGroup, unit : Unit ):
        self.id = id
        self.__frequency = frequency
        self.__frequencyDesc = frequencyDesc
        self.__geoLocation = geoLocation
        self.indicatorGroup = indicatorGroup
        self.unit = unit

    def describe(self):
        return "id : " + str(self.id) + " frequency : " + str(self.__frequency) + "\n frequency Description :" + self.__frequencyDesc +  "geo Location" +   self.__geoLocation + "Indicator Group " + self.indicatorGroup.name + self.unit.describe()
        



