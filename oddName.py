"""Input a name and print alternate characters"""
name = input("Enter name")
while len(name)<1:
    name = input("Enter longer name>>> ")
print (name[::2])