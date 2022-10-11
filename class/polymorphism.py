# there are two type of polymorphism 
# 1. Method Overriding
# 2. Method Overloading

# # 1 Method Overriding:
# class A:
#     def put(self):
#         print("This is value of A Class. ")

# class B(A):
#     def put(self):
#         print("This is value of B Class. ")
#         super().put()

# class C(B):
#     def put(self):
#         print("This is value of C Class. ")
#         super().put()


# s1=C()

# s1.put()



# # 1 Method Overriding:
# class A:
#     def put(self):
#         print("This is value of A Class. ")

# class B(A):
#     def put(self):
#         super().put()
#         print("This is value of B Class. ")

# class C(B):
#     def put(self):
#         super().put()
#         print("This is value of C Class. ")


# s1=C()

# s1.put()




# # 1 Method Overriding:
# class A:
#     def put(self):
#         print("This is value of A Class. ")

# class B:
#     def put(self):
#         # super().put()
#         print("This is value of B Class. ")

# class C(B, A):
#     def put(self):
#         super().put()
#         print("This is value of C Class. ")

# s1=C()
# s1.put()



# # 1 Method Overriding:
# class A:
#     def put(self):
#         print("This is value of A Class. ")

# class B(A):
#     def put(self):
#         super().put()
#         print("This is value of B Class. ")

# class C(A):
#     def put(self):
#         super().put()
#         print("This is value of C Class. ")

# class D(C,B):
#     def put(self):
#         super().put()
#         print("This is value of D Class. ")

# s1=D()
# s1.put()
