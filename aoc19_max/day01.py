
def fuel_per_module(mass:int):
    """

    :param mass:
    :return:
    """
    return int(mass // 3) - 2

def fuel_sum(mass_list:list):
    """

    :param mass_list:
    :return:
    """
    return sum([fuel_per_module(mass) for mass in mass_list])

def data_to_list(stream):
    data_list = list()
    with open(stream, "r") as s:
        for line in s.readlines():
            data_list.append(int(line))
    return data_list

if __name__ == "__main__":
    input_path = "data/input/input.txt"
    data_as_list = data_to_list(input_path)
    print("The fuel needed for all modules is: ", fuel_sum(data_as_list))
