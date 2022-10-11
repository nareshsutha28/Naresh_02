class Hello:
    __hed='Narehs'

class Cell(Hello):
    # __hed='Narehs'
    pass

h2=Hello()
# # Gives Error
# print(h2.__hed)

# # Success
# print(h2._Hello__hed)

# # Gives Error
# h1=Cell()
# print(h1.__hed)

# # Gives Error
# h1=Cell()
# print(h1._Cell__hed)

# # success
# h1=Cell()
# print(h1._Hello__hed)