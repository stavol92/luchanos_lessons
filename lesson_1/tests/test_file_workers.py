from lesson_1.my_funcs.file_workers import read_from_file
import  pytest

def create_test_data():
    test_data = ['one\n', 'two\n', 'three\n']
    with open("tests/test_file.txt", "a") as f_o:
        f_o.writelines(test_data)

def test_read_from_file():
    assert test_data == read_from_file("tests/test_file.txt")

def test_read_from_file2():
    assert test_data == read_from_file("tests/test_file.txt")