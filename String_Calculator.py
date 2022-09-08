import re


def calculator(s):

    # sum variable for storing the addition value
    sum = 0

    # flag variable for detecting negative value

    flag = 0

    # Message for Negative Number
    msg = "Negative Not allowed : "

    # Adding the number corresponding to the alphabet
    for i in s:
        if (ord('a') <= ord(i) <= ord('z')):
            sum += (ord(i)-ord('a')+1)

    # find the digit in string and typecasting it into integer and storing it in list using regex
    result = [int(d) for d in re.findall(r'-?\d+', s)]

    # Adding values from the list
    for i in result:
        if i < 0:
            flag = 1
            msg = msg+str(i)+" "
        elif i >= 1000:  # if number greater than 1000 ignored it
            pass
        else:
            sum += i

    if flag == 0:
        return (sum)
    else:
        return (msg)
