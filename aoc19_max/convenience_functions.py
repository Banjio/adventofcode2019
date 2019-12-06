import re
import os
import glob
import pathlib

def data_to_list(stream) -> list:
    """
    Converts data from the text file to a list
    :param stream: every type that can be openend with builtin open
    :return: List with one item = one line in stream
    """
    data_list = list()
    with open(stream, "r") as s:
        for line in s.readlines():
            data_list.append(int(line))
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
    filename = glob.glob1(datadir, f"*_day_{day}*")[0]
    return pathlib.Path(datadir, filename)