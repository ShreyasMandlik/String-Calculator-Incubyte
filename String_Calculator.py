import re

def calculator(s):

    # sum variable for storing the addition value
    sum = 0
    multiply=1
    # flag variable for detecting negative value

    flag = 0
    flag1=0             ## sum ==0  multiply ==1
    # Message for Negative Number
    if len(s)==0:
        return 0
    first_char=s[0]

    if first_char=='*':
        flag1=1

    msg = "Negative Not allowed : "

    # Adding the number corresponding to the alphabet
    for i in s:
        if (ord('a') <= ord(i) <= ord('z')) and flag1==0:
            sum += (ord(i)-ord('a')+1)

        elif (ord('a') <= ord(i) <= ord('z')) and flag1==1:
            multiply *=(ord(i)-ord('a')+1)

    # find the digit in string and typecasting it into integer and storing it in list using regex
    result = [int(d) for d in re.findall(r'-?\d+', s)]

    # Adding values from the list
    for i in result:
        if i < 0 and flag1==0:
            flag = 1
            msg = msg+str(i)+" "
        elif i >= 1000:  # if number greater than 1000 ignored it
            pass
        else:
            if flag1==0:
                sum += i
            elif flag1==1:
                multiply *=i

    if flag == 0 and flag1==0:
        return (sum)
    elif flag == 0 and flag1==1:
        return (multiply)
    elif flag==1:
        return (msg)
