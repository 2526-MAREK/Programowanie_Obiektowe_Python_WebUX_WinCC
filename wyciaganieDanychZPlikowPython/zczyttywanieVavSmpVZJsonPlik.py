import json
import pprint
def validate_json(filename):
    try:
        with open(filename, 'r', encoding='utf-16le') as file:
            data = json.load(file)
        print(f"Plik {filename} jest poprawnym plikiem JSON.")
    except json.JSONDecodeError as e:
        print(f"Błąd w pliku {filename}: {e}")
    except Exception as e:
        print(f"Nieoczekiwany błąd podczas przetwarzania pliku {filename}: {e}")

# Użyj funkcji

def zczyttywanieVavSmpVZJson(filename):
    validate_json(filename)

    # Wczytywanie pliku JSON
    with open(filename, 'r', encoding='utf-16le') as file:
        data = json.load(file)

    new_jsons = []
    input_jsons = []

        # Przeszukiwanie listy items
    for item in data['items']:
        input_jsons.append(item)


    # Przygotowanie listy do przechowywania nowych JSONów i 'ElementID'
    new_jsons = []
    element_ids = []

    # Iteracja po każdym JSON i dodanie wybranych wartości do listy oraz zapisanie 'ElementID' do osobnej listy
    for json1 in input_jsons:
        if 'FaceplateType' not in json1['props']:
            continue
        
        
        FaceplateType = json1['props']['FaceplateType']
        if FaceplateType == "Faceplates\\Devices\\Icons\\ValveSimple_IconV.FPT":
            #print(json1)

            if 'Left'  not in json1['props']:
                leftTemp = '0'
            else:
                leftTemp = json1['props']['Left']
            new_json = {
                'Left': leftTemp,
                'Top': json1['props']['Top'],
                
                
                'SIMPLE_VALVE_Status02': json1['props']['SIMPLE_VALVE_Status02'],
                'SIMPLE_VALVE_StatusAlarm': json1['props']['SIMPLE_VALVE_StatusAlarm'],
                'SIMPLE_VALVE_Status': json1['props']['SIMPLE_VALVE_Status'],
                'SIMPLE_VALVE_Config': json1['props']['SIMPLE_VALVE_Config'],

                'Label': 'temp',
                'Tag': json1['props']['Tag'],
                'ElementID': json1['props']['ElementID']
            }
            new_jsons.append(new_json)
            element_ids.append(json1['props']['ElementID'])

    #print(new_jsons)
    #print(element_ids)

    dynamic_jsons = []
    for dyn in data['dynamics']:
        dynamic_jsons.append(dyn)

    #print(dynamic_jsons)

    for nj in new_jsons:
        element_id = nj['ElementID']
        for dj in dynamic_jsons:
            if dj['elementID'] == element_id and dj['target'] in nj:
                nj[dj['target']] = dj['attributes']['tag']['address']


    #print(new_jsons[0])
    #pprint.pprint(new_jsons[0])
    text_jsons = []
    for text in data['textlibrary']:
        text_jsons.append(text)

    #pprint.pprint(text_jsons)


    def znajdz_po_elementID(lista, id_szukane):
        for element in lista:
            if element['elementID'] == id_szukane:
                return element
        return None


    for i, nj in enumerate(new_jsons):
        czesci = nj['Tag'].split('.')
        elementIDStr = czesci[2]
        elementIDInt = int(elementIDStr)

        wynikTemp = znajdz_po_elementID(text_jsons, elementIDInt+1)
        #print(elementIDEngUnits)
        #print(text_jsons)
        nj['Tag'] = wynikTemp['text'][0]['en-US']
        wynikTemp = znajdz_po_elementID(text_jsons, elementIDInt)
        nj['Label'] = wynikTemp['text'][0]['en-US']

        
        # print(nj['Label'])
        # print(nj['EngUnits'])
    #pprint.pprint(new_jsons)



    #for nj in new_jsons:
        #print(json.dumps(nj, indent=2))

    file_content = ""
    for i, nj in enumerate(new_jsons):
        file_content += f"Obiekt_{i+1} ({nj['Label']}):\n  Left: {nj['Left']}\n  Top: {nj['Top']}\n\n"


    nameOfFileTemp = filename.split('.')
    file_path = f'lokalizacja_obiektów_VavSmpV_{nameOfFileTemp[0]}.txt'
    with open(file_path, 'w') as file:
        file.write(file_content)


    vbs_script_content = ""
    dictionary_array = "\tDim vavSmpVArray(" + str(len(new_jsons)) + ")\n"

    #unique_keys = ["EngUnits", "alHiLoOn", "alHiHiLoLoOn", "alTechOn", "spOn", "Label"]

    def is_number(value):
        try:
            float(value.replace(',', '.'))  # Sprawdzanie, czy wartość może być floatem
            return True
        except ValueError:
            return False


    for i, nj in enumerate(new_jsons):
        # Usunięcie określonych pól
        nj.pop("Left", None)
        nj.pop("Top", None)
        nj.pop("ElementID", None)

        # Tworzenie skryptu VBS dla każdego obiektu
        vbs_script_content += f"\tDim vavSmpVTab_{i}({len(nj)})\n"
        d = 0
        for key, value in nj.items():
            if (isinstance(value, int) or is_number(value)):  # Jeśli wartość jest intem
                vbs_script_content += f"\tvavSmpVTab_{i}({d}) = {value.replace(',', '.')} '{key}\n"
            elif (key != "Label") and (key != "Tag"):  # Jeśli wartość jest stringiem i warunki
                vbs_script_content += f"\tvavSmpVTab_{i}({d}) = SmartTags(\"{value}\") '{key}\n"
            else:
                vbs_script_content += f"\tvavSmpVTab_{i}({d}) = \"{value}\" '{key} \n"
            
            d=d+1


        vbs_script_content += "\n"
        dictionary_array += f"\tvavSmpVArray({i}) = vavSmpVTab_{i}\n"


    vbs_script_content =  vbs_script_content + "\n" + dictionary_array  + "\n" + '\tinitializeValveSimple_IconWebUXW2A vavSmpVArray, "VavSmpV"\n'

    # Zapis do pliku "proporties_of_objects.vbs"
    vbs_file_path = f'proporties_of_objects_VavSmpV_{nameOfFileTemp[0]}.txt'
    if len(new_jsons) > 0:
        with open(vbs_file_path, 'w') as file:
            file.write(f'\nSub initialize_VavSmpV_{nameOfFileTemp[0]}_WebUX(lineName, fullLineName)\n')
            file.write(vbs_script_content)
            file.write(f'\nEnd Sub\n')
    
        return vbs_file_path, f'initialize_VavSmpV_{nameOfFileTemp[0]}_WebUX'
    else:
        return None, None