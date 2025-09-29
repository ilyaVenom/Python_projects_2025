# var = a container for a vakue(str, in, float, bool)
#   A variable that behaves, as if i was the value it contains
# these are strings:
First_Name = "Ilya"
Food = "donut"
Email = "I_man123@gmail.com"

#next ints:
Age = 35
Quantity = 3
Num_of_Students = 30

# 3rd floats or 
price = 10.99
gpa = 3.2
distance = 5.5

# 4th bools
is_student = False
for_sale= True
is_online = True

if is_online:
    print("You are online")
else:
    print("You are offline")

if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT aviailable")

print(f"Are you a student?:/t {is_student}")

if is_student:
    print("You are a student")
else:
    print("You are NOT a student")


print(f"You are {Age} years old.")
print(f"You are buying {Quantity} items")
print(f"You class has {Num_of_Students} students.")
print(f"The price is ${price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance} Km")
print(f"Hi {First_Name}")
print(f"You like {Food}")
print(f"Your email is: {Email}")