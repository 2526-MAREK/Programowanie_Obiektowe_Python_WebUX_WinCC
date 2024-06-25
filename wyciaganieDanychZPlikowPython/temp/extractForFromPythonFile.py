import os
import re

               
def extract_text_props(file_content):
    text_props = {}


    lines = file_content.split('\n')  # Podziel zawartość pliku na linie
    matching_lines = [line for line in lines if 'wynikTemp' in line]  # Znajdź wszystkie linie zawierające 'wynikTemp'

    index = 0
    prop = ""
    # Wyświetl wszystkie dopasowane linie
    for line in matching_lines:
        
        #print(line)
        #print(line[-3:])
        if len(line) >= 3:  # Sprawdź, czy linia ma co najmniej 3 znaki
            if line[-3] == "+":
                #print(line[-2])  # Wyświetl trzeci znak od końca
                index = int(line[-2])
            elif line[-1] == ")":    
                index = 0

            #print(index)

            line_without_whitespace = ''.join(line.split())
            if line_without_whitespace[2] == "[":
                start_index = 4
                end_index = line_without_whitespace.find("']", start_index)
                if start_index != -1 and end_index != -1:
                    # Wyciągnij wartość z pierwszego nawiasu kwadratowego
                    match = line_without_whitespace[start_index:end_index]
                    prop = match

                text_props[prop] = index
                    


        
        
        

    print(text_props)

            
    
    #print(text_props)
    return text_props               
               


def extract_kind_of_device(file_content):
    kind_pattern = re.compile(r'kindOfDevice\s*=\s*"([^"]+)"')
    vbs_pattern = re.compile(r'vbs_file_path\s*=\s*f\'proporties_of_objects_([^_]+)_')

    kind_match = kind_pattern.search(file_content)
    vbs_match = vbs_pattern.search(file_content)
    
    if kind_match:
        return kind_match.group(1)
    elif vbs_match:
        return vbs_match.group(1)
    else:
        return "Unknown"
    
def process_files_in_directory(directory):
    all_props_by_type = {}

    count = 0

    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                file_content = file.read()

               

                text_props = extract_text_props(file_content)
                
                

            count = count + 1
    
    print("count of file with .py end: " + str(count))
    return all_props_by_type

def write_props_to_file(props_by_type, output_filename):
    count = 0
    with open(output_filename, 'w', encoding='utf-8') as file:
        for type_of_element, data in props_by_type.items():
            text_props = data['textProps']
            file.write(f"typeOfElement = \"{type_of_element}\"\n")
            file.write("listOfTextProps = {\n")
            for prop, index in text_props.items():
                file.write(f"    '{prop}': {index},\n")

            file.write("\n\n")

            count = count + 1
    
    print("count kind of extract data from python file: " + str(count))


if __name__ == "__main__":
    sciezka_do_folderu = os.path.join(os.path.dirname(__file__))
    directory = sciezka_do_folderu  # Zmień na ścieżkę do katalogu zawierającego pliki .py
    output_filename = "extracted_props_by_type.txt"
    
    props_by_type = process_files_in_directory(directory)
    write_props_to_file(props_by_type, output_filename)
    
    print(f"Props extracted and saved to {output_filename}")