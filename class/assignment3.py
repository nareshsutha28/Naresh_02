# # Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]
# list1= [2, 33, 222, 14, 25]
# print(list1[-1])

# # Write a Python function to get the largest number, smallest num and sum of all from a list. 
# list1=[2,4,7,9,6,4,52,68,9,6,43]
# def fun(list1):
#     print('largest number:', max(list1))
#     print('smallest number:', min(list1))
#     print('sum of all number:', sum(list1))
# fun(list1)

# # Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.  
# list2=["naresh", 'suthar', 'nayan', 'a', 'aliya', 'asha']
# b=0
# for i in list2:
#     if len(i)>=2 and i[0]==i[-1]:
#         b+=1
# print(b)


# Write a Python program to remove duplicates from a list. 
# list1=[2,4,7,9,6,4,5,2,6,8,9,6,4,3]
# print(list(set(list1)))
# list3=[]
# for i in list1:
#     if i not in list3:
#         list3.append(i)
# print(list3)

# # Write a Python program to check a list is empty or not. 
# list1=[2,4,7,9,6,4,5,2,6,8,9,6,4,3]
# list2=[]
# def fun(l):
#     if len(l)!=0:
#         print("list is not empty")
#     else:
#         print("list is empty")
# fun(list1)
# fun(list2)

# Write a Python function that takes two lists and returns true if they have at least one common member
# list1=[6,3]
# list2=[4,7,2,3]
# for i in list1:
#     if i in list2:
#         print('True')
#         break
# else:
#     print('False')

# # Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30. 
# list1=[]
# for i in set(range(1,31)).difference(set(range(6,26))):
#         list1.append(i**2)
# print(list1)

# for i in range(1,31):
#     list1.append(i**2)
# p=list1[:5]
# p.extend(list1[-5:])
# print(p)


#  Write a Python function that takes a list and returns a new list with unique elements of the first list.
# list1=[2,4,4,3, 'Naresh', 4,6,8,7]
# def fun(l,p):
#     f=[]
#     for i in l:
#         if type(i)!=p:
#             f.append(i)
#     print(f)
# fun(list1,int)

# #  Write a Python program to convert a list of characters into a string. 
# list1=['a','c','d','d','e']
# p=''.join(list1)
# print(type(p))
# print(p)

# # Write a Python program to select an item randomly from a list. 
# import random
# list1=['a','c','d','d','e',6,56,5]
# print(list1[random.randrange(0,len(list1))])

# Write a Python program to find the second smallest number in a list. 
# list1=[2,4,7,9,6,4,5,6,8,9,6,4,3]
# list1.sort()
# print(list1[1])

# Write a Python program to get unique values from a list 
# list1=[2,4,7,9,6,4,5,2,6,8,9,6,4,3]
# def fun(l):
#     f=[]
#     for i in l:
#         if l.count(i)==1:
#             f.append(i)
#     print(f)
# fun(list1)

# # Write a Python program to split a list into different variables. 
# n= int(input("number of spliting element:"))
# o=[]
# m=-1
# p= ['Naresh', 'Suthar', 'Deepak', 'Prajapati', 'Hello', 'World']
# for i in range(len(p)):
#     if i%n!=0:
#         o[m].append(p[i]) 
#     else:
#         m=m+1
#         o.append([])
#         o[m].append(p[i])
# print(o)

# # Write a Python program to create a tuple with different data types.
# p= ['Naresh', 'Suthar', 'Deepak', 'Prajapati', 'Hello', 'World']
# b=tuple(p)
# print(b) 

# # Write a Python program to create a tuple with numbers.
# p= (2,4,6,8,6,6.6,5.6,3.7)
# print(p)


# # Write a Python program to convert a tuple to a string. 
# p= ('Naresh', 'Suthar', 'Deepak', 'Prajapati', 'Hello', 'World')
# r= ' '.join(p)
# print(r)


# #  Write a Python program to check whether an element exists within a tuple. 
# p= ('Naresh', 'Suthar', 'Deepak', 'Prajapati', 'Hello', 'World')
# n=input("Enter string to find:")
# if n in p:
#     print(n, 'is exist in list.')
# else:   
#     print(n, 'is not existed in list.')

#  Write a Python program to find the length of a tuple.
# p= ('Naresh', 'Suthar', 'Deepak', 'Prajapati', 'Hello', 'World')
# print(len(p))

# #  Write a Python program to convert a list to a tuple.
# p= ['Naresh', 'Suthar', 'Deepak', 'Prajapati', 'Hello', 'World']
# b=tuple(p)
# print(b) 

# #  Write a Python program to reverse a tuple. 
# p= ('Naresh', 'Suthar', 'Deepak', 'Prajapati', 'Hello', 'World')
# p=list(p)
# print(p.reverse())
# print(tuple(p))

# Write a Python program to replace last value of tuples in a list. 
# l=[(5,3,5), (8,5,3), (9,7,4)]
# o=[]
# for r in l:
#     i=r[:-1]+(100,)
#     o.append(i)
# print(o)

# Write a Python program to find the repeated items of a tuple. 
# p=(3,6,8,0,7,5,3,5,8,0,9,6,4)
# c=[]
# for i in p:
#     if p.count(i)>1:
#         if i not in c:
#             c.append(i)
# print(c)


# Write a Python program to remove an empty tuple(s) from a list of tuples
# p=[(3,56),4,67,(),(54,68,9),(),[],{},(),(), (35,7) ]
# for i in p[::-1]:
#     if type(i)==tuple and len(i)==0:
#         p.remove(i)
# print(p)

# Write a Python program to unzip a list of tuples into individual lists. 
# l = [(1,2), (3,4)]
# print(list(zip(*l)))

# Write a Python program to convert a list of tuples into a dictionary. 
# l = [(1,"Naresh"), (2,"Deepak"), (3,"Mayank"), (4,"Satish")]
# print(dict(l))

# p={}
# for i in l:
#     p[i[0]]=i[1]
# print(p)

# Write a Python script to sort (ascending and descending) a dictionary by value
# p={3: 'Naresh', 2: 'Deepak', 5: 'Mayank', 4: 'Satish'}
# # print(p.items())
# s=[]
# for i in p.items():
#     s.append(i[1])

# s=dict(sorted(p.items(), key = lambda x: x[1], reverse=True))
# print(s)

# s=dict(sorted(p.items(), key = lambda x: x[1]))
# print(s)



# Write a Python script to concatenate following dictionaries to create a new one.
# p={3: 'Naresh', 2: 'Deepak', 5: 'Mayank', 4: 'Satish'}
# r={1:"Suthar", 6:"Hitesh"}
# s={7:"Ritesh", 8:"Haresh", 9:"Malin"}
# g={10:"Shankar", 11:"Sunil"}
# j={}
# for i in [p,r,s,g]:
#     j.update(i)
# print(j)

# # Write a Python script to check if a given key already exists in a dictionary. 
# s=int(input("Enter the key:"))
# p={3: 'Naresh', 2: 'Deepak', 5: 'Mayank', 4: 'Satish'}
# if s in p.keys():
#     print(s, "is allready exist.")
# else:
#     print(s, "is not exist in given dictionary.")


# Write a Python script to print a dictionary where the keys are numbers between 1 and 15. 
# p={}
# for i in range(1,16):
#     o=input("Enter a value:")
#     p[i]=o
# print(p)
# 

#  Write a Python program to check multiple keys exists in a dictionary 
# p={3: 'Naresh', 2: 'Deepak', 5: 'Mayank', 4: 'Satish', 5:"Haresh"}
# print('Key in the dictionary:',list(p.keys()))
    
    
# Write a Python script to merge two Python dictionaries 
# p={3: 'Naresh', 2: 'Deepak', 5: 'Mayank', 4: 'Satish', 5:"Haresh"}
# o={1:"Hello", 6:"akash", 7:"Jitendra"}
# p.update(o)
# print(p)

# # Write a Python program to map two lists into a dictionary.
# key= [1,2,3,4,5,6,7,8,9,10]
# value= ["Naresh", "Deepak", "Hello", "Sonalisa", "Dhruv", "Gineous", "Ayushi", "Neha", "Pankaj", "Kamlesh"]
# d=dict()
# for i in range(10):
#     d[key[i]]=value[i]
# print(d)

# # Write a Python program to combine two dictionary adding values for common keys
# p={2:65,6:86,4:65,7:43,5:53,8:98}
# t={1:65,6:78,9:65,7:45,5:23,8:12}
# o=dict()
# for i in list(p.keys()):
#     if i in list(t.keys()):
#         o[i]=p[i]+t[i]
        
#     else:
#         o[i]=p[i]
# for i in list(t.keys()):
#     if i not in list(p.keys()):
#         o[i]=t[i]

# print(o)


# # Write a Python program to print all unique values in a dictionary. 
# p={'a':32, 'b':33, 'c':75, 'd':33, 'e':42, 'f':32, 'g':32, 'h':65, 'i':65}
# i=set(p.values())
# print(list(i))


# # Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
# o={1:["a","b"],2:["c","d"]}

# r=list(o.values())
# for i in r[0]:
#     for j in r[1]:
#         p=i+j
#         print(p, end=" ")

# print()
        

# # Write a Python program to find the highest 3 values in a dictionary 
# p={'a':32, 'b':33, 'c':75, 'd':54, 'e':42, 'f':97, 'g':43, 'h':44, 'i':65}
# c= p.values()
# c=sorted(list(p.values()), reverse=True)
# v=[c[0],c[1],c[2]]
# print(v)


# Write a Python program to combine values in python list of dictionaries. 
from collections import Counter
# p=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}] 

# result = Counter()

# for d in p:
#     result[d['item']] += d['amount']
# print(result) 


#write e a Python program to create a dictionary from a string. 
# rel= Counter('w3resource')
# print(rel)


# write  a Python function to calculate the factorial of a number (a nonnegative integer) 
# def fact(a):
#     if a<=0:
#         print("Not posible.")
#     else:
#         b,c=1,1
#         while b<=a:
#             c*=b
#             b+=1
#         print(c)
# fact(5)

#  Write a Python function to check whether a number is in a given range
# def ok(a,*l ):

#     if a in (range(*l)):
#         print("Given Number is availble in range")
#     else:
#         print("Given Number is not availble in range") 

# ok(3,0,9)

# #  Write a Python function to check whether a number is perfect or not. 
# def perfect(a):
#     b=0
#     for i in range(1,int(a+1/2)):
#         if a%i==0:
#             b+=i
#     if b==a:
#         print(a, "is a perfect number.")
#     else:
#         print(a, "is not perfect number.")

# perfect(26)
# perfect(28)

# Write a Python function that checks whether a passed string is palindrome or not
# def ispalidrome(a):
#     start,end= 0, len(a)-1
#     while start<=end:
#         if not a[start]==a[end]:
#             return False
        
#         start+=1
#         end-=1
#     else:
#         return True

# print(ispalidrome('cawaq'))
# print(ispalidrome('awa'))

# #  Write a Python program to read a random line from a file. 
# import random
# file=open("Naresh.txt", "r")
# a=(file.read()).split(".")[:-1]
# print(random.choice(a))

# # Write a Python program to convert degree to radian 
# import math
# p=int(input("enter value in degree:"))
# a=math.pi*p/180
# print(a)


# Write a Python program to calculate the area of a trapezoid 

