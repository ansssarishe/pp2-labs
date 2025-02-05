import re
file_path = r"C:\Users\Ansar\pepepeton\pp2-labs\lab5\sample3.txt"
with open(file_path, 'r', encoding="utf8") as file:
    data = file.read()


#1
first = re.findall("a.*b", data)
print(first)