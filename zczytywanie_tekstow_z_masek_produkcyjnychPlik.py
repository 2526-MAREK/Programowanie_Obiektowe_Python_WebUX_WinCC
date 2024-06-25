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


def zczytywanie_tekstow_z_masek_produkcyjnych(filename):
    validate_json(filename)

    # Wczytywanie pliku JSON
    with open(filename, 'r', encoding='utf-16le') as file:
        data = json.load(file)



    text_jsons = []
    for text in data['textlibrary']:
        text_jsons.append(text)


    input_jsons = []

        # Przeszukiwanie listy items
    for item in data['items']:
        input_jsons.append(item)

    #print(text_jsons)



    results = {}


    def znajdz_po_elementID(lista, id_szukane):
        for element in lista:

            if 'Text' in element['props']:
                czesci= element['props']['Text'].split('.')
                if len(czesci) > 3:
                    elementID = int(czesci[2])
                    if elementID == id_szukane:
                        return element['props']['ObjectName']
        return None



    for element in text_jsons:
        if 'en-US' in element['text'][0]:
            if "R13" in element['text'][0]['en-US']:
                if len(element['text'][0]['en-US']) < 15:
                    #print(element['elementID'])
                    wynikTemp = znajdz_po_elementID(input_jsons, element['elementID'])
                    #print(wynikTemp)
                    #print(element['text'][0]['en-US'])
                    results[wynikTemp] = element['text'][0]['en-US']


    #print(results)

    fileNameTemp = filename.split('.')

    with open(f'initialize_Texts_{fileNameTemp[0]}_WebUX.txt', "w") as file:
        file.write(f'\n\n')

        for key, value in results.items():
            #value.replace(r"\r\n", '" & vbCrLf & "')
            if "Line" in value:
                raw_value = repr(value).strip("'")
                czesci= raw_value.split(' ')



                file.write(f'\tIf HMIRuntime.Language = 1045 Then\n')
                file.write(f'\t\tScreenItems("{key}").Text = "Linia {czesci[1]}"\n')
                file.write(f'\tElseif HMIRuntime.Language = 1033 Then\n')
                file.write(f'\t\tScreenItems("{key}").Text = "{raw_value}"\n')
                file.write(f'\tEnd If\n')
            else:
                raw_value = repr(value).strip("'")


                file.write(f'\tScreenItems("{key}").Text = "{raw_value}"\n')
            
