# list is the group of element.
# It can contain element like integer, float, strting, variable and object etc. 


# list1=[1,2,3,4,5]
# list2=[[1,2,3,4,5],[7,8,6,4,3]]
# print(list2[1][4])
# .......

# list1=[1,2,3,4,5]
# list2=[[[1,2],[[3,4],5]],[7,8,6,4,3]]
# print(list2[0][1][0][1])
# ........

# x=(1,3,56,78,5)
# print(type(x))
# y=list(x)
# print(y)
# print(type(y))
# ..........

# l=[1,32,4,6,8,5,3]
# list1=["Apple", "Ball", "Sat","5"]
# print(len(l))
# print(max(l))
# print(min(list1))
# print(max(list1))

# list2=(1,3,5,7,9)
# a=list(list2)
# print(a)
# .........

# y=5
# x=2
# l.append(x)
# print(l)
# .........

# list1=[1,3,5,7]
# x=4
# list2=[5,8,7]
# for i in list2:
#     list1.append(i)
# print(list1)
# ...........

# list1.extend(list2)
# print(list1)
# ...........

# list1.insert(2, x)
# print(list1)

# list1.insert(2, list2)
# print(list1)

# ..........

# c=[2,7,5,7,6,3,6,2,"suthar","suthar",6,9,5,2,5,2,6,7,3,2,7,7,4]
# print(c.count(2))
# ...............

# print(c.index("suthar"))
# ...........

# c.pop(8)
# print(c)
# c.remove('suthar')
# print(c)
# ...........

# fOR ONLY ONE DIGIT
# m=int(input())
# n=int(input())
# c=[]
# a=str(input())
# x=a.split()
# b=str(input())
# y=b.split()
# y.sort(reverse=True)
# x.sort()
# print(x)
# if len(x)==n and len(y)==m:
#     x.extend(y)
    
#     print(*c)
# else:
#     print("Not applicable")
    
# print(b)
# ............

# a= "2 6 8 2 3 9 7 5 2 3 2 3 6 7"
# a=str(input("enter the array number:"))
# x=a.split()
# b=[]
# for i in x: 
#     if i not in b:
#         b.append(i)
# print(b)
# .........

# n=int(input())
# list1=list(map(int,input().split()))
# if len(list1)==n:
#     print("NO")
# else:
#     print("yes") 
# from collections import counter
# lst = [1,2,3,4,5,2,2,4,4,5,5]
# x = set(lst) 
# print(x) 
# y = list(x) 
# print(*y) 

# for i in lst: 
#     if i != 2:
# print(v)
# ..............

# x=list(map(int, input().split()))
# y=list(map(int, input().split()))
# z=list(map(int, input().split()))
# y.sort()
# z.sort(reverse=True)
# if len(y)==x[0] and len(z)==x[1]:print(*y+z)
# else: print("Not Aplicable")
# .........

# def fun1(a):
#     return a*a
# def fun2(b):
#     return b*b*b
# squ=[fun1, fun2]
# for i in [1,2,3,4,5]:
#     x=list(map(lambda v : v(i), squ))
#     print(x)
# ........

# x= ["Hitesh", "Naresh", "Deepak", "suresh"]
# print(x.index("Hitesh"))
# .........

# x=[60,34,33,45,34,97,76]
# print(sorted(x, reverse=True))
# print(sorted(x))
# .........

# x=[3,5,7,5,3,5,7,7,6,4,3,2,2]
# print(set(x))


# n=int(input("Enter a number:"))
# x= list(map(int, input("enter a value:").split()))

# if len(x)==n:
#     print(min(x))
# else:
#     print("Enter a", n, "number of list")


# l1= ['Naresh', 'Deepak',1 , 23, 32.4, 0, True, False]
# l2=[34, 4.6, 'Mahesh', 'Suthar']
# l4=l1.copy()
# l4.pop()
# print(l4)
# print(l1)
# print(l1.count(1))
# print(l1.count(0))

# l5=[]
# l5.append(10)
# print(l5)
# l5.append(20)
# print(l5)
# l5.append(30)
# print(l5)
# l5.append(40)
# print(l5)
# l5.append(50)
# print(l5)
# l5.pop()
# print(l5)
# l5.pop()
# print(l5)
# l5.pop()
# print(l5)
# l5.pop()
# print(l5)


# TO iterate list
# l1= ['Naresh', 'Deepak',1 , 23, 32.4, 0, True, False]
# for i in l1:
#     print(i)


# l1= [1 , 23, 32.4, 0 ]
# (l1.sort())
# print(l1)