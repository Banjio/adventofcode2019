import re
import os
import glob
import pathlib
import time

def data_to_list(stream) -> list:
    """
    Converts data from the text file to a list
    :param stream: every type that can be openend with builtin open
    :return: List with one item = one line in stream
    """

    with open(stream, "r") as s:
        content = s.read()
        data_list = content.splitlines()
    return data_list

def get_day_from_file(filename: str) -> str :
    """
    parses the day from a filename/ filepath
    :param filename: filename of the executing file -> __file__
    :return: str of the day with leading zeto
    """
    regex = re.compile("[0-9][0-9]")
    day = regex.findall(os.path.basename(filename))[0]
    return day

def get_input_by_day(day:str, datadir:str) -> pathlib.Path:
    """
    gets the file coresponding to the day -> only if naming conventions are kept
    :param day: str of the day with leading zero
    :param datadir: directory where the files can be found
    :return: Filepath of the file
    """
    assert os.path.isdir(datadir), f"{datadir} is no known directory"
    filename = glob.glob1(datadir, f"*_day_{day}*")[0]
    return pathlib.Path(datadir, filename)

def timer(func):
    """
    Wrapper for a function that a returns a result by
    https://github.com/Dementophobia/advent-of-code-2019/blob/master/aoc.py
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"\nTime required: {(time.time() - start_time)*1000:.2f} ms\n")
        return result
    return wrapper