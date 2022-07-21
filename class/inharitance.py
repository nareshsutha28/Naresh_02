# creating a class from the existing class is called inharitance.
# There are total five types of inharitance 

# 1. single inharitance:
# class A:
#     def put(self, a):
#         print("value of a: ", a)

# class B(A):
#    def get(self, b):
#         print("value of b: ", b)
 
# s1= B()
# s1.put(45)
# s1.get(35)
    

# # 2. multilevel inharitance:
# class A:
#     def put(self, a):
#         print("value of a: ", a)

# class B(A):
#    def get(self, b):
#         print("value of b: ", b)
 
# class C(B):
#    def met(self, c):
#         print("value of b: ", c)

# s1= C()
# s1.put(45)
# s1.get(35)
# s1.met(75)


# # 3. multiple inharitance:
# class A:
#     def put(self, a):
#         print("value of a: ", a)

# class B:
#    def get(self, b):
#         print("value of b: ", b)
 
# class C(A,B):
#    def met(self, c):
#         print("value of b: ", c)

# s1= C()
# s1.put(45)
# s1.get(35)
# s1.met(75)

# # 4. herarchi inharitance:
# class A:
#     def put(self, a):
#         print("value of a: ", a)

# class B(A):
#    def get(self, b):
#         print("value of b: ", b)
 
# class C(A):
#    def met(self, c):
#         print("value of b: ", c)

# s1=C()
# s2=B()

# s1.put(45)
# s1.met(75)

# s2.put(34)
# s2.get(12)


# # # 4. Hibrid inharitance:
# class A:
#     def put(self, a):
#         print("value of a: ", a)

# class B(A):
#    def get(self, b):
#         print("value of b: ", b)
 
# class C(A):
#    def met(self, c):
#         print("value of c: ", c)

# class D(B,C):
#    def fat(self, d):
#         print("value of d: ", d)

# s1=D()

# s1.put(45)
# s1.get(12)
# s1.met(75)
# s1.fat(46)

