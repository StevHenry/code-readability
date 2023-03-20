import ast

def getnumberofLoopsandlines(code):
    # Parse the code snippet into an abstract syntax tree
    tree = ast.parse(code)

    # Initialize counters for loops and lines
    num_loops = 0
    num_lines = 0

    # Traverse the AST to count loops and lines
    for node in ast.walk(tree):
        if isinstance(node, ast.For) or isinstance(node, ast.While):
            num_loops += 1
        elif isinstance(node, ast.Expr):
            num_lines += 1

    # Return the results as a dictionary
    return {"num_loops": num_loops, "num_lines": num_lines}
