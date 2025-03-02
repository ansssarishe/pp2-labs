import re
file_path = r"lab5/sample3.txt"
with open(file_path, 'r', encoding="utf8") as file:
    data = file.read()


#1
first = re.findall("a*b", data)
print(first)

#2
first = re.findall("ab{2,3}", data)
print(first)

#3
first = re.findall(r"[a-z]+_", data)
print(first)

#4
first = re.findall(r"[A-Z][a-z]", data)
print(first)

#5
pattern1 = r"a.*b"
matches1 = re.findall(pattern1, data)
print(matches1)

#6
pattern2 = r"[ ,.]"
replaced_data = re.sub(pattern2, ":", data)
print(replaced_data)

#7
def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

snake_str = "this_is_a_snake_case_string"
camel_str = snake_to_camel(snake_str)
print(camel_str)

#8
def split_at_uppercase(s):
    return re.findall(r'[A-Z][^A-Z]*', s)

s = "ThisIsAStringWithUppercaseLetters"
split_str = split_at_uppercase(s)
print(split_str)

#9
def insert_spaces(s):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)

s = "ThisIsAStringWithCapitalLetters"
spaced_str = insert_spaces(s)
print(spaced_str)

#10
def camel_to_snake(camel_str):
    snake_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()
    return snake_str

camel_str = "ThisIsACamelCaseString"
snake_str = camel_to_snake(camel_str)
print(snake_str)