#import aoc
from config import DATADIR

from aoc19_max.convenience_functions import data_to_list, get_day_from_file, get_input_by_day


def fuel_per_module(mass:int) -> int:
    """
    fuel per module version 1
    :param mass: mass of module
    :return: fuel required
    """
    return int(mass // 3) - 2

def fuel_per_module_accounting_fuel(mass: int) -> int:
    """
    fuel per module version 2
    :param mass: mass of module
    :return: fuel required
    """
    fuel = 0
    while mass > 0 :
        mass = int(mass // 3) - 2
        if mass < 0:
            mass = 0
        fuel += mass
    return fuel


def fuel_sum(mass_list:list, fuel_calc_fun) -> int:
    """
    calls fuel calculation function for every element in a list
    :param mass_list: list of masses per module
    :return: final mass
    """
    return sum([fuel_calc_fun(mass) for mass in mass_list])



if __name__ == "__main__":
    # Easy way is to download Data and run this
    # ------------- PART 1 ------------------
    day = get_day_from_file(str(__file__))
    input_path = get_input_by_day(day, DATADIR)
    data_as_list = data_to_list(input_path)
    print("The fuel needed for all modules is: ", fuel_sum(data_as_list, fuel_per_module))
    # ------------ PART 2 ------------------
    day = get_day_from_file(str(__file__))
    input_path = get_input_by_day(day, DATADIR)
    data_as_list = data_to_list(input_path)
    print("The fuel needed for all modules is: ", fuel_sum(data_as_list, fuel_per_module_accounting_fuel))
    # Thanks to functions provided by Simon we can use this
    #aoc.
