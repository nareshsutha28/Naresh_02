# def tostr(a):
#     b=str(a)
#     print('"',b,'"')
   
# tostr(999)
# x = [int(x) for x in input("Enter multiple value: ").split(",")]
# Sum=sum(x)
# print(Sum)
#
# for x in range(9):
#   print(x)

# ..........
# n=int(input('enter number'))
# for x in range(n+1):
#  print(x)
    
# from re import X


# from copy import copy

# n=["Suthar","Naresh","Chauhan","Sardar"]
# b=["Deepak","Hitesh","Satish"]
# n.reverse()
# print(n)
# ........................

# swap the Value
# a=int(input("Enter A value of a:"))
# b=int(input("Enter A value of b:"))
# c=a
# a=b
# b=c
# print("value of a:", a)
# print("value of b:", b)
# ...................

# Find square root
# a=int(input("Enter A value of a:"))
# print("square root of a is", a**0.5)

# .....................

# Generate Random number
# import random
# print(random.randint(0,6))
# ...................

# convert sq. mtr. to sq. ft.
# a=int(input("Enter A value in sq. mtr:"))
# b= a*10.764
# print(b)
# ...................

# use of .formate
# x = 5
# y = 10
# print('The value of x is {1} and y is {0}'.format(x,y))
# ..................


# a=35.6565566
# print("the value a is %3.2f" %a)

# x = 12.3456789
# print('The value of x is %3.2f' %x)
# ..................
 
#  convert str to int
# a=str(input("enter the value of a:"))
# c=int(a)
# print(c) 
# .............

# import math module and print pi value from it
# import math
# print(math.pi)
# ...................

# import sys
# print(sys.path)
# ...................

# eval function
# import math
# number = 9
# square_number = eval('number % math.pi')
# print(square_number)
# ..............................

# import sympy
# x=range(0,10)
# for i in x:
#     y= sympy.isprime(i)
#     if y==True:
#         print(i, sep=" ")
# ........................

# a=[7,8,4]
# b=[7,43,24]
# c=[]
# for i in range(0,len(a)):
#     c.append(a[i]+b[i])

# print(str(c))
# ...................

# c=[]
# d=[]
# n=int(input("Enter the element you want to add:"))
# for i in range(0,n):
#     a=int(input("enter value no."))
#     c.append(a)
# print(c)
# for i in range(0,n):
#     a=int(input("enter value no."))
#     d.append(a)
# print(d)
# e=[]
# for i in range(0,n):
#     e.append(c[i]+d[i])
# print(str(e))

# ...............
# from collections import OrderedDict
# n=int(input("Enter a number:"))
# a=str(input("Type anything:"))
# c=int(len(a)/n)

# b= []
# for i in range(0,n):
#     d=(a[(i*c):(i+1)*c])
#     b.append(d)
# e=[]

# for i in b:
#     e.append("".join(OrderedDict.fromkeys(i)))
# for i in e:
#     print(i)


# import math 
# print(math.factorial(4))
# print(math.ceil(4.005))
# print(math.floor(4.005))
# print(math.trunc(4.0005))
# print(math.trunc(-4.005))
# print(math.pow(2,3))



# for i in range(1,10):
#     for j in range(i, 2*i):
#         print(j, end="")
#     print()



