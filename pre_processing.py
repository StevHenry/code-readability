import ast
file =  open("./resources/DatasetDorn/dataset/snippets/python/10.jsnp" , 'r', encoding = "utf-8") 
snippet1 = file.read()

def number_Of_Loops(code):
    
    tree = ast.parse(code)

    # Initialize counters for loops 
    num_loops = 0
   

    # Traverse the AST to count loops 
    for node in ast.walk(tree):
        if isinstance(node, ast.For) or isinstance(node, ast.While):
            num_loops += 1
       

    # Return the results as a dictionary
    return {"num_loops": num_loops}

def number_Of_Lines(code):
    tree = ast.parse(code)

    # Initialize counters for  lines
    num_lines = 0
   

    # Traverse the AST to count  lines
    for node in ast.walk(tree):
        if isinstance(node, ast.Expr):
            num_lines += 1
       

    # Return the results as a dictionary
    return  num_lines

number_Of_Lines(snippet1)
