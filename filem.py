import random

like=open("list.txt", "w")
odd=open('odd.txt', "w+")
even=open('even.txt', "w+")
prime1=open("prime.txt", "w+")
for i in range(10):
    like.write(str(random.randint(1,100))+',')

like.close()
like=open("list.txt", "r")

for i in like.read().split(",")[:-2]:
    if int(i)%2==0:
        even.write(i+",")
   
    else:
        odd.write(i+",")
        
        for j in range(3, int(int(i)/2)+1, 2):
            if int(i)%j==0:
                break
        else:    
            prime1.write(i+",")           
      
like.seek(0)
print(like.read())
even.seek(0)
print(even.read())
odd.seek(0)
print(odd.read())
prime1.seek(0)
print(prime1.read())    

even.close()
like.close()
odd.close()
prime1.close()
# odd=open("odd.txt", "r+")
# odd=open("even.txt", "r+")

# for i in like.split(","):
#     if 

# print(like.read())
# like.close()

# like=open("list1.txt", "a")
# like.write("i am naresh ")
# like.close()

# like=open("list.txt", "a")
# like.write("\n How are you")
# like.close()


