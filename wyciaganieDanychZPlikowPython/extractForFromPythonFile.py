import os
import re

def extract_matching_lines(file_path):
    # Prostsze wyrażenie regularne dla debugowania
    pattern = re.compile(r"wynikTemp = znajdz_po\(.*?\)")
    results = []

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        print(f"Checking line {i + 1}: {line.strip()}")
        match = pattern.search(line)
        print(f"Match: {match}")
        if match:
            print(f"Line matched: {line.strip()}")
            argument_match = re.search(r"wynikTemp = znajdz_po\(.*?, (.*?)\)", line)
            if argument_match:
                argument = argument_match.group(1)
                print(f"Captured group: {argument}")
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    results.append((os.path.basename(file_path), argument, next_line))
                    print(f"Next line: {next_line}")
                else:
                    results.append((os.path.basename(file_path), argument, ''))
                    print("Next line: (none)")

    return results

def process_python_files(folder_path):
    output_file = "matched_lines.txt"
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for filename in os.listdir(folder_path):
            if filename.endswith(".py"):
                file_path = os.path.join(folder_path, filename)
                matches = extract_matching_lines(file_path)
                for match in matches:
                    out_file.write(f"Filename: {match[0]}\n")
                    out_file.write(f") {match[1]}   +1)\n")
                    out_file.write(f"{match[0]}  ) '{match[2]}'   +1)\n")
                    out_file.write("\n" + "="*40 + "\n\n")

if __name__ == "__main__":
    folder_path = "."  # Folder z plikami Python (możesz zmienić na odpowiedni folder)
    process_python_files(folder_path)
