import re
def calculator(s):

   ## sum variable for storing the addition value
   sum=0   

   ## Message for Negative Number   
   msg="Negative Not allowed : "

   ## Adding the number corresponding to the alphabet 
   for i in s:                     
        if (96<ord(i)<123):  
            sum+=(ord(i)-96)

   ## find the digit in string and typecasting it into integer and storing it in list using regex 
   result = [int(d) for d in re.findall(r'-?\d+', s)]    
   

   ## Adding values from the list
   for i in result:
    if i<0:
            msg=msg+str(i)+" "
            return msg
    else:
        sum=sum+int(i)

   return(sum)


