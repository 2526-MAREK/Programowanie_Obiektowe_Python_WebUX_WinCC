import json
import base64
import re
import pprint
# Odczytanie pliku JSON
def zczytywanieSkryptowZObiektow(fileName):
    with open(fileName, "r", encoding='utf-16le') as file:
        data = json.load(file)

    # Funkcja do dekodowania Base64
    def decode_base64(data):
        try:
            decoded_bytes = base64.b64decode(data)
            #print(decoded_bytes)
            return decoded_bytes.decode('utf-16le')
        except Exception as e:
            print(f"Wystąpił błąd podczas dekodowania: {e}")
            return None

    # Funkcja zamieniająca wyrażenie
    def replace_expression(expression):
        tags = []
        for i, part in enumerate(expression.split("OR"), 1):
            tags.append(f"tag{i}")
        return " OR ".join(tags)

    # Słownik do przechowywania wyników
    results = {}

    startTempFlag = True 
    # Przeszukiwanie "scriptmodules"
    for script in data["scriptmodules"]:
        for script2 in script["scripts"]:
            element_id = script2.get("elementID")
            name = script2.get("name")


            czesci = name.split('_', 1)

            #print(name)
            if 'OnClick' in czesci:
                continue


            if not element_id:
                print("Brak 'elementID' w skrypcie:", script2)
                continue  # Jeśli nie ma "elementID", omijamy ten skrypt
            code = script2.get("code")
            if not code:
                continue

            # Dekodowanie kodu
            decoded_code = decode_base64(code)
            #print(decoded_code)
            #print("\n \n \n")
            #print(decoded_code)
            if not decoded_code:
                print("Nie udało się zdekodować kodu:", code)
                continue
            


            decoded_code_copy =  decoded_code  

            bitIndex = False
            expressionBool = False
            setTag = False
            expression = ""
            if "bitIndex" not in decoded_code:
                bitIndex = False
                if "expression" not in decoded_code:
                    expressionBool = False
                    #print(decoded_code)
                    if 'Set tag1' in decoded_code:
                        start_idx_3 = decoded_code.index('Set tag1 = ')  + 11
                        end_idx_3 = decoded_code.index('\n', start_idx_3)
                        for klucz, wartosc in results.items():
                            # Sprawdzanie, czy wartość zawiera szukaną frazę
                            if decoded_code[start_idx_3:end_idx_3].replace("HMIRuntime.Tags", "SmartTags") in wartosc:
                                #print(decoded_code[start_idx_3:end_idx_3])
                                expression = decoded_code[start_idx_3:end_idx_3] + " '" + czesci[1] + " WARNING IT CAN BE NEGATION YOU MUST CHECK THIS <----------------------------------------------------------------------------"
                                expression = expression.replace("HMIRuntime.Tags", "SmartTags")
                            else:
                                #print(decoded_code[start_idx_3:end_idx_3])
                                expression = decoded_code[start_idx_3:end_idx_3] + " '" + czesci[1]
                                expression = expression.replace("HMIRuntime.Tags", "SmartTags")


                        if expression == "":
                            expression = decoded_code[start_idx_3:end_idx_3] + " '" + czesci[1]
                            expression = expression.replace("HMIRuntime.Tags", "SmartTags")

                        setTag = True
                    else:
                        continue
                    
                else:
                    if not setTag:
                        expressionBool = True
            else:
                if not setTag:
                    bitIndex = True   




            # print(bitIndex)
            # print(expression) 
            # print(setTag)
            # print(element_id)
            #print(decoded_code)      
            #print(decoded_code_copy.split('\n')[5])

        
            # Sprawdzanie, czy "expression" jest w zd  ekodowanym kodzie



            # Wyciąganie i zamiana wyrażenia
            # if not expression:
            #     start_idx_3 = decoded_code.index('Set tag1 = ') 
            #     end_idx_3 = decoded_code.index('\n', start_idx_3)
            #     expression = decoded_code[start_idx_3:end_idx_3] + " '" + czesci[1]


            if expressionBool:
                start_idx = decoded_code.index('expression = ') + 13
                end_idx = decoded_code.index('\n', start_idx)
                expression = decoded_code[start_idx:end_idx] + " '" + czesci[1]

                expression = expression.replace("group", "SmartTags")
                expression = expression.replace(".value", "")

            

            if bitIndex:
                #print("HALO1")
                start_idx_2 = decoded_code.index('Set tag1 = ') + 11
                end_idx_2 = decoded_code.index('\n', start_idx_2) 

                start_idx = decoded_code.index('bitIndex = ') + 11
                end_idx = decoded_code.index('\n', start_idx) 

                if startTempFlag:
                    expression = decoded_code[start_idx_2:end_idx_2]  + " '" + czesci[1] + "_bit_" + decoded_code[start_idx:end_idx] 
                    expression = expression.replace("HMIRuntime.Tags", "SmartTags")
                    startTempFlag = False



                for klucz, wartosc in results.items():
                    #print("HALO2")
                    # Sprawdzanie, czy wartość zawiera szukaną frazę
                    if decoded_code[start_idx_2:end_idx_2].replace("HMIRuntime.Tags", "SmartTags") in wartosc:
                        expression = decoded_code[start_idx_2:end_idx_2]  + " '" + czesci[1] + " WARNING IT CAN BE NEGATION YOU MUST CHECK THIS <----------------------------------------------------------------------------"  + "_bit_" + decoded_code[start_idx:end_idx]
                        expression = expression.replace("HMIRuntime.Tags", "SmartTags")
                        #print("HALO3")
                    else:
                        expression = decoded_code[start_idx_2:end_idx_2]  + " '" + czesci[1] + "_bit_" + decoded_code[start_idx:end_idx] 
                        expression = expression.replace("HMIRuntime.Tags", "SmartTags")
                        #print("HALO4")


                
                
            #print(start_idx)
            #print(end_idx)
            #new_expression = replace_expression(expression)


            #print(data["dynamics"])
            # Wyszukiwanie "elementID" w "dynamics" -> "script"
            for dynamic in data["dynamics"]:
                if "script" in dynamic["attributes"]:
                    script = dynamic["attributes"]["script"]
                
                    if script["element"] == element_id:
                        target_element_id = dynamic["elementID"]
                        
                        # Wyszukiwanie "elementID" w "items"
                        for item in data["items"]:
                            if item["props"]["ElementID"] == target_element_id:
                                object_name = item["props"]["ObjectName"]
                                results[object_name] = expression



    print("Zakończono przetwarzanie!")
    #print(results)
    #pprint.pprint(results)
    # for element in results:
    #     print(element)

    countOfTabDisplayWithBit = 0
    countOfTabLineColorWithBit = 0
    countOfBackgroundColorWithBit = 0

    countOfTabDisplayWithBool = 0
    countOfTabLineColorWithBool = 0
    countOfBackgroundColorWithBool = 0


    fileNameTemp = fileName.split('.')
    #print(results)
    with open(f'initialize_DynamicVariable_{fileNameTemp[0]}_WebUX.txt', "w") as file:
        file.write(f'\n\n')

        file.write(f'\tDim colorOnMainElement , colorOffMainElement\n')
        file.write(f'\tcolorOnMainElement = RGB(255 ,255,255)\n')
        file.write(f'\tcolorOffMainElement = RGB(152 ,150,152) \n')
        file.write(f'\n\n')

        file.write(f'\tDim colorOnLine , colorOffLine\n')
        file.write(f'\tcolorOnLine = RGB(255 ,255,255)\n')
        file.write(f'\tcolorOffLine = RGB(0 ,0,0)  \n')

        file.write(f'\n\n')
        for keyTemp, valueTemp in results.items():
            czesci = valueTemp.split("'")

            leftString = czesci[0]
            # Wybieranie części stringa po pierwszym wystąpieniem "'" (jeśli istnieje)
            rightString = czesci[1] if len(czesci) > 1 else ""
            # file.write(f'"leftString" = {leftString}\n')
            # file.write(f'"rightString" = {rightString}\n')

            
            if '_bit_' in rightString:
                czesci_2 = rightString.split('_')
                bitTemp = ""
                if len(czesci_2) > 2:
                    # Połączenie wszystkich części po drugim '_'
                    bitTemp = int('_'.join(czesci_2[2:]))
                    print(bitTemp)
                else:
                    bitTemp = ""


                if 'Visible' in rightString:
                    file.write(f"\t'{rightString}")
                    file.write(f'\ttabDisplayWithBit_Bit({countOfTabDisplayWithBit}) = {bitTemp}\n')
                    file.write(f'\ttabDisplayWithBit_Variable({countOfTabDisplayWithBit}) = {leftString}\n')
                    file.write(f'\ttabDisplayWithBit_Obj({countOfTabDisplayWithBit}) = "{keyTemp}"\n\n')
                    countOfTabDisplayWithBit = countOfTabDisplayWithBit + 1
                    
                
                if 'BorderColor' in rightString:
                    file.write(f"\t'{rightString}")
                    file.write(f'\ttabLineColorWithBit_Bit({countOfTabLineColorWithBit}) = {bitTemp}\n')
                    file.write(f'\ttabLineColorWithBit_Variable({countOfTabLineColorWithBit}) = {leftString}\n')
                    file.write(f'\ttabLineColorWithBit_Obj({countOfTabLineColorWithBit}) = "{keyTemp}"\n\n')
                    countOfTabLineColorWithBit = countOfTabLineColorWithBit + 1
                
                if 'BackColor' in rightString:
                    file.write(f"\t'{rightString}")
                    file.write(f'\ttabBackgroundColorWithBit_Bit({countOfBackgroundColorWithBit}) = {bitTemp}\n')
                    file.write(f'\ttabBackgroundColorWithBit_Variable({countOfBackgroundColorWithBit}) = {leftString}\n')
                    file.write(f'\ttabBackgroundColorWithBit_Obj({countOfBackgroundColorWithBit}) = "{keyTemp}"\n\n')
                    countOfBackgroundColorWithBit =  countOfBackgroundColorWithBit + 1

            else:
                if 'Visible' in rightString:
                    file.write(f"\t'{rightString}\n")
                    file.write(f'\ttabDisplayWithBool_Variable({countOfTabDisplayWithBool}) = {leftString}\n')
                    file.write(f'\ttabDisplayWithBool_Obj({countOfTabDisplayWithBool}) = "{keyTemp}"\n\n')
                    countOfTabDisplayWithBool = countOfTabDisplayWithBool + 1
                    
                
                if 'BorderColor' in rightString:
                    file.write(f"\t'{rightString}\n")
                    file.write(f'\ttabLineColorWithBool_Variable({countOfTabLineColorWithBool}) = {leftString}\n')
                    file.write(f'\ttabLineColorWithBool_Obj({countOfTabLineColorWithBool}) = "{keyTemp}"\n\n')
                    countOfTabLineColorWithBool = countOfTabLineColorWithBool + 1
                
                if 'BackColor' in rightString:
                    file.write(f"\t'{rightString}\n")
                    file.write(f'\ttabBackgroundColorWithBool_Variable({countOfBackgroundColorWithBool}) = {leftString}\n')
                    file.write(f'\ttabBackgroundColorWithBool_Obj({countOfBackgroundColorWithBool}) = "{keyTemp}"\n\n')
                    countOfBackgroundColorWithBool = countOfBackgroundColorWithBool + 1


    zawartosc = ""
    with open(f'initialize_DynamicVariable_{fileNameTemp[0]}_WebUX.txt', "r") as file:
        zawartosc = file.read()


    with open(f'initialize_DynamicVariable_{fileNameTemp[0]}_WebUX.txt', "w") as file:
        if countOfTabDisplayWithBit > 0: 
            file.write(f'\tDim  tabDisplayWithBit_Bit({countOfTabDisplayWithBit})\n')
            file.write(f'\tDim tabDisplayWithBit_Variable({countOfTabDisplayWithBit})\n')
            file.write(f'\tDim tabDisplayWithBit_Obj({countOfTabDisplayWithBit})\n\n')

        if countOfTabLineColorWithBit > 0: 

            file.write(f'\tDim tabLineColorWithBit_Bit({countOfTabLineColorWithBit})\n')
            file.write(f'\tDim tabLineColorWithBit_Variable({countOfTabLineColorWithBit})\n')
            file.write(f'\tDim tabLineColorWithBit_Obj({countOfTabLineColorWithBit})\n\n')

        if countOfBackgroundColorWithBit > 0: 

            file.write(f'\tDim tabBackgroundColorWithBit_Bit({countOfBackgroundColorWithBit})\n')
            file.write(f'\tDim tabBackgroundColorWithBit_Variable({countOfBackgroundColorWithBit})\n')
            file.write(f'\tDim tabBackgroundColorWithBit_Obj({countOfBackgroundColorWithBit})\n\n')


        if countOfTabDisplayWithBool > 0: 

            file.write(f'\tDim tabDisplayWithBool_Variable({countOfTabDisplayWithBool})\n')
            file.write(f'\tDim tabDisplayWithBool_Obj({countOfTabDisplayWithBool})\n\n')

        if countOfTabLineColorWithBool > 0: 

            file.write(f'\tDim tabLineColorWithBool_Variable({countOfTabLineColorWithBool})\n')
            file.write(f'\tDim tabLineColorWithBool_Obj({countOfTabLineColorWithBool})\n\n')

        if countOfBackgroundColorWithBool > 0: 

            file.write(f'\tDim tabBackgroundColorWithBool_Variable({countOfBackgroundColorWithBool})\n')
            file.write(f'\tDim tabBackgroundColorWithBool_Obj({countOfBackgroundColorWithBool})\n\n')





        file.write(zawartosc)
        file.write(f'\tDim i\n')

        if countOfTabDisplayWithBit > 0:
            file.write(f'\tFor i = 0 To {countOfTabDisplayWithBit-1}\n')
            file.write(f'\t\tOn Error Resume Next\n')
            file.write(f'\n\n') 
            file.write(f'\t\tdisplayWithBit  tabDisplayWithBit_Bit(i),  tabDisplayWithBit_Variable(i) , tabDisplayWithBit_Obj(i) \n')
            file.write(f'\n\n')            
            file.write(f'\t\tIf Err.Number <> 0 Then\n')
            file.write(f'\t\t\tHMIRuntime.Trace("Błąd podczas wywoływania funkcji displayWithBit dla:" & tabDisplayWithBit_Obj(i) &  " i = "& i & " Numer błędu: " & Err.Number  & vbCrLf)\n')
            file.write(f'\t\tErr.Clear  \n')
            file.write(f'\t\tEnd If \n')
            file.write(f'\t\tOn Error Goto 0 \n')
            file.write(f'\tNext \n\n')
        
        if countOfTabLineColorWithBit > 0:
            file.write(f'\tFor i = 0 To {countOfTabLineColorWithBit-1}\n')
            file.write(f'\t\tOn Error Resume Next\n')
            file.write(f'\n\n') 
            file.write(f'\t\tlineColorWithBit tabLineColorWithBit_Bit(i),  tabLineColorWithBit_Variable(i) , tabLineColorWithBit_Obj(i) , colorOnLine, colorOffLine \n')
            file.write(f'\n\n')            
            file.write(f'\t\tIf Err.Number <> 0 Then\n')
            file.write(f'\t\t\tHMIRuntime.Trace("Błąd podczas wywoływania funkcji lineColorWithBit dla:" & tabLineColorWithBit_Obj(i) & " i = "& i & " Numer błędu: " & Err.Number  & vbCrLf)\n')
            file.write(f'\t\tErr.Clear  \n')
            file.write(f'\t\tEnd If \n')
            file.write(f'\t\tOn Error Goto 0 \n')
            file.write(f'\tNext \n\n')
        
        if countOfBackgroundColorWithBit  > 0:
            file.write(f'\tFor i = 0 To {countOfBackgroundColorWithBit-1 }\n')
            file.write(f'\t\tOn Error Resume Next\n')
            file.write(f'\n\n') 
            file.write(f'\t\tbackgroundColorWithBit tabBackgroundColorWithBit_Bit(i),  tabBackgroundColorWithBit_Variable(i) , tabBackgroundColorWithBit_Obj(i) , colorOnMainElement, colorOffMainElement \n')
            file.write(f'\n\n')            
            file.write(f'\t\tIf Err.Number <> 0 Then\n')
            file.write(f'\t\t\tHMIRuntime.Trace("Błąd podczas wywoływania funkcji backgroundColorWithBit dla:" & tabBackgroundColorWithBit_Obj(i) & " i = "& i & " Numer błędu: " & Err.Number  & vbCrLf)\n')
            file.write(f'\t\tErr.Clear  \n')
            file.write(f'\t\tEnd If \n')
            file.write(f'\t\tOn Error Goto 0 \n')
            file.write(f'\tNext \n\n')



        if countOfTabDisplayWithBool > 0:
            file.write(f'\tFor i = 0 To {countOfTabDisplayWithBool-1}\n')
            file.write(f'\t\tOn Error Resume Next\n')
            file.write(f'\n\n') 
            file.write(f'\t\tdisplayWithBool  tabDisplayWithBool_Variable(i) , tabDisplayWithBool_Obj(i) \n')
            file.write(f'\n\n')            
            file.write(f'\t\tIf Err.Number <> 0 Then\n')
            file.write(f'\t\t\tHMIRuntime.Trace("Błąd podczas wywoływania funkcji  displayWithBool dla:" & tabDisplayWithBool_Obj(i) & " i = "& i &" Numer błędu: " & Err.Number  & vbCrLf)\n')
            file.write(f'\t\tErr.Clear  \n')
            file.write(f'\t\tEnd If \n')
            file.write(f'\t\tOn Error Goto 0 \n')
            file.write(f'\tNext \n\n')
        
        if countOfTabLineColorWithBool > 0:
            file.write(f'\tFor i = 0 To {countOfTabLineColorWithBool-1}\n')
            file.write(f'\t\tOn Error Resume Next\n')
            file.write(f'\n\n') 
            file.write(f'\t\tlineColorWithBool  tabLineColorWithBool_Variable(i) , tabLineColorWithBool_Obj(i), colorOnLine, colorOffLine \n')
            file.write(f'\n\n')            
            file.write(f'\t\tIf Err.Number <> 0 Then\n')
            file.write(f'\t\t\tHMIRuntime.Trace("Błąd podczas wywoływania funkcji lineColorWithBool dla:" & tabLineColorWithBool_Obj(i) & " i = "& i &" Numer błędu: " & Err.Number  & vbCrLf)\n')
            file.write(f'\t\tErr.Clear  \n')
            file.write(f'\t\tEnd If \n')
            file.write(f'\t\tOn Error Goto 0 \n')
            file.write(f'\tNext \n\n')
        
        if countOfBackgroundColorWithBool  > 0:
            file.write(f'\tFor i = 0 To {countOfBackgroundColorWithBool-1 }\n')
            file.write(f'\t\tOn Error Resume Next\n')
            file.write(f'\n\n') 
            file.write(f'\t\tbackgroundColorWithBool  tabBackgroundColorWithBool_Variable(i) , tabBackgroundColorWithBool_Obj(i) , colorOnMainElement, colorOffMainElement \n')
            file.write(f'\n\n')            
            file.write(f'\t\tIf Err.Number <> 0 Then\n')
            file.write(f'\t\t\tHMIRuntime.Trace("Błąd podczas wywoływania funkcji  backgroundColorWithBool dla:" & tabBackgroundColorWithBool_Obj(i) & " i = "& i & " Numer błędu: " & Err.Number  & vbCrLf)\n')
            file.write(f'\t\tErr.Clear  \n')
            file.write(f'\t\tEnd If \n')
            file.write(f'\t\tOn Error Goto 0 \n')
            file.write(f'\tNext \n\n')