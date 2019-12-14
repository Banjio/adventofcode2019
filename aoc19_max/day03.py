import re
from typing import List, Tuple
from aoc19_max.convenience_functions import data_to_list, get_day_from_file, get_input_by_day, timer
from config import DATADIR


def calc_manhattan_dist(orig: Tuple[int], point: Tuple[int]):
    return abs(orig[0] - point[0]) + abs(orig[1] - point[1])


def parse_directions(inp: str):
    direction = re.findall(r"R|L|D|U", inp)[0]
    steps = int(re.findall(r'\d+',inp)[0])

    return direction, steps


def get_positions(wire:List[str]):
    x, y = 0, 0
    positions = set()

    for elem in wire:
        direction, step = parse_directions(elem)
        for i in range(int(step)):
            if direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            elif direction == "U":
                y -= 1
            elif direction == "D":
                y += 1
            positions.add((x, y))

    return positions

def get_min_dist(intersections: set, orig: tuple):
    min_dist = 10e10
    for elem in intersections:
        temp_dist = calc_manhattan_dist(orig, elem)
        if temp_dist >= min_dist:
            continue
        else:
            min_dist = temp_dist
    return min_dist

@timer
def get_results():
    day = get_day_from_file(str(__file__))
    input_path = get_input_by_day(day, DATADIR)
    data_as_list = data_to_list(input_path)
    directions1 = data_as_list[0].split(",")
    directions2 = data_as_list[1].split(",")
    path1 = get_positions(directions1)
    path2 = get_positions(directions2)
    intersections = path1.intersection(path2)
    result = get_min_dist(intersections, (0, 0))
    return result

if __name__ == "__main__":
    print(f"The closest point to the central port has a distance of: ", get_results())