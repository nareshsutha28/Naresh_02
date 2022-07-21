# assi:-1.  If a number is positive, negative or zero. 

# try:
#     x= int(input('Enter any number:'))
# except ValueError:
#     print("Enter a valid number")
# else:    
#     if x<0:
#         print('Number is negative.')
#     elif x==0:
#         print('Number is Zero.')    
#     else:
#        print('Number is positive.')
# .....

# ass2.  to get the Factorial number of given number
# z=int(input("Enter any number:"))
# x=1
# for i in range(0,z-1):
#     x*=(z-i)
# print(x)

# from math import factorial 
# print(factorial(z))
# ........

# assi 3.  to get the Fibonacci series of given range
# x= int(input("enter any number:"))
# a,b= 0,1
# print(a, end=' ')
# while b<x:
#     print(b,end=" ")
#     a,b= b,a+b
# .........

# assi 4.swap two number with temp variable and without temp variable
# x=int(input("enter value A"))
# y=int(input("enter value B"))
# x,y= y,x
# print("x:",x)
# print("y:",y)
# ....
# temp=x
# x=y
# y=temp
# print("x:",x)
# print("y:",y)

# assi 5.o find whether a given number is even or odd, print out an appropriate message to the user  
# x=int(input("enter value "))
# if x%2==0:
#     print('given number is even.' )
# else:
#     print('given number is odd.' )


# assi 6. to test whether a passed letter is a vowel or not. 
# x= input("enter a single character:")
# if x=='a' or x=='e' or x=='i' or x=='u' or x=='o':
#     print('character is vovel.')
# else:
#     print('character is consolance.')


# assi.7.to sum of three given integers. However, if two values are equal sum will be zero. 
# a=int(input("enter a number A:"))
# b=int(input("enter a number B:"))
# c=int(input("enter a number C:"))
# if a==b or b==c or c==a:
#     print("sum of value is zero.")
# else:
#     print("sum of value is", a+b+c)

# assi 8. program that will return true if the two given integer values are equal or their sum or difference is 5. 
# a=int(input("enter a number A:"))
# b=int(input("enter a number B:"))
# if a==b or a+b==5 or a-b==5 or b-a==5:
#     print("True")
# else:
#     print('False')    

# assi 9. program to sum of the first n positive integers 
# a=int(input("enter a number :"))
# sum=0
# for i in range(1, a+1):
#     sum+=i
# print(sum)

# assi 10. program to calculate the length of a string. 
# a=input("enter a number :")
# # print(len(a))
# b=0
# for i in a:b+=1
# print (b)

# assi 11. program to count the number of characters (character frequency) in a string 
# a=input("enter a string :")
# b=input('charecter which want to count:')
# c=0
# for i in a:
#     if i==b:
#         c+=1
# print(c)
# print(a.count(b))


# assi 12. program to count occurrences of a substring in a string. 
# a=input("enter a string :")
# b=input('substring which want to count:')
# print(a.count(b))

# assi 13. program to count the occurrences of each word in a given sentence 
# s=input("enter a string :")
# l=0
# for i in s:
#     if i.isalnum():
#         l+=1
# print("total number of character: ",l)

# assi 14.program to get a single string from two given strings, separated by a space and swap the first two characters of each string.  
# s=input("enter a string :")
# w=input("enter a string :")
# x=w[0:2]+s[2:]
# y=s[0:2]+w[2:]
# print("The string is ",x,y )

# assi 15.  program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged. 
s=input("enter a string :")
if len(s)<=3:
    print(s)
elif s.endswith('ing'):
    print(s+"ly")
else:
    print(s+'ing') 
    

# assi 16. program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.  
# s="Rudra's condition is not poor."
# print(s.replace(s[(s.find('not')):((s.find('poor'))+4)], 'good'))

# assi 17.  function that takes a list of words and returns the length of the longest one.
# a=['Naresh', 'Suthar', 'Hasmukh', 'Ravi', 'Purushottam']
# def fun(a):
#     b=[]
#     for i in a:
#         b.append(len(i))
#     print(max(b))
# fun(a)

# assi 18. Python function to reverses a string if its length is a multiple of 4. 
# s= input("Enter a string: ")
# def fun(a):
#     if len(a)%4==0:
#         for i in a[::-1]:
#             print(i, end='')          
#     else:
#         print(a)
# fun(s)


# assi 19. Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. 
# s= input("Enter a string: ")
# if len(s)<2:
#     print("Empty string")
# elif len(s)==2:
#     print(s*2)
# else:
#     print(s[0:2]+s[(len(s)-2):])

# assi 20. Python function to insert a string in the middle of a string.  
# s="My name is Naresh"
# u=input("enter a substring: ")
# n=int(input("enter number at which you want to change: "))
# print(s[:n],u+s[n:])


