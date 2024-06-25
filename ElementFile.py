from IElementFile import IElement 
import json


class Element(IElement):

    #typeOfElement  = "AngInpt"
    #kindOfFunctionToInitializeElement = "W2A"
    #faceplateType = "Faceplates\\Devices\\Icons\\AI_Icon.FPT"
    #listOfProps = ['Left', 'Top', 'Right', 'Down']
    #listOfPropsToDelete = ['Left', 'Top', 'ElementID']
    #listOfStringInPropsToCondtion = ["EngUnits", "alTechOn", "Label", "Tag"]

    # listOfTextProps = {
    #         'EngUnits': 0,     #'Props': idFirst,
    #         'Label': 1,
    #         'Tag': 2
    #     }




    def __init__(self, typeOfElement,faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondtion):
        self._typeOfElement = typeOfElement
        self._faceplateType = faceplateType
        self._kindOfFunctionToInitializeElement = kindOfFunctionToInitializeElement
        self._listOfProps = listOfProps
        self._listOfTextProps = listOfTextProps
        self._listOfPropsToDelete = listOfPropsToDelete
        self._listOfStringInPropsToCondtion = listOfStringInPropsToCondtion

        self.inputJsons = []
        self.dynamicJsons = []
        self.textJsons = []
        self.newJson = []
        self.elementIds = []

        self.vbs_script_content = ""
        self.vbs_file_path = ""
        self.nameOfFileSplit = ""



    

    def ReadElementFromJson(self, filename):
        self.ValidateJson(filename)

        data = self.ReadJsonFile(filename)

        self.ReadItemsFromJson(data)
        self.ReadDynamicsFromJson(data)
        self.ReadTextLibraryFromJson(data)

        self.ParseOfJson()

        self.CompareNewJsonsAndDynamicJsons()

        self.FindElementPropsTextWithElementID()

        self.SaveLocationOfObjectsToTxtFile(filename)

        self.CreateIntitializeOfElementFunctionContent()

        return self.SaveIntitializeOfElementFunctionContentToTxtFile()


    
    def ValidateJson(self, filename):
        try:
            with open(filename, 'r', encoding='utf-16le') as file:
                data = json.load(file)
            print(f"Plik {filename} jest poprawnym plikiem JSON.")
        except json.JSONDecodeError as e:
            print(f"Błąd w pliku {filename}: {e}")
        except Exception as e:
            print(f"Nieoczekiwany błąd podczas przetwarzania pliku {filename}: {e}")

    
    
    def ReadJsonFile(self, filename):
        with open(filename, 'r', encoding='utf-16le') as file:
            data = json.load(file)
            return data


   
    def ReadItemsFromJson(self, data):
        for item in data['items']:
            self.inputJsons.append(item)

    
    def ReadDynamicsFromJson(self, data):
        for dyn in data['dynamics']:
            self.dynamicJsons.append(dyn)

    
    def ReadTextLibraryFromJson(self, data):
        for text in data['textlibrary']:
            self.textJsons.append(text)
    

    
    def ParseOfJson(self):
        for json1 in self.inputJsons:

            if 'FaceplateType' not in json1['props']:
                continue
            
            
            FaceplateType = json1['props']['FaceplateType']
            if FaceplateType == self._faceplateType:
                
                new_json = {}

                for prop in self._listOfProps:
                    if prop not in json1['props']:
                        new_json[prop] = '0'
                    else:
                        new_json[prop] = json1['props'][prop]


                self.newJson.append(new_json)
                self.elementIds.append(json1['props']['ElementID'])
        

    
    def CompareNewJsonsAndDynamicJsons(self):
        for nj in self.newJson:
            element_id = nj['ElementID']
            for dj in self.dynamicJsons:
                if dj['elementID'] == element_id and dj['target'] in nj:
                    if 'tag' in dj['attributes']:
                        nj[dj['target']] = dj['attributes']['tag']['address']

    def FindElementWithID(self, elementID):
        for element in self.textJsons:
            if element['elementID'] == elementID:
                return element
        return None
    
    def FindElementPropsTextWithElementID(self):
        if len(self._listOfTextProps) >= 1:
            first_key = list(self._listOfTextProps.keys())[0]
            
            for i, nj in enumerate(self.newJson):
                czesci = nj[first_key].split('.')

                if len(czesci) >= 2:
                    elementIDStr = czesci[2]
                    elementIDEngUnits = int(elementIDStr)

                    for key, offset in self._listOfTextProps.items():
                        wynikTemp = self.FindElementWithID(elementIDEngUnits + offset)
                        if wynikTemp is not None and 'text' in wynikTemp and wynikTemp['text']:
                            nj[key] = wynikTemp['text'][0]['en-US']

    
    def SaveLocationOfObjectsToTxtFile(self, filename):
        file_content = ""
        for i, nj in enumerate(self.newJson):
            #if 'Label' in nj:
            file_content += f"Obiekt_{i+1} ({nj['Label']}):\n  Left: {nj['Left']}\n  Top: {nj['Top']}\n\n"


        self.nameOfFileSplit = filename.split('.')
        file_path = f'lokalizacja_obiektów_{self._typeOfElement}_{self.nameOfFileSplit[0]}.txt'
        with open(file_path, 'w') as file:
            file.write(file_content)

    @staticmethod
    def IsNumber(value):
        try:
            float(value.replace(',', '.'))  # Sprawdzanie, czy wartość może być floatem
            return True
        except ValueError:
            return False

    
    def CreateIntitializeOfElementFunctionContent(self):
        dictionary_array = "\tDim " + self._typeOfElement + "Array(" + str(len(self.newJson)) + ")\n"

        for i, nj in enumerate(self.newJson):
            
            for prop in self._listOfPropsToDelete:
                nj.pop(prop, None)


            self.vbs_script_content += f"\tDim {self._typeOfElement}Tab_{i}({len(nj)})\n"
            d = 0
            for key, value in nj.items():
                if (isinstance(value, int) or self.IsNumber(value)):  
                    self.vbs_script_content += f"\t{self._typeOfElement}Tab_{i}({d}) = {value.replace(',', '.')} '{key}\n"
                elif key not in self._listOfStringInPropsToCondtion:  
                    self.vbs_script_content += f"\t{self._typeOfElement}Tab_{i}({d}) = SmartTags(\"{value}\") '{key}\n"
                else:
                    self.vbs_script_content += f"\t{self._typeOfElement}Tab_{i}({d}) = \"{value}\" '{key} \n"
                
                d=d+1


            self.vbs_script_content += "\n"
            dictionary_array += f"\t{self._typeOfElement}Array({i}) = {self._typeOfElement}Tab_{i}\n"


        self.vbs_script_content =  self.vbs_script_content + "\n" + dictionary_array + "\n" + '\tinitialize' + self._typeOfElement + '_IconWebUX'+ self._kindOfFunctionToInitializeElement +' ' + self._typeOfElement + 'Array\n'

        
        # Zapis do pliku "proporties_of_objects.vbs"
        self.vbs_file_path = f'proporties_of_objects_{self._typeOfElement}_{self.nameOfFileSplit[0]}.txt'




    
    def SaveIntitializeOfElementFunctionContentToTxtFile(self):
        if len(self.newJson) > 0:
            with open(self.vbs_file_path, 'w') as file:
                file.write(f'\nSub initialize_{self._typeOfElement}_{self.nameOfFileSplit[0]}_WebUX(lineName, fullLineName)\n')
                file.write(self.vbs_script_content)
                file.write(f'\nEnd Sub\n')
        
            return self.vbs_file_path, f'initialize_{self._typeOfElement}_{self.nameOfFileSplit[0]}_WebUX'
        else:
            return None, None

    
