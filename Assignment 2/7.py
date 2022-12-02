
birthyear = 2001
def take3(name,bithyear,weight):
    today = 2022
    age = today-birthyear
    print("Your age is", age )
    return age 

name = str(input("What is your name?"))
if name == "":
    name = "Timothy"
weight = int(input("What is your weight?"))
             
print("you are", name, "your weight is", weight)