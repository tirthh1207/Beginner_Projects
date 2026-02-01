
import re
from colorama import Fore

def validate_expression(exp):
    if not re.fullmatch(r'[0-9+\-*/.^() ]+', exp):
        raise ValueError("Invalid characters detected in expression.")

def cal_pattern(exp, pattern, operation):
    while re.search(pattern, exp):
        match = re.search(pattern, exp)
        x = float(match.group(1))
        op = match.group(2)
        y = float(match.group(3))
        result = operation(x, op, y)
        exp = exp[:match.start()] + str(result) + exp[match.end():]
    return exp

def mul_div(exp):
    pattern = re.compile(r'(-?\d+(?:\.\d+)?)([*/])(-?\d+(?:\.\d+)?)')
    return cal_pattern(exp, pattern, lambda x, op, y: x / y if op == '/' else x * y)

def add_sub(exp):
    exp = exp.replace('--', '+')
    numbers = re.findall(r'(?<!\d)-?\d+(?:\.\d+)?', exp)
    return sum(map(float, numbers))

def main(exp):
    
    exp = exp.replace(' ', '')
    validate_expression(exp)
    while '(' in exp:
        inside = re.compile(r'\([^()]+\)')
        match = re.search(inside, exp)
        if match:
            inside_exp = match.group()[1:-1]
            inside_result = main(inside_exp)
            exp = exp[:match.start()] + str(inside_result) + exp[match.end():]
    exp = mul_div(exp)
    return add_sub(exp)

if __name__ == "__main__":
    print('it is a CALCULATER which uses BODMAS rule-->')
    eq = input('Enter a simpel equation:')
    print(Fore.GREEN+eq+' = '+ str(main(eq)))