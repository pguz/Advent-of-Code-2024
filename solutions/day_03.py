import re


def parse_file(fd):
    return fd.read(),
  
    
def task_1(memory):
    re_pattern = re.compile(r"mul\((\d+),(\d+)\)")
    return sum(int(digit1_gr) * int(digit2_gr) for digit1_gr, digit2_gr in re.findall(re_pattern, memory))


def task_2(memory):
    re_pattern = re.compile(r"(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))")
    result = 0
    op_enabled = True
    for _, digit1_gr, digit2_gr, enable_gr, disable_gr in re.findall(re_pattern, memory):
        if enable_gr:
            op_enabled = True
        elif disable_gr:
            op_enabled = False
        elif digit1_gr and digit2_gr and op_enabled is True:
            result += int(digit1_gr) * int(digit2_gr)
    return result


solution_function_01 = task_1
solution_function_02 = task_2
