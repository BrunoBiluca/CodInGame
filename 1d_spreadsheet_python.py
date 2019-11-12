import sys
import math

n = int(input())

spreadsheet = {}

def execute_operation(operation, arg_1, arg_2):
    try:
        return {
            "VALUE": arg_1,
            "ADD": arg_1 + arg_2,
            "SUB": arg_1 - arg_2,
            "MULT": arg_1 * arg_2
        }.get(operation)
    except TypeError:
        print("error", operation, arg_1, arg_2)

def check_argument(arg):
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
        
        
def calculate_operation(key, value):
    if not isinstance(value, tuple):
        return value

    arg_1 = check_argument(value[1])
    if isinstance(arg_1, str) and arg_1.startswith("$"):
        arg_1 = calculate_operation(arg_1, spreadsheet[arg_1])
    
    arg_2 = check_argument(value[2])
    if isinstance(arg_2, str) and arg_2.startswith("$"):
        arg_2 = calculate_operation(arg_2, spreadsheet[arg_2])
    
    # Garanto que aqui tenho valores inteiros para fazer a operação
    spreadsheet[key] = execute_operation(value[0], arg_1, arg_2)
    return spreadsheet[key]
    

for i in range(n):
    operation, arg_1, arg_2 = input().split()

    arg_1 = check_argument(arg_1)
    arg_2 = check_argument(arg_2)
    
    if isinstance(arg_1, int) and isinstance(arg_2, int):
        value = execute_operation(operation, arg_1, arg_2)
    else:
        value = (operation, arg_1, arg_2)
        
    spreadsheet.update({f"${str(i)}": value})

# Print results   
for key, value in spreadsheet.items():
    print(calculate_operation(key, value))
