import sys
import os
import shutil


from zczytywanie_tekstow_z_masek_produkcyjnychPlik import zczytywanie_tekstow_z_masek_produkcyjnych
from zczytywanieSkryptowZObiektowPlik import zczytywanieSkryptowZObiektow

from initializeElements import initializeElementsFnc


sciezka_do_folderu = os.path.join(os.path.dirname(__file__))



for plik in os.listdir(sciezka_do_folderu):
    # Sprawdzanie, czy plik ma rozszerzenie .json
    if plik.endswith('.json'):
        print("START FILE")
        print(plik)
        sciezka_pliku = os.path.join(sciezka_do_folderu, plik)

        filePathTabOfPropObj = []
        nameOfFunctionTabOfPropObj = []
        
        
        filePathTabOfPropObj, nameOfFunctionTabOfPropObj = initializeElementsFnc(plik)

        zczytywanieSkryptowZObiektow(plik)
        zczytywanie_tekstow_z_masek_produkcyjnych(plik)

        czesci = plik.split('.')


        folder_path = f'{czesci[0]}' 
        if not os.path.exists(folder_path):
            # If it doesn't exist, create it
            os.makedirs(folder_path)

        folder_path = f'{czesci[0]}/' 
        plik_docelowy = f'{folder_path}initialize_{czesci[0]}_WebUX.txt'

        with open(plik_docelowy, 'w') as outfile:
                    # Iteracja po każdym pliku z listy
                    
            for nazwa_pliku in filePathTabOfPropObj:
                # Otwarcie każdego pliku do odczytu
                with open(nazwa_pliku, 'r') as infile:
                    # Odczytanie zawartości i zapisanie do pliku docelowego
                    outfile.write(infile.read())
                    # Opcjonalnie: dodanie nowej linii między zawartością plików
                    outfile.write('\n')
                
                if os.path.exists(nazwa_pliku):
                    os.remove(nazwa_pliku)



            with open(f'initialize_DynamicVariable_{czesci[0]}_WebUX.txt', 'r') as infile:
                    # Odczytanie zawartości i zapisanie do pliku docelowego
                outfile.write(f'Sub initialize_DynamicVariable_{czesci[0]}_WebUX(lineName, fullLineName)\n\n')
                outfile.write(infile.read())
                    # Opcjonalnie: dodanie nowej linii między zawartością plików
                outfile.write('\n')
                outfile.write(f'End Sub\n\n')




            # Usuwanie pliku
            if os.path.exists(f'initialize_DynamicVariable_{czesci[0]}_WebUX.txt'):
                os.remove(f'initialize_DynamicVariable_{czesci[0]}_WebUX.txt')
                

            #initialize_Texts_{fileNameTemp[0]}_WebUX
            with open(f'initialize_Texts_{czesci[0]}_WebUX.txt', 'r') as infile:
                    # Odczytanie zawartości i zapisanie do pliku docelowego
                outfile.write(f'Sub initialize_Texts_{czesci[0]}_WebUX(lineName, fullLineName)\n\n')
                outfile.write(infile.read())
                    # Opcjonalnie: dodanie nowej linii między zawartością plików
                outfile.write('\n')
                outfile.write(f'End Sub\n\n')


            # Usuwanie pliku
            if os.path.exists(f'initialize_Texts_{czesci[0]}_WebUX.txt'):
                os.remove(f'initialize_Texts_{czesci[0]}_WebUX.txt')


            outfile.write(f'Sub initialize_{czesci[0]}_WebUX(lineName, fullLineName)\n\n')

            for nazwa_funkcji in nameOfFunctionTabOfPropObj:
                outfile.write(f'\t{nazwa_funkcji} lineName, fullLineName\n')
            

            
            


            outfile.write(f'\n\tinitialize_DynamicVariable_{czesci[0]}_WebUX lineName, fullLineName\n')
            outfile.write(f'\n\tinitialize_Texts_{czesci[0]}_WebUX lineName, fullLineName\n')

            outfile.write(f'\nEnd Sub\n')


            for plik_TXT in os.listdir(sciezka_do_folderu):
                if plik_TXT.endswith('.txt'):
                    source_file = os.path.join(sciezka_do_folderu, plik_TXT)
                    target_file = os.path.join(f'{czesci[0]}', plik_TXT)
                    shutil.move(source_file, target_file)




        

