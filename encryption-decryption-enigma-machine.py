import sys

# Input
operation = input()
pseudo_random_number = int(input())

rotor_list = []
for i in range(3):
    rotor_list.append(input())
    
message = input()

def calculate_position(alphabet, character, offset):
    pos = alphabet.index(character)
    new_pos = pos + offset
    
    if abs(new_pos) < len(alphabet):
        return new_pos
    elif new_pos < 0:
        times = abs(int(new_pos / len(alphabet)))
        return new_pos + len(alphabet) * times
    elif new_pos > 0:
        times = abs(int(new_pos / len(alphabet)))
        return new_pos - len(alphabet) * times


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if operation == "ENCODE":
    encoded_message = ""
    for i in range(len(message)):
        character = message[i]
        alphabet_pos = calculate_position(alphabet, character, pseudo_random_number + i) 
        encoded_message += alphabet[alphabet_pos]
        
    for rotor in rotor_list:
        rotor_message = ""
        for i in range(len(encoded_message)):
            character = encoded_message[i]
            alphabet_pos = alphabet.index(character)
            rotor_message += rotor[alphabet_pos]
        encoded_message = rotor_message
        
    print(encoded_message)

elif operation == "DECODE":
    rotor_message = message
    for rotor in reversed(rotor_list):
        temp_message = ""
        for i in range(len(rotor_message)):
            character = rotor_message[i]
            rotor_pos = rotor.index(character)
            temp_message += alphabet[rotor_pos]
        rotor_message = temp_message

    decoded_message = ""
    for i in range(len(rotor_message)):
        character = rotor_message[i]
        alphabet_pos = calculate_position(alphabet, character, -(pseudo_random_number + i)) 
        decoded_message += alphabet[alphabet_pos]
        
    print(decoded_message)
