# if  Do some code of if some condition is True
#    Else do something else
# and order of positioning for the if-statements matter too.
# 
#  

Age = int(input("Enter your age: "))

if Age >= 100:
    print("You are too old to sign up!")

elif Age >= 18:
    print("You are now signed up!")
elif Age < 0:
    print("You have not been born yet!")
    
else:
    print("You must be 18 or older to sign up!")

# otherwise an exercise asking if a user wants some food:
'''
reponse = input("Would you like some food? (Y/N): ")

if reponse == "Y":
    print("Have some food!")
else:
    print("No food for you!")
'''
# 3rd exercise focusing on name gathering:
'''
name = input("Enter your name: ")

if name == "":
    print("You did not type your name!")
else:
    print(f"Hi {name}!")
'''
# next reviewing bools
online = False

if online:
    print("The user is online!")
else:
    print("The use is offline!")