import unittest
import os
from io import StringIO
from unittest.mock import patch
import HW3.EX3
from HW3.EX2.last_call import square_num, reset, add_two


def ex1_remove_all_html_files():
    """
    Removes all html files in the ex1 folder for testing
    """
    current_dir = os.path.abspath(os.getcwd())
    ex1_dir = os.path.join(current_dir, 'EX1')
    for file in os.listdir(ex1_dir):
        if ".html" in file:
            os.remove(os.path.join(ex1_dir, file))
    return ex1_dir


def run_ex1(working_directory, python_file_name: str, html_output: str, python_file_to_doc: str):
    os.chdir(working_directory)
    os.system(f"python {os.path.join(working_directory, python_file_name)} {python_file_to_doc} {html_output}")
    os.chdir(working_directory.replace("EX1", ""))


class doc_to_html_test(unittest.TestCase):
    """
    Tests for EX1 - HTML documentation generator from python module
    """

    def test_file_creation_and_naming(self):
        ex1_dir = ex1_remove_all_html_files()
        self.assertTrue(".html" not in [file for file in os.listdir(ex1_dir)])
        run_ex1(ex1_dir, 'doc_to_html.py', 'doc_test.html', 'homeworkmodule.py')
        self.assertTrue("doc_test.html" in [file for file in os.listdir(ex1_dir)])

    def test_html_output_content(self):
        ex1_dir = ex1_remove_all_html_files()
        run_ex1(ex1_dir, 'doc_to_html.py', 'doc_test.html', 'homeworkmodule.py')
        with open(os.path.join(ex1_dir, 'doc_test.html'), "r") as file:
            html_content = file.read()


class last_call_test(unittest.TestCase):
    """
    Tests for EX2 - last call input module
    """

    def test_square_func(self):
        with patch('sys.stdout', new=StringIO()) as test_output:
            square_num(2)
            self.assertEqual(test_output.getvalue(), "")
            square_num(2)
            self.assertTrue("4" in test_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as test_output:
            square_num(3)
            self.assertEqual(test_output.getvalue(), "")
            square_num(3)
            self.assertTrue("9" in test_output.getvalue())

    def test_function_switch(self):
        with patch('sys.stdout', new=StringIO()) as test_output:
            square_num(2)
            self.assertEqual(test_output.getvalue(), "")
            add_two(5)
            self.assertEqual(test_output.getvalue(), "")
            add_two(5)
            self.assertTrue("7" in test_output.getvalue())



if __name__ == "__main__":
    unittest.main()
    doc_to_html_test()
