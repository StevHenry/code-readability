import ast
import re
file =  open("./resources/DatasetDorn/dataset/snippets/python/10.jsnp" , 'r', encoding = "utf-8") 
snippet1 = file.read()


def reg_number_of_lines(code) : 
    x = re.findall("\n", code)
    return len(x)

def reg_number_of_loops(code) : 
    x = re.findall("for" , code) 
    y = re.findall("while" , code)
    output = x+y
    if len(output) == 0 : 
        return "snippet does not contain loops"
    else :
        return len(output)

def number_of_indentation(code) : 
    lines = code.split('\n')
    indentation_level = 0

    for line in lines:
        match = re.match(r'^\s+', line)
        if match:
            indentation = match.group(0)
            if indentation_level == 0 or len(indentation) > len(previous_indentation):
                indentation_level += 1
            elif len(indentation) < len(previous_indentation):
                indentation_level -= 1
                previous_indentation = indentation
        else:
            previous_indentation = ""

    print(f"Indentation level: {indentation_level} - {line}")


x = reg_number_of_loops(snippet1)
print(x)
number_of_indentation(snippet1)
