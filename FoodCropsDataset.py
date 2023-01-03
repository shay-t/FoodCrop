from FoodCropFactory import FoodCropFactory
import re
import pandas as pd
from IndicatorGroup import IndicatorGroup 
from CommodityGroup import CommodityGroup
from Volume import Volume
from Price import Price
from Weight import Weight
from Count import Count
from Ratio import Ratio
from Surface import Surface
from UnitRatio import UnitRatio
from Unit import Unit
from Measurement import Measurement
import math
class FoodCropsFactory:
    def __init__(self):
        self.__commodGroup={}
        self.__indicatorGroup={}
        self.__geographicalLocation={}
        self.__unit = {}
        self.__allmeasurements = []
        self.foodCropFactory = FoodCropFactory()
    print("Veuillez attendre le chargement de données \n")

    #on a definit des getters pour accéder aux clés des dictionnaires depuis le programme main pour proposer les choix aux utilisateurs
    def get_commodGroup(self):
        return self.__commodGroup
    def get_indicatorGroup(self):
        return self.__indicatorGroup
    def get_geographicalLocation(self):
        return self.__geographicalLocation
    def get_unit(self):
        return self.__unit
    def get_allmeasurements(self):
        return self.__allmeasurements
    def loadData(self, path : str):
        df = pd.read_csv(path)
        co=0         #variable utilisée pour limiter la quantité de données pendant la phase de test 
        df = df.fillna(0)
        for index, row in df.iterrows():
            co += 1
            print("\rLoading line :",index,end="")

            #Pour faciliter l'acces aux colonnes, on va les stocker dans des variables
            #on a casté les colonnes contenant des valeurs entières 
            sCGroupID = int(row["SC_Group_ID"]) 
            sCGroupCommodID = int(row["SC_GroupCommod_ID"])
            sCGeographyIndentedDesc = row["SC_GeographyIndented_Desc"]
            sCCommodityID = int(row["SC_Commodity_ID"])
            sCUnitID = int(row["SC_Unit_ID"])
            sCUnitDesc = row["SC_Unit_Desc"]
            yearID = int(row["Year_ID"])
            sCFrequencyID = int(row["SC_Frequency_ID"])
            sCFrequencyDesc = row["SC_Frequency_Desc"]
            timeperiodID = int(row["Timeperiod_ID"])
            timeperiodDesc = row["Timeperiod_Desc"]
            amount = int(row["Amount"])
            
            # On commence par créer des unités
            unite = str(sCUnitDesc).lower() #on a utilisé lower() car les unités sont ecrites avec un melange de majuscules et de miniscules 
            """on a utilisé les expressions regulières pour matcher les unités à partir du fichier csv
            et ainsi determiner la nature de chaque unité """
            if(re.search(r"gallons|liters",unite)): 
                unit=self.foodCropFactory.createVolume(sCUnitID,sCUnitDesc)
            elif(re.search(r"dollar|cents",unite)):
                unit=self.foodCropFactory.createPrice(sCUnitID,sCUnitDesc)

                """pour remplir le multiplier, on a utlisé 2 expressions regulieres pour identifier si c est 1000 OU million 
                et pour eviter que  1,000 soit consideré comme 1 à cause de la virgule"""
            elif(re.search(r"bushel|ton",unite)):
                multiplier = 1
                if(re.search(r"1,000",unite)):
                    multiplier = 1000
                if(re.search(r"million",unite)):
                    multiplier = 1000000
                unit=self.foodCropFactory.createWeight(sCUnitID,multiplier,sCUnitDesc)
            elif(re.search(r"acres|hectares",unite)):
                unit=self.foodCropFactory.createSurface(sCUnitID,sCUnitDesc)
            elif(re.search(r"index|carloads|animal",unite)):
                """on a utilisé la fonction group() du module des expressions regulières pour remplir le what par la valeur qu'on cherche 
                car Il s'agit d'une grandeur sans unité permettant de connaitre le nombre ou la quantité """
                what= re.search(r"index|carloads|animal",unite).group()
                unit=self.foodCropFactory.createCount(sCUnitID,what,sCUnitDesc)
            elif(re.search(r"ratio",unite)):
                unit=self.foodCropFactory.createRatio(sCUnitID,sCUnitDesc)              

            #on utilise ici le try catch pour gerer les valeurs autres que celles qu'on a dans l'enumeration 
            # Creation des indicateurs
            try:
                indicatorGroup = IndicatorGroup(sCGroupID)
            except ValueError: 
                indicatorGroup = IndicatorGroup.OTHER 
            idi=str(sCGroupID)+","+str(unit.id)  
            """idi = concatenation de 2 id l'un du groupe l'autre de l'unité pour obtenir une clé permettant
             de resoudre le probleme qui fait que les mesures sont cherchés en se basant uniquement sur l'id du groupe """
            indicator=self.foodCropFactory.createIndicator(idi,sCFrequencyID,sCFrequencyDesc,sCGeographyIndentedDesc,indicatorGroup,unit)
            
            # instanciation de la classe commodity
            try:
                commodityGroup = CommodityGroup(sCGroupCommodID)
            except ValueError:
                commodityGroup = CommodityGroup.OTHER
            
            commodity=self.foodCropFactory.createCommodity(commodityGroup,sCCommodityID,commodityGroup.name)


            #A ce stade on va pouvoir instancier notre measurement

            measurement=self.foodCropFactory.createMeasurement(Measurement.staticid,yearID,amount,timeperiodID,timeperiodDesc,commodity,indicator)

            self.__allmeasurements.append(measurement)

            #Il ne reste plus qu'indexer les mesures
            ####################################

            #indexation selon CommodityGroup
            #si commodityGroup n'est pas dans le dictionnaire on cree une liste vide comme valeur de la clé associéé
            if(commodityGroup not in self.__commodGroup.keys()):
                self.__commodGroup[commodityGroup]=[]
            self.__commodGroup[commodityGroup].append(measurement)

            ####################################

            #indexation selon indicatorgroup
        
            if(indicatorGroup not in self.__indicatorGroup.keys()):
                self.__indicatorGroup[indicatorGroup] = []
            self.__indicatorGroup[indicatorGroup].append(measurement)

            ####################################
            #indexation selon geographical location

            if(sCGeographyIndentedDesc not in self.__geographicalLocation.keys()):
                self.__geographicalLocation[sCGeographyIndentedDesc]=[]
            self.__geographicalLocation[sCGeographyIndentedDesc].append(measurement)
            
            #####################################
            #indexation selon unité
            
            if(unit not in self.__unit.keys()):
                self.__unit[unit]=[]
            self.__unit[unit].append(measurement)



        

        print("\nChargement terminé, merci pour votre patience!\n")

    
#fonction de recherche des mesures selon les critères choisis par l'utilisateur 
    def findMeasurments(self, commodityType: CommodityGroup = None, indicatorGroup : IndicatorGroup = None, geographicalLocation : str = None,unit : Unit = None) -> list() :
        measurments = []
        
        if(commodityType):
            measurments=self.__commodGroup[commodityType]
        else:
            measurments = self.__allmeasurements.copy()

        if(indicatorGroup):
            rindicatorGroup = self.__indicatorGroup[indicatorGroup]
            measurments = list(set.intersection(set(measurments) , set(rindicatorGroup)))

        if(geographicalLocation):
            rgeographical = self.__geographicalLocation[geographicalLocation]
            measurments = list(set.intersection(set(measurments) , set(rgeographical)))

        if(unit):
            runit = self.__unit[unit]
            measurments = list(set.intersection(set(measurments) , set(runit)))

        return measurments
        





#Le programme main du projet

if __name__ == "__main__" :

    print("Bienvenu dans le programme principal \n")
    mi=FoodCropsFactory()
    mi.loadData('FeedGrains.csv')
    """for m in all:
        print(m.describe())"""
    q=int(input("tapez 1 pour continuer ou 0 pour quitter\n"))
    while(q!=0):
        print("Vous allez commencer une recherche \n veuillez choisir vos critères")
        i=0
        commodityType = None
        indicatorGroup = None
        geographicalLocation = None
        natureUnit = None
        unit = None
        while(i<4):
            i+=1
            print("1/ Type de culture")
            print("2/ Type d'indicateur")
            print("3/ Localisation")
            print("4/ unite")
            print("5/ fin")
            choice=int(input("Veuillez saisir votre choix: "))
            if(choice==1):
                l = list(dict(mi.get_commodGroup()).keys())
                print("*"*50)
                for j in range(len(l)):
                    print("{} / pour {}".format(j,l[j].name))
                choice2 = int(input("Veuillez Choisir votre type de culture: "))
                commodityType = l[choice2]
            elif(choice==2):
                l = list(dict(mi.get_indicatorGroup()).keys())
                print("*"*50)
                for j in range(len(l)):
                    print("{} / pour {}".format(j,l[j].name))
                choice2 = int(input("Veuillez Choisir votre type d'indicateur: "))
                indicatorGroup = l[choice2]
            elif(choice==3):
                l = list(dict(mi.get_geographicalLocation()).keys())
                print("*"*50)
                for j in range(len(l)):
                    print("{} / pour {}".format(j,l[j]))
                choice2 = int(input("Veuillez Choisir votre geo localisation: "))
                geographicalLocation = l[choice2]     
            elif(choice==4):
                l = list(dict(mi.get_unit()).keys())
                print("Voici les unités disponibles: ")
                for j in range(len(l)):
                    print("{} / pour {}".format(j,l[j].name))
                choice2 = int(input("Veuillez Choisir votre unite: "))
                unit = l[choice2]                                                            
            elif(choice==5):
                i = 5
        
        res=mi.findMeasurments(commodityType,indicatorGroup,geographicalLocation,unit)
        for item in res:
            print(item.describe())

        q = int(input("tapez 1 pour continuer ou 0 pour quitter\n"))








