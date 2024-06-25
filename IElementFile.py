from abc import ABC, abstractmethod

#ABC to skrót od Abstract Base Class, co oznacza klasę bazową abstrakcyjną. 

#pip install sphinx - do tworzenia autmatycznej dokumnetacji 


#IElement - Interface of Element
class IElement(ABC):

    @abstractmethod
    def __init__(self, typeOfElement, faceplateType,  kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondtion):
        pass 
    
    @abstractmethod
    def ReadElementFromJson(self, filename):
        """
        Main Function Of Create Element
        Accepts: fileNameOfJson
        Return: NameVbsFilePathPropsOfElement, NameOfInitializeFuntionOfElement
        """
        pass


    @abstractmethod
    def ValidateJson(self, filename):
        pass
    
    @abstractmethod
    def ReadJsonFile(self, filename):
        pass

    @abstractmethod
    def ReadItemsFromJson(self, data):
        pass

    @abstractmethod
    def ReadDynamicsFromJson(self, data):
        pass

    @abstractmethod
    def ReadTextLibraryFromJson(self, data):
        pass
    

    @abstractmethod
    def ParseOfJson(self):
        """
        Parse Json To extract props of element
        Accepts: inputJsons
        Return: newJsons, elementIds
        """
        pass

    @abstractmethod
    def CompareNewJsonsAndDynamicJsons(self):
        pass

    
    @abstractmethod
    def FindElementPropsTextWithElementID(self):
        pass

    @abstractmethod
    def SaveLocationOfObjectsToTxtFile(self, filename):
        pass

    @abstractmethod
    def IsNumber(self, value):
        pass

    @abstractmethod
    def CreateIntitializeOfElementFunctionContent(self):
        pass

    @abstractmethod
    def SaveIntitializeOfElementFunctionContentToTxtFile(self):
        pass

    

