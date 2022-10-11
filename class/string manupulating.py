# from ast import Num
# from binascii import b2a_hex
# from datetime import date
# from math import factorial
# from re import X
# from numpy import identity


sd='naresh suthar'
# print(sd)

# for capitalization of first letter
# print(sd.capitalize())

# for lower case
# c="DGFDGBDFBGFB"
# print(c.casefold())

# to count any number or word
# print(sd.count('r'))

# to check last digit 
# print(sd.endswith("r"))

# to check first digit
# print(sd.startswith("r"))

# to find number in string
# print(sd.find("t"))

# print(sd.index("su"))

# with space it will be false otherwise it will be true
# print('fhew ifwe'.isalnum())

# it will be true if alphabatic in the string other wise it will be false
# print("adg".isalpha())

# check digit or not
# print("23".isdigit())

# print("1.1".isnumeric())

# to check identifier right or wrong
# print('in t'.isidentifier())

# print("sddg".islower())

# string should be capitalized
# print("Dsdof".istitle())

# print("FGGFG".isupper())

# vary important function 
# print("/".join("Naresh"))

# after the string joint with star or something
# print(sd.ljust(30,'*'))

# partition at first digit
# print(sd.partition("a"))

# replace one words to another word
# print(sd.replace('t', 'T'))

# skip the given word and patition are done
# print(sd.split("a", maxsplit=2))

# old case
# print("alpfewf.efe".isalnum())

# slicing
# print(sd[0:5])
# print(sd[1:9])

# print(sd[7:-9])
# .......

# Homework
# string=str(input("Enter your string:"))
# string="Indira Gandhi in 1974 applied in emergency of 78 Months when lead to on economic loss of 9 million." 
# b=[]
# print(string.split())
# for i in string.split():
#     if i.isdigit(): 
#         b.append(int(i))
# print("the maximum number is", max(b))
# ...........

# x = [int(i) for i in string.split() if i.isdigit()]
# print(x)
#.................

# import datetime
# i=input("Enter a date in formate of dd-mm-yyyy:")
# d = datetime.datetime.strptime(i, "%d-%m-%Y")
# print(d.strftime("%B"))
# print(d.strftime("%A"))
# print(d.strftime("%w"))
# print(d.strftime("%x"))
# .......
# 
# i=input("Enter a time in formate of hh-mm-ss:")
# a=datetime.datetime.strptime(i, "%H-%M-%S")
# print(a.strftime("%X"))
# ..........

# string="hello, i am technology.technology is great thing in that time."
# print(string.replace("technology", "tech"))
# .........

# find factorial value
# n=int(input("Enter any number:"))
# print(factorial(n))
# ........
# b=[]
# n=str(input("Enter any vehicle number:"))
# a=list(n)
# for i in a:
#     if i.isdigit(): b.append(int(i))
# print(sum(b))
# ........

# a=[int(i) for i in list(n) if i.isdigit()]
# print(sum(a))
# .......

# n= 34

# print(even(n))

## Home work
# s="My name is Naresh Suthar"
# l=0
# for i in s:
#     if i.isalnum():
#         l+=1
# print("total number of character: ",l)
# ...........................
# p=0
# for i in s:
#     if i.isspace():
#         p+=1
# print("total number of space: ", p)
# # ..............

# print("Total number of words: ", len(s.split()))

