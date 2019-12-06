import aoc19_max
from aoc19_max.convenience_functions import data_to_list, get_day_from_file, get_input_by_day
from config import DATADIR

class IntcodeCp(object):

    def __init__(self, opcode_list):
        self.opcode_list = opcode_list
        self.start_index_pos = 0


    def op_code_1(self, inputpos1, inputpos2, outputpos):
        self.opcode_list[outputpos] = self.opcode_list[inputpos1] + self.opcode_list[inputpos2]

    def op_code_2(self, inputpos1, inputpos2, outputpos):
        self.opcode_list[outputpos] = self.opcode_list[inputpos1] * self.opcode_list[inputpos2]

    def op_code99(self):
        return "END"

    def execute_op_code(self, opcode, index_opcode):

        inputpos1 = self.opcode_list[index_opcode+1]
        inputpos2 = self.opcode_list[index_opcode+2]
        outputpos = self.opcode_list[index_opcode+3]

        if opcode == 1:
            self.op_code_1(inputpos1, inputpos2, outputpos)
            return True
        elif opcode == 2:
            self.op_code_2(inputpos1, inputpos2, outputpos)
            return True
        elif opcode == 99:
             return False

        else:
            raise TypeError(f"Encountered Unknown opcode {opcode}, aborting Intcode Programm")

    def execute_intcode(self):
        curr_indexpos = self.start_index_pos
        flag = True
        while flag:
            flag = self.execute_op_code(self.opcode_list[curr_indexpos], curr_indexpos)
            curr_indexpos += 4
        return self.opcode_list

    def find_special_output(self, desired_output:int, original_list:list):
        self.opcode_list = original_list.copy()
        for i in range(100):
            for j in range(99, -1, -1):
                self.opcode_list[1] = i
                self.opcode_list[2] = j
                result_list = self.execute_intcode()
                result = result_list[0]
                if result == desired_output:
                    print("DEBUG")
                    return dict(noun=i, verb=j)
                else:
                    self.opcode_list = original_list.copy()



if __name__ == "__main__":
    # ------------- PART 1 ------------------
    day = get_day_from_file(str(__file__))
    input_path = get_input_by_day(day, DATADIR)
    data_as_list = data_to_list(input_path)
    # Additional action to have LIST[int]
    data_as_list = data_as_list[0].split(",")
    data_as_list = [int(x) for x in data_as_list]
    # Changing value from second and third element
    data_as_list[1] = 12
    data_as_list[2] = 2
    # Giving in a copy, because we potentially need the original list for Part 2
    computer = IntcodeCp(data_as_list.copy())
    final_list = computer.execute_intcode()
    print(f"The value from list at position zero is {final_list[0]}")
    #print("The fuel needed for all modules is: ", fuel_sum(data_as_list, fuel_per_module))
    # ------------ PART 2 ------------------
    result_2 = computer.find_special_output(19690720, data_as_list.copy())
    print("The result from brute_forcing is:", result_2)
    print("Thus the result for the task is:", result_2["noun"] * 100 + result_2["verb"])
