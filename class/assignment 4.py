# # Write a Python program to read an entire text file. 
# p=open("Naresh.txt", "r")
# print(p.read())
# p.close()

# # Write a Python program to append text to a file and display the text.
# p=open("Naresh.txt", "a")
# p.write("You have done Prime Function.Thank You for visit, Bye.")
# p.close()

# # Write a Python program to read first n lines of a file. 
# n=int(input("enter start line number:"))
# p=open("Naresh.txt", "r")
# r=(p.read())
# p.close()
# a=(r.split("\n"))
# for i in a[:n]:
#     print(i)

# # Write a Python program to read last n lines of a file.
# n=int(input("enter ending line number:"))
# p=open("Naresh.txt", "r")
# r=(p.read())
# p.close()
# a=(r.split("\n"))
# for i in a[-n:]:
#     print(i)

# # Write a Python program to read a file line by line and store it into a list
# p=open("Naresh.txt", "r")
# r=(p.read())
# p.close()
# a=(r.split("\n"))
# print(a)


# Write a Python program to read a file line by line store it into a variable. 
# p=open("Naresh.txt", "r")
# r=(p.read())
# p.close()
# a=(r.split("\n"))
# o=""
# for i in a:
#     o=o+i
# print(o)

# # Write a python program to find the longest words.
# o="Write a Python program to read first n lines of a file. Usually, the paper is divided into sections for each of those major. groupings labelled A, B, C, and so on, with pagination prefixes yielding. page numbers A1-A20, B1-B20, C1-C20, and so on. Most traditional. papers also feature an editorial page containing editorials. written by an editor or by the papers editorial board and expressing an opinion. on a public issue, opinion articles called op-eds written by guest writers. which are typically in the same section as the editorial"
# o=o.replace(",", "")
# o=o.replace(".", "")
# p=o.split(" ")
# r={len(i) for i in p }
# for i in p:
#     if len(i)==max(r):
#         print(i)


# Write a Python program to count the number of lines in a text file.
# p=open("Naresh.txt", "r")
# r=(p.read())
# p.close()
# a=(r.split("\n"))
# print(len(a)) 


# Write a Python program to count the frequency of words in a file.
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


# Write a Python program to write a list to a file. 
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


# # Write a Python program to copy the contents of a file to another file.
# o=open("Helo.txt", "r")
# i=open("selo.txt", "w+")
# line=o.read()
# i.write(line)
# o.close()
# i.seek(0)
# print(i.read())
# i.close()


# Write python program that user to enter only odd numbers, else will raise an exception. 
# o=int(input("Enter a number: "))
# if o%2!=0:
#     print("")
    # ................


