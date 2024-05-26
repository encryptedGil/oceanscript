import re

print("Oceanscript (c) encryptedGil 2024-Present")

def split_string(input_string):
    # Define the regular expression pattern
    pattern = r'([.;() ])'
    
    # Use re.split() to split the string and include the delimiters as tokens
    result = re.split(pattern, input_string)
    
    # Remove any empty strings from the result
    result = [s for s in result if s]
    
    return result

def parse(tokens):
    if len(tokens) >= 5 and tokens[0] == 'print' and tokens[1] == '(' and tokens[-1] == ')':
        # Join the tokens inside the parentheses to form the argument
        argument = ''.join(tokens[2:-1]).strip()
        if argument.startswith('"') and argument.endswith('"'):
            return ("print", argument[1:-1])  # Remove the surrounding quotes
        else:
            raise SyntaxError("Invalid argument for print function")
    else:
        raise SyntaxError("Invalid function")

def execute(command):
    if command[0] == "print":
            print(command[1])
    
    else:
        raise ValueError("Unknown command")

def interpreter(input_string):
    tokens = split_string(input_string)
    command = parse(tokens)
    execute(command)

# Example usage
while True:
    inputer = input("$~")
    interpreter(inputer)




