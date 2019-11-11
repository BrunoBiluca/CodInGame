import sys
import math

n = int(input())

spreadsheet = {}

def evaluation(operation, arg_1, arg_2):
    return {
        "VALUE": arg_1,
        "ADD": arg_1 + arg_2,
        "SUB": arg_1 - arg_2,
        "MULT": arg_1 * arg_2
    }.get(operation)
    

def check(arg):
    if isinstance(arg, int):
        return arg
    
    if arg == "_":
        return 0
    
    if not arg.startswith("$"):
        return int(arg)
        
    if arg not in spreadsheet:
        return arg

    if isinstance(spreadsheet[arg], int):
        return spreadsheet[arg]
    else:
        return arg

for i in range(n):
    operation, arg_1, arg_2 = input().split()

    # print(operation)
    
    arg_1 = check(arg_1)
    arg_2 = check(arg_2)
    
    if isinstance(arg_1, int) and isinstance(arg_2, int):
        value = evaluation(operation, arg_1, arg_2)
    else:
        value = (operation, arg_1, arg_2)
        
    spreadsheet.update({f"${str(i)}": value})
    
    # print(spreadsheet)

    # print(value)
    
for key, value in spreadsheet.items():
    # print(value)
    if isinstance(value, tuple):
        arg_1 = check(value[1])
        arg_2 = check(value[2])
        
        # print(arg_1)
        # print(arg_2)

        if isinstance(arg_1, int) and isinstance(arg_2, int):
            result = evaluation(value[0], arg_1, arg_2)
            spreadsheet[key] = result
            
            print(result)
    else:
        print(value)
