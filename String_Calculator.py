import re
from string import digits


def calculator(s):
    sum = 0
    multiply = 1
    detect_negative = 0
    sum_or_multipy = 0

    if len(s) == 0:
        return 0
    first_char = s[0]

    if first_char == '*':
        sum_or_multipy = 1

    msg = "Negative Not allowed : "

    for i in s:
        if (ord('a') <= ord(i) <= ord('z')) and sum_or_multipy == 0:
            sum += (ord(i)-ord('a')+1)

        elif (ord('a') <= ord(i) <= ord('z')) and sum_or_multipy == 1:
            multiply *= (ord(i)-ord('a')+1)

    digits = [int(d) for d in re.findall(r'-?\d+', s)]

    for i in digits:
        if i < 0 and sum_or_multipy == 0:
            detect_negative = 1
            msg = msg+str(i)+" "
        elif i >= 1000:
            pass
        else:
            if sum_or_multipy == 0:
                sum += i
            elif sum_or_multipy == 1:
                multiply *= i

    if detect_negative == 0 and sum_or_multipy == 0:
        return (sum)
    elif detect_negative == 0 and sum_or_multipy == 1:
        return (multiply)
    elif detect_negative == 1:
        return (msg)
