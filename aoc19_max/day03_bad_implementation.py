import numpy as np
import re

from aoc19_max.convenience_functions import data_to_list, get_day_from_file, get_input_by_day
from config import DATADIR


# TODO: Stimmt noch nicht hanz weil bei
def update_matrix(direction, steps, matrix, cur_row, cur_col):
    assert direction in ["R", "L", "U", "D"]

    if "R" in direction:
        matrix[cur_row, cur_col:cur_col+steps+1] = 1
        new_row = cur_row
        new_col = cur_col + steps

    elif "L" in direction:
        matrix[cur_row, cur_col-steps:cur_col+1] = 1
        new_row = cur_row
        new_col = cur_col - steps

    elif "U" in direction:
        matrix[cur_row-steps:cur_row+1, cur_col] = 1
        new_row = cur_row - steps
        new_col = cur_col

    elif "D" in direction:
        matrix[cur_row:cur_row+steps+1, cur_col] = 1
        new_row = cur_row + steps
        new_col = cur_col

    return matrix, new_row, new_col


def parse_directions(inp: str):
    direction = re.findall(r"R|L|D|U", inp)[0]
    steps = int(re.findall(r'\d+',inp)[0])

    return direction, steps


def get_matrix_one_path(inputs:list, x_dim:int, y_dim:int):
    cur_row, cur_col = int(x_dim/2), int(y_dim/2)
    matrix = np.zeros((x_dim,y_dim))
    for inp in inputs:
        direction, steps = parse_directions(inp)
        matrix, cur_row, cur_col = update_matrix(direction, steps, matrix, cur_row, cur_col)
    return matrix


def calc_manhattan_dist(orig, point):
    return abs(orig[0] - point[0]) + abs(orig[1] - point[1])


# TODO: Verhalten abfangen, wenn es nur eine Überkreuzung gibt
def get_results(intersection_matrix, origin):
    intersections = np.where(intersection_matrix == 2)

    min_dist = origin[0] * origin[1]
    nearest_coordinates = None
    for intersection in intersections:
        dist = calc_manhattan_dist(origin, intersection)
        if dist == 0:
            continue
        elif dist < min_dist:
            nearest_coordinates = intersection

    return nearest_coordinates




if __name__ == "__main__":
    day = get_day_from_file(str(__file__))
    input_path = get_input_by_day(day, DATADIR)
    data_as_list = data_to_list(input_path)
    directions1 = data_as_list[0].split(",")
    directions2 = data_as_list[1].split(",")
    x_orig = 30000
    y_orig = 30000
    matrix1 = get_matrix_one_path(directions1, x_orig, y_orig)
    matrix2 = get_matrix_one_path(directions2, x_orig, y_orig)
    intersection = matrix1 + matrix2
    print(get_results(intersection, (x_orig, y_orig)))

    test_inp = ["R5", "U10", "L12", "D20"]
#test_inp2 = ["L10", "D24", "R10", "U12"]
#matrix = get_matrix_one_path(test_inp)
#matrix2 = get_matrix_one_path(test_inp2)
#intersection_matrix = matrix + matrix2
#intersection_matrix[250, 249] = 2
#intersection_matrix[250, 250] = 1
#intersection_matrix[250, 230] = 2
#get_results(intersection_matrix, (50, 50))
