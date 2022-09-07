from unittest import result


def calculator(s):
   sum=0
   if len(s)==0:
    return 0
   result=s.split(',')
   for i in result:
    sum=sum+int(i)

   return(sum)


