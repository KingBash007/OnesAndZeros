# Program to find the number of the zero bits and one bits present in a number
# Function taking our number as input
def numberofbits(n):
 ones = 0
 zeros = 0
 # While our number is greater than a 0 check last bit and write shift
 while(n):
   if(n&1 == 1):
     ones += 1
   else:
     zeros += 1
   # Write shift number, remove the last bit, then check above
   n>>= 1
 print("\n \n ones = ", ones,"\n zeros = ", zeros)
number = int(input("Enter your number:"))
numberofbits(number)   
