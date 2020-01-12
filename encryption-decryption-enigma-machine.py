import sys


class AbstractOperation:
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    def __init__(self, incremental_number, rotor_list):
        self.incremental_number = incremental_number
        self.rotor_list = rotor_list
        
    def calculate_position(self, character, offset):
        pos = self.alphabet.index(character)
        new_pos = pos + offset
        
        if abs(new_pos) < len(self.alphabet):
            return new_pos
        elif new_pos < 0:
            times = abs(int(new_pos / len(self.alphabet)))
            return new_pos + len(self.alphabet) * times
        elif new_pos > 0:
            times = abs(int(new_pos / len(self.alphabet)))
            return new_pos - len(self.alphabet) * times
        
    def map_incremental_number(self):
        pass
    
    def map_rotor(self):
        pass
    
    
class EncodeOperation(AbstractOperation):
    def map_incremental_number(self, message):
        encoded_message = ""
        for i in range(len(message)):
            character = message[i]
            alphabet_pos = self.calculate_position(character, self.incremental_number + i)
            encoded_message += self.alphabet[alphabet_pos]
        return encoded_message

    def map_rotor(self, message):
        encoded_message = message
        for rotor in rotor_list:
            rotor_message = ""
            for i in range(len(encoded_message)):
                character = encoded_message[i]
                alphabet_pos = self.alphabet.index(character)
                rotor_message += rotor[alphabet_pos]
            encoded_message = rotor_message
        return encoded_message
    

class DecodeOperation(AbstractOperation):
    def map_incremental_number(self, message):
        encoded_message = ""
        for i in range(len(message)):
            character = message[i]
            alphabet_pos = self.calculate_position(character, -(self.incremental_number + i))
            encoded_message += self.alphabet[alphabet_pos]
        return encoded_message
    
    def map_rotor(self, message):
        decoded_message = message
        for rotor in reversed(rotor_list):
            temp_message = ""
            for i in range(len(decoded_message)):
                character = decoded_message[i]
                rotor_pos = rotor.index(character)
                temp_message += self.alphabet[rotor_pos]
            decoded_message = temp_message
        return decoded_message


class EnigmaMessage:
    def __init__(self, message):
        self.message = message
        
    def encode(self, operation: EncodeOperation):
        encoded_message = operation.map_incremental_number(self.message)
        encoded_message = operation.map_rotor(encoded_message)
        return encoded_message
    
    def decode(self, operation: DecodeOperation):
        decoded_message = operation.map_rotor(self.message)
        decoded_message = operation.map_incremental_number(decoded_message)
        return decoded_message

# Input
operation = input()
pseudo_random_number = int(input())

rotor_list = []
for i in range(3):
    rotor_list.append(input())
    
message = input()

if operation == "DECODE":
    operation = DecodeOperation(pseudo_random_number, rotor_list)
    decoded_message = EnigmaMessage(message).decode(operation)
    print(decoded_message)
elif operation == "ENCODE":
    operation = EncodeOperation(pseudo_random_number, rotor_list)
    encoded_message = EnigmaMessage(message).encode(operation)
    print(encoded_message)
    
