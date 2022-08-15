# # 1. Write a Python program to read an entire text file. 
# p=open("Naresh.txt", "r")
# print(p.read())
# p.close()

# # 2. Write a Python program to append text to a file and display the text.
# p=open("Naresh.txt", "a")
# p.write("You have done Prime Function.Thank You for visit, Bye.")
# p.close()

# #3. Write a Python program to read first n lines of a file. 
# n=int(input("enter start line number:"))
# p=open("Naresh.txt", "r")
# r=(p.read())
# p.close()
# a=(r.split("\n"))
# for i in a[:n]:
#     print(i)

# #4. Write a Python program to read last n lines of a file.
# n=int(input("enter ending line number:"))
# p=open("Naresh.txt", "r")
# r=(p.read())
# p.close()
# a=(r.split("\n"))
# for i in a[-n:]:
#     print(i)

# #5. Write a Python program to read a file line by line and store it into a list
# p=open("Naresh.txt", "r")
# r=(p.read())
# p.close()
# a=(r.split("\n"))
# print(a)


# 6. Write a Python program to read a file line by line store it into a variable. 
# p=open("Naresh.txt", "r")
# r=(p.read())
# p.close()
# a=(r.split("\n"))
# o=""
# for i in a:
#     o=o+i
# print(o)

# #7.  Write a python program to find the longest words.
# o="Write a Python program to read first n lines of a file. Usually, the paper is divided into sections for each of those major. groupings labelled A, B, C, and so on, with pagination prefixes yielding. page numbers A1-A20, B1-B20, C1-C20, and so on. Most traditional. papers also feature an editorial page containing editorials. written by an editor or by the papers editorial board and expressing an opinion. on a public issue, opinion articles called op-eds written by guest writers. which are typically in the same section as the editorial"
# o=o.replace(",", "")
# o=o.replace(".", "")
# p=o.split(" ")
# r={len(i) for i in p }
# for i in p:
#     if len(i)==max(r):
#         print(i)


#8. Write a Python program to count the number of lines in a text file.
# p=open("Naresh.txt", "r")
# r=(p.read())
# p.close()
# a=(r.split("\n"))
# print(len(a)) 


#9. Write a Python program to count the frequency of words in a file.
# p=open("Naresh.txt", "r")
# r=(p.read())
# p.close()
# a=(r.split("\n"))
# o=""
# for i in a:
#     o=o+i
# o=o.replace(",", "")
# o=o.replace(".", "")
# p=o.split(" ")
# w={}
# for i in p:
#     if i not in w.keys():
#         w[i]=p.count(i)
# print(w)


#10. Write a Python program to write a list to a file. 
# u=("Naresh", "Kamlesh", "Rudra", "Deepak", "Jay", "Hiteh", "Harsh")
# p=open("Helo.txt", "w")
# p.write("Given list are following: \n")
# p.close()
# p=open("Helo.txt", "a")
# o=0
# for i in u: 
#     o+=1
#     p.write(str(o)+":"+i+"\n" )
# p.close()
# p=open("Helo.txt", "r")
# print(p.read())
# p.close()


# #11. Write a Python program to copy the contents of a file to another file.
# o=open("Helo.txt", "r")
# i=open("selo.txt", "w+")
# line=o.read()
# i.write(line)
# o.close()
# i.seek(0)
# print(i.read())
# i.close()


#12. Write python program that user to enter only odd numbers, else will raise an exception. 
# o=int(input("Enter a number: "))
# if o%2!=0:
#     print("given value is odd")
# else:
#     print("given number is even.")
    # ................


#13. Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle 
# class Rectangle:
#     def __init__(self, length, width):
#         self.length=length
#         self.width=width
    
#     def method(self):
#         total=self.length*self.width
#         print(total)

# h1=Rectangle(4, 5)
# h1.method()



# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle  
# import math
# class Circle:
#     def __init__(self, radius):
#         self.radius=radius
        
    
#     def area(self):
#         total= math.pi*(self.radius**2)
#         print(total)

#     def perimeter(self):
#             total=2*math.pi*self.radius            
#             print(total)

# h1=Circle(5)
# h1.area()
# h1.perimeter()


