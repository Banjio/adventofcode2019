import numpy as np
import re


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


def get_matrix_one_path(inputs:list):
    x, y = 500, 500
    cur_row, cur_col = int(x/2), int(y/2)
    matrix = np.zeros((x,y))
    for inp in inputs:
        direction, steps = parse_directions(inp)
        matrix, cur_row, cur_col = update_matrix(direction, steps, matrix, cur_row, cur_col)
    return matrix


def calc_manhattan_dist(orig, point):
    return abs(orig[0] - point[0]) + abs(orig[1] - point[1])


def get_results(intersection_matrix, origin):
    intersections = np.where(intersection_matrix == 2)
    distances = list()
    if np.ndim(intersections) == 2:
        return intersections
    else:
        dist = list()
        for intersection in intersections:



test_inp = ["R95", "U150", "L200", "D50"]
test_inp2 = ["L99", "D104", "R200", "U50"]
matrix = get_matrix_one_path(test_inp)
matrix2 = get_matrix_one_path(test_inp2)
intersection_matrix = matrix + matrix2
intersection_matrix[250, 249] += 1
intersection_matrix[250, 250] = 1
get_results(intersection_matrix, (250, 250))
