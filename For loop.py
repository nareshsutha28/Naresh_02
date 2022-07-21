# for install sympy: pip install sympy 
# for upgrade sympy: pip install --u sympy

# To check prime number
# from sympy import isprime
# n=int(input('Enter any number:'))
# a = isprime(n)
# if a==False:
#     print("the number is not a prime number")
# else:
#     print("the number is prime number")
# # ....................

# # another way
# import sympy
# n=int(input('Enter any number:'))
# a = sympy.isprime(n)
# if a==False:
#     print("the number is not a prime number")
# else:
#     print("the number is prime number")
# ..................

# range syntax: range(start, end, step)
# print number from 1 to n

# String wise
# n=int(input('Enter any number:'))
# x= range(1,n+1,2)
# for i in x :
#     print(i,end=' ')

# block wise
# n=int(input('Enter any number:'))
# x= range(1,n+1,2)
# for i in x :
#     print(i)

# .....................

# use of library
# x={'Harsh','Naresh','Vinit','Krupa'}
# for i in x:
#     print(i)

# # use of list
# x=['Harsh','Naresh','Vinit','Krupa']
# for i in x:
#     print(i)


# x=("nareash", "Suthar","harsh")
# print(x)
# ......................

# Nested for loop 
# x=range(1,6)

# for i in x:
#     for j in x:
#         print("*", end=' ')
#     print()
# ...............


# for i in range(1, 8):
#     for j in range(i):
#         print("*", end=' ')
#     print()
# ........

# while loop
# x=0
# while x<12:
#     print(x)
#     x+=2
# .............

# for i in range(1,10):
#     print("*"*i)
# ............

# for i in range(1,10):
#     print(" "*(9-i), "*"*i)

# ................
# for i in range(1,10):
#     print(" "*(9-i), " *"*i)

# ..............
# for i in range(1,10):
#     print(" "*(9-i), " * "*i)
# ...................

# for i in range(1,10):
    # print(*range(1,i))

# ............

# for i in range(9,0,-1):
#     print("  "*(i),*range(i,10))
# ...............

# for i in range(1,10):
#     print("  "*(i),*range(i,10))
# .........

# Find number is prime number or Not.
# n= int(input("Enter a number:"))
# if n%2==0:
    # print(n," is not a prime number.")
# else:
#     for i in range(3,int(n/2)+1,2):
#         if n%i==0:
#             print(n," is not a prime number.")
#             break
#     else:
#         print(n," is a prime number.")
# ..............

# fabonnacci series
# n= int(input("Enter a number:"))
# sum=0
# while n>0: 
#     sum+=n  
#     n-=1

# print(sum)

from sympy import *
print(isprime(4))