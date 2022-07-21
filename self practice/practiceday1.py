# def multiply(a, b): print(a * b)
# multiply(3,5)
# .....

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
# b=[ i for i in range(1,1000) if i%3==0 or i%5==0]
# print(sum(b))
# ........

# a=[1,2]
# for i in range(1,11): a.append(a[len(a)-1] + a[(len(a)-2)]) 
# print(a)
# .......

# p=int(input("enter the value you want:"))
# a=[1,2]
# b=1
# while b:
#     b=(a[len(a)-1] + a[(len(a)-2)])
#     if b<p:
#         a.append(b)
    # else:
#         break
#     b+=1
       
# print(a)
# print(len(a))
# ..........

# p="mayank"
# a=range(len(p))
# for i in a:
#     print(p[i])
# ........

# p=str(input("Enter a nuber in formate of :"))
# print(p[1:-1])

#.........

# Find factorial value 
# a= int(input("Enter value for factorial:"))
# c=1
# for i in range(0,a):
#     c=c*(a-i)
# print(c)
# ..........

# a= int(input("Enter value for factorial:"))
# fac=1
# for i in range (1,a+1):
#     fac*=i
# print(fac)

# .......

# a=["java", "python"]
# b=["Naresh", "suthar"]
# # for i in zipped:  
# #     for j in b:
# #         print(i,j )

# c=zip(a,b)
 # print(list(c))
