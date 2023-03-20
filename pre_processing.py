import ast
import re
file =  open("./resources/DatasetDorn/dataset/snippets/python/5.jsnp" , 'r', encoding = "utf-8") 
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


x = reg_number_of_loops(snippet1)
print(x)
