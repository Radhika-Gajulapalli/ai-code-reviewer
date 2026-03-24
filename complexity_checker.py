import ast

def analyze_code(code):
    tree = ast.parse(code)

    functions = 0
    classes = 0

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions += 1
        elif isinstance(node, ast.ClassDef):
            classes += 1

    lines = len(code.split("\n"))

    return lines, functions, classes