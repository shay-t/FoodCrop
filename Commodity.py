from CommodityGroup import CommodityGroup
from Describable import Describable


class Commodity(Describable):
    def __init__(self, id : int, name : str, commodityGroup : CommodityGroup):
        self.id = id
        self.__name = name
        self.commodityGroup = commodityGroup

    def describe(self):
        return "id : " + str(self.id) + " name : " + self.__name + "\n CommodityGroup :" + self.commodityGroup.name




