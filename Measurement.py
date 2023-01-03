from Commodity import Commodity
from Indicator import Indicator
from Indicator import Describable

class Measurement(Describable):
    staticid = 0
    def __init__(self, id: int, year : int, value : float, timeperiodId : int, timeperiodDesc : str, commodity : Commodity, indicator : Indicator):
        self.id=id
        Measurement.staticid += 1
        self.__year = year
        self.__value = value
        self.__timeperiodId = timeperiodId
        self.__timeperiodDesc = timeperiodDesc
        self.commodity = commodity
        self.indicator = indicator


    def describe(self):
        return "\n Measurment id: " + str(self.id)+" year "+str(self.__year)+" value "+str(self.__value)+" timeperiodId "+str(self.__timeperiodId)+" timeperiodDesc "+self.__timeperiodDesc+" commodity " + self.commodity.describe()+"indicator"+self.indicator.describe()


