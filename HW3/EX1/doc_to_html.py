import sys
import importlib

"""
    EX1 of HW3
    Receives input file of a python module and an output file for the desired HTML file 
    from the users commandline and extract the documentation of the module into an HTML
    include minimal file error handling
"""


def generate_html_from_module(module):
    """
    Extracts a module documentations from a module object into a HTML string
    uses a pre-written builtins list in order to exclude built in functions
    :param module: Module object type to extract documentation from
    :return: String representation of an HTML file
    """
    html_content = f"<html><head><title>{module.__name__} Doc</title></head><body><h1>Module {module.__name__}:</h1>"
    html_content += f"Function {module.__doc__}"
    for function in module.__dict__:
        if callable(getattr(module, function)):
            html_content += f"<h2>Function {function}:</h2>"
            html_content += f"{getattr(module, function).__doc__}"
            html_content += f"<h3>Annotations:</h3>"
            for annotation in getattr(module, function).__annotations__.keys():
                html_content += f"{annotation} <br>"
    html_content += "</body></html>"
    return html_content


def doc_to_html():
    """
    Gets the user commandline input and calls the html creaton function
    This method also handles file read write errors
    :return: Creates a HTML file with the desired name and
    """
    try:
        module_file_name = sys.argv[1]
        output_html = sys.argv[2]
    except IndexError or UnboundLocalError:
        print("Error: Please enter two correct arguments at the right order [1. module file, 2. output HTML file]")
        sys.exit(0)
    module = importlib.import_module(module_file_name.replace(".py", ""))
    try:
        with open(output_html, "w") as file:
            file.write(generate_html_from_module(module))
    except Exception as error:
        print(error)


if __name__ == "__main__":
    doc_to_html()