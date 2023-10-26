# Here I am showing DavOps Project Day 6

import inspect

def generate_function_documentation(module):
    documentation = []
    functions = inspect.getmembers(module, inspect.isfunction)

    for name, func in functions:
        docstring = func.__doc__
        if docstring:
            documentation.append(f"### Function: {name}\n\n{docstring}\n")

    return '\n'.join(documentation)

if __name__ == '__main__':
    import my_module  # Replace with the name of your module
    documentation = generate_function_documentation(my_module)
    with open('documentation.md', 'w') as doc_file:
        doc_file.write(documentation)
