# # In oops, in consists of concept like, object, class, encapsulation, abstraction, polymorphysum
# class school:

# school.teacher(first)# it is for understanding.
# # there are two type of object one is attribute and other one is behavior. behavior is one one type of method we also can call it function.

#     def __init__(self, m1, m2): # Not need to call it for execution. and it is one type of constructor

#         self.m1=m1
#         self.m2=m2
#     def teacher(self):
#         print("student is :", self.m1 ,self.m2 )
    
# first= school("Naresh","Deepak")
# second= school("Mahendra", "Hello")

# first.teacher() # it is use generaally. if we will not passing any parameter in parenthesis then it will take "a" as a parameter
# second.teacher()

# .......

# class private:
    # def __init__(self):
    #     self.name= "Naresh"
    #     self.age= "19"

#     def update(self):
#         self.name= "Suthar"

# c1=private()
# c2=private()
# # c1.name="Deepak"
# c1.update()
# print(c1.name, c2.name, c1.age, c2.age)
# ........

# class mycomparison:
#     def __init__(self):
#         self.name= "Naresh"
#         self.age= "19"

#     def update(self):
#         self.age= "28"

#     def comp(self, other):
#         if self.age == other.age:
#             return True
#         else: 
#             return False
    
# c1=mycomparison()
# c2=mycomparison()
# c2.update()
# if c1.comp(c2):
#     print("the value are same")
# else:
#     print("they are different")
# # ........

# Class variable and static variable are same in python class.
# class mycomparison:
#     school= "saraswati" 
#     def __init__(self):
#         self.name= "Naresh"    # this two variable are instance variable.
#         self.age= "19"

#     def update(self):
#         self.age= "28"

#     def comp(self, other):
#         if self.age == other.age:
#             print("the value are same")
#         else:
#             print("they are different")

    # def pt(self):

    #     print(c1.school, c1.name, c1.age)
    # mycomparison.school= "gyandeep"
    
# c2=mycomparison()
# c1.comp(c2)
# c1=mycomparison()
  
# c1.update()
# c1.pt()
# ...........

# class mycomparison:
     
#     def __init__(self,m1,m2,m3):
#         self.m1= m1    
#         self.m2= m2
#         self.m3= m3

    
#     def comp(self):
#         print((self.m1+self.m2+self.m3)/3)
# s1=mycomparison(34, 64, 76)
# s2=mycomparison(54, 23, 76)

# s1.comp()
# s2.comp()

# ...........

# class school:
#     def __init__(self, m1, m2):
#         self.m1=m1
#         self.m2=m2
#         self.lap = self.laptop()
    
#     class laptop:
#         def __init__(self):
#             self.rom="1000GB"
#             self.ram="16GB"

#         def show(self):
#             print(self.rom, self.ram)
    
#     def show(self):
#         print(self.m1, self.m2)
#         self.lap.show()

# s1= school("Naresh", "19")

# s1.show()
# ........

# # inheritance is of two type: one is single level inheritance and multi level inheritance
# class A:
#     def practice1(self):
#         print("this is practice1")


# class B(A):
#     def practice2(self):
#         print("this is practice2") 

#     def practice3(self):
#         print("this is practice3")
    
#     def practice4(self):
#         print("this is practice4")

# # a1=A()
# a2=B()

# a2.practice1()
# a2.practice2()
# a2.practice3()
# a2.practice4()
# #this is called inheritance.
# .................


# class A:
#     def practice1(self):
#         print("this is practice1")


# class B(A):
#     def practice2(self):
#         print("this is practice2") 

#     def practice3(self):
#         print("this is practice3")
    
# class C(B):
#     def practice4(self):
#         print("this is practice4")

# # a1=A()
# # a2=B()
# a3=C()
# a3.practice1()
# a3.practice2()
# a3.practice3()
# a3.practice4()
##this is called multi level class
# # ...............

# class A:
#     def practice1(self):
#         print("this is practice1")


# class B:
#     def practice2(self):
#         print("this is practice2") 

#     def practice3(self):
#         print("this is practice3")
    
# class C(A,B):
#     def practice4(self):
#         print("this is practice4")

# # a1=A()
# # a2=B()
# a3=C()
# a3.practice1()
# a3.practice2()
# a3.practice3()
# a3.practice4()
# #this is called multiple inheritance.
# # ...............

##there are four type of polymorphism : first one is Duck typing, second one is operator overloading, third one is Method Overloading, Method Overriding.


# class school:
#     def __init__(self, m1, m2):
#         self.m1=m1
#         self.m2=m2

#     def __add__(self, other):
#         m1= self.m1 + other.m1
#         m2= self.m2 + other.m2
#         s3= school(m1, m2)
#         return s3

#     def __str__(self):
#         self='{}  {}'.format(self.m1, self.m2) 
#         return self


    # def __gt__(self, other):
    #     self = self.m1 + self.m2
    #     other = other.m1 + other.m2
    #     if self>other:
    #         return True
    #     else: 
    #         return False        

# s1= school(46,53) 
# s2= school(58,23)
# s3= s1+s2

# print(s3.__str__())
# if s1>s2:
#     print("s1 is greater then s2")
# else:
#     print("s1 is less then s2")

# ..........

# class example:
#         # def __init__(self,f ):
#         #     self.f=f
#     #     self.b=b
#     #     self.c=c

#         def sum(self, a=None, b=None, c=None):
#             if a!=None and b!=None and c!=None:
#                 d=a + b + c
#             elif  a!=None and b!=None:
#                 d=a + b
#             else:
#                 d=a
#             return (d)

# s1= example()
# # s1= example(,6,5)

# print(s1.sum(5,7))
# # .........

