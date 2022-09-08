import re
def calculator(input_string):
    sum = 0
    multiply = 1
    detect_negative = 0
    sum_or_multipy = 0

    if len(input_string) == 0:
        return 0
    first_char = input_string[0]

    if first_char == '*':
        sum_or_multipy = 1

    msg = "Negative Not allowed : "
    digits = [int(d) for d in re.findall(r'-?\d+', input_string)]

    for i in input_string:
        if (ord('a') <= ord(i) <= ord('z')):
            digits.append((ord(i)-ord('a')+1))

    for i in digits:
        if i < 0 :
            detect_negative = 1
            msg = msg+str(i)+" "
        elif i >= 1000:
            pass
        elif sum_or_multipy == 0:
            sum += i
        elif sum_or_multipy == 1:
            multiply *= i
    
    if detect_negative == 1:
        return (msg)
    elif sum_or_multipy == 0:
        return (sum)
    elif sum_or_multipy == 1:
        return (multiply)
    
