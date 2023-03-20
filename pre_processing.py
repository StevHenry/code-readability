import ast



def NumberOfLoops(code):
    # Parse the code snippet into an abstract syntax tree
    tree = ast.parse(code)

    # Initialize counters for loops 
    num_loops = 0
   

    # Traverse the AST to count loops 
    for node in ast.walk(tree):
        if isinstance(node, ast.For) or isinstance(node, ast.While):
            num_loops += 1
       

    # Return the results as a dictionary
    return {"num_loops": num_loops}

def NumberOfLines(code):
    # Parse the code snippet into an abstract syntax tree
    tree = ast.parse(code)

    # Initialize counters for  lines
    num_lines = 0
   

    # Traverse the AST to count  lines
    for node in ast.walk(tree):
        if isinstance(node, ast.Expr):
            num_lines += 1
       

    # Return the results as a dictionary
    return {"num_lines": num_lines}
