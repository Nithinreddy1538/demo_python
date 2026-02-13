import math 
num=int(input("enter a number:"))
if num>=0:
    print("the square root is",math.sqrt(num))
    print("the cube root is",num**(1/3))
else:
    print("square root and cube root are not defined for negative numbers")