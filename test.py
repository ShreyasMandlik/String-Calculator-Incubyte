def operations(digits):
    sum = 0
    multiply = 1
    detect_negative = 0
    sum_or_multipy = 0
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
    

