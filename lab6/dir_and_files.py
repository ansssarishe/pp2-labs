import os
import string

# 1
def list_directories_files(path):
    directories = []
    files = []
    all_items = []

    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            directories.append(item)
        elif os.path.isfile(full_path):
            files.append(item)
        all_items.append(item)

    print("Directories:", directories)
    print("Files:", files)
    print("All items:", all_items)

# 2
def check_access(path):
    print("Existence:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

# 3
def test_path(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Directory portion:", os.path.dirname(path))
        print("Filename portion:", os.path.basename(path))
    else:
        print("404")

# 4
def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        print("Number of lines:", len(lines))

# 5
def write_list_to_file(file_path, lst):
    with open(file_path, 'w') as file:
        for item in lst:
            file.write(f"{item}\n")

# 6
def generate_text_files():
    for letter in string.ascii_uppercase:
        file_name = f"{letter}.txt"
        with open(file_name, 'w') as file:
            file.write(f"This is {file_name}")

# 7
def copy_file_contents(source_path, destination_path):
    with open(source_path, 'r') as source_file:
        contents = source_file.read()
    with open(destination_path, 'w') as destination_file:
        destination_file.write(contents)

# 8.
def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"{path} deleted.")
        else:
            print(f"No access to {path}")
    else:
        print(f"Path {path} 404")