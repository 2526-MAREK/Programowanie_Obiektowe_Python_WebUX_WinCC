import os
import re

def extract_props_from_new_json(file_content):
    pattern = re.compile(r'new_json\s*=\s*{([^}]*)}')
    matches = pattern.findall(file_content)
    
    props = set()
    for match in matches:
        lines = match.split(',')
        for line in lines:
            prop_match = re.match(r'\s*\'([^\']+)\'\s*:', line)
            if prop_match:
                props.add(prop_match.group(1))
    
    return list(props)


def extract_faceplate_type(file_content):
    faceplate_pattern = re.compile(r'FaceplateType\s*==\s*"([^"]+)"')
    faceplate_match = faceplate_pattern.search(file_content)
    
    if faceplate_match:
        return faceplate_match.group(1)
    else:
        return "Unknown"
    

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

def extract_props_to_delete(file_content):
    delete_pattern = re.compile(r'nj.pop\("([^"]+)", None\)')
    matches = delete_pattern.findall(file_content)
    
    return matches


def extract_string_props_to_condition(file_content):
    condition_pattern = re.compile(r'elif\s*\((.*?)\)\s*:')
    condition_match = condition_pattern.search(file_content)
    
    if condition_match:
        condition = condition_match.group(1)
        props_pattern = re.compile(r'key\s*!=\s*"([^"]+)"')
        props_matches = props_pattern.findall(condition)
        return props_matches
    else:
        return []

# def extract_text_props(file_content):
#     text_prop_pattern = re.compile(r'wynikTemp\s*=\s*znajdz_po_elementID\(text_jsons,\s*elementID\w*\+\s*(\d+)\)\s*nj\[\'([^\']+)\'\]')
#     matches = text_prop_pattern.findall(file_content)
    
#     text_props = {}
#     for match in matches:
#         index, prop = match
#         text_props[prop] = int(index)
    
#     return text_props

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

    
    return text_props


def process_files_in_directory(directory):
    all_props_by_type = {}

    count = 0

    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                file_content = file.read()
                props = extract_props_from_new_json(file_content)
                kind_of_device = extract_kind_of_device(file_content)
                faceplate_type = extract_faceplate_type(file_content)
                props_to_delete = extract_props_to_delete(file_content)
                string_props_to_condition = extract_string_props_to_condition(file_content)
                text_props = extract_text_props(file_content)
                
                if kind_of_device not in all_props_by_type:
                    all_props_by_type[kind_of_device] = {
                        'faceplateType': faceplate_type,
                        'props': set(),
                        'propsToDelete': set(),
                        'stringPropsToCondition': set(),
                        'textProps': {}
                    }
                all_props_by_type[kind_of_device]['props'].update(props)
                all_props_by_type[kind_of_device]['propsToDelete'].update(props_to_delete)
                all_props_by_type[kind_of_device]['stringPropsToCondition'].update(string_props_to_condition)
                all_props_by_type[kind_of_device]['textProps'].update(text_props)

            count = count + 1
    
    print("count of file with .py end: " + str(count))
    return all_props_by_type

def write_props_to_file(props_by_type, output_filename):
    count = 0
    with open(output_filename, 'w', encoding='utf-8') as file:
        for type_of_element, data in props_by_type.items():
            faceplate_type = data['faceplateType']
            props = data['props']
            props_to_delete = data['propsToDelete']
            string_props_to_condition = data['stringPropsToCondition']
            text_props = data['textProps']
            file.write(f"typeOfElement = \"{type_of_element}\"\n")
            file.write(f"kindOfFunctionToInitializeElement = \"W2A\"\n")
            file.write(f"faceplateType = \"{faceplate_type}\"\n")
            file.write("listOfProps = [")
            file.write(", ".join([f"'{prop}'" for prop in props]))
            file.write("]\n")
            file.write("listOfPropsToDelete = [")
            file.write(", ".join([f"'{prop}'" for prop in props_to_delete]))
            file.write("]\n")
            file.write("listOfStringInPropsToCondition = [")
            file.write(", ".join([f"'{prop}'" for prop in string_props_to_condition]))
            file.write("]\n")
            file.write("listOfTextProps = {\n")
            for prop, index in text_props.items():
                file.write(f"    '{prop}': {index},\n")
            file.write("}\n\n")
            file.write(f"processElement(typeOfElement, faceplateType, kindOfFunctionToInitializeElement, listOfProps, listOfTextProps, listOfPropsToDelete, listOfStringInPropsToCondition, fileName, filePathTabOfPropObj, nameOfFunctionTabOfPropObj)\n")
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