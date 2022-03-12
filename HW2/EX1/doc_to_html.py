import sys
import inspect


def doc_to_html():
    try:
        module_file_name = sys.argv[1]
        output_html = sys.argv[2]
    except IndexError or UnboundLocalError:
        print("Error: Please enter two correct arguments at the right order [1. module file, 2. output HTML file]")
        sys.exit(0)
    print(module_file_name + " " + output_html)


if __name__ == "__main__":
    doc_to_html()
