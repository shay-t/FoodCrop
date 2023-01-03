from Commodity import Commodity
from Indicator import Indicator
from Measurement import Measurement
from CommodityGroup import CommodityGroup
from IndicatorGroup import IndicatorGroup
from Unit import Unit
from Volume import Volume
from Price import Price
from Weight import Weight
from Count import Count
from Ratio import Ratio
from Surface import Surface
from UnitRatio import UnitRatio

class FoodCropFactory :
    def __init__(self):
        self.__unitsRegistry={}
        self.__indicatorsRegistry={}
        self.__commodityRegistry={}
        
    def getUnitsRegistry(self) -> dict:
        return self.__unitsRegistry

    def getIndicatorsRegistry(self) -> dict:
        return self.__indicatorsRegistry

    def getCommodityRegistry(self) -> dict:
        return self.__commodityRegistry    

    def createVolume(self, id : int , name : str) -> Unit:
        if(id not in self.__unitsRegistry):
            volume = Volume(id,name)
            self.__unitsRegistry[id]=volume
        return self.__unitsRegistry[id]

    def createPrice(self, id : int , name : str) -> Unit:
        if(id not in self.__unitsRegistry.keys()):
            price = Price(id,name)
            self.__unitsRegistry[id]=price
        return self.__unitsRegistry[id]

    def createWeight(self, id : int ,multiplier : int , name : str) -> Unit:
        if(id not in self.__unitsRegistry):
            weight = Weight(id,multiplier,name)
            self.__unitsRegistry[id]=weight
        return self.__unitsRegistry[id]
            

    def createSurface(self, id : int,name : str) -> Unit:
        if(id not in self.__unitsRegistry):
            surface = Surface(id,name)
            self.__unitsRegistry[id]=surface
        return self.__unitsRegistry[id]

    def createCount(self, id: int , what: str , name : str) -> Unit:
        if(id not in self.__unitsRegistry):
            count = Count(id,what,name)
            self.__unitsRegistry[id]=count
        return self.__unitsRegistry[id]

    def createRatio(self, id: int, name : str) -> Unit:
        if(id not in self.__unitsRegistry):
            ratio = Ratio(id,name)
            self.__unitsRegistry[id] = ratio
        return self.__unitsRegistry[id]

    def createUnitRatio(self, id:int , unite1: Unit , unite2: Unit):
        if(id not in self.__unitsRegistry):
            unitRatio = UnitRatio(id,unite1,unite2)
            self.__unitsRegistry[id] = unitRatio
        return self.__unitsRegistry[id]

    def createCommodity(self, group : CommodityGroup , id : int, name : str  ) -> Commodity :
        if(id not in self.__commodityRegistry):
            commodity = Commodity(id, name, group)
            self.__commodityRegistry[id]=commodity
        return self.__commodityRegistry[id]

    def createIndicator(self,id : str, frequency : int , freqDesc : str, geoLocation : str, indicatorGroup : IndicatorGroup, unit : Unit) -> Indicator:
        if(id not in self.__commodityRegistry):
            idi = id.split(",")[0]
            indicator = Indicator(idi, frequency, freqDesc, geoLocation, indicatorGroup, unit)
            self.__indicatorsRegistry[id]=indicator
        return self.__indicatorsRegistry[id]

    def createMeasurement(self, id : int, year : int, value : float, timeperiodId : int, timeperiodDesc : str, commodity : Commodity, indicator : Indicator) -> Measurement:
        measurement = Measurement(id, year, value, timeperiodId, timeperiodDesc, commodity, indicator)
        return measurement



