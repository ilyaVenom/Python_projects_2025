# covering math operators again
# adding
# friends = friends + 1
# an augmented style:
# friends += 1
#friends = 10
# subtracting style:

#friends -= 2
# multiplying way:
#friends *= 3
# division way
#friends /= 2
# or an exponent way:
#friends **= 2
# next a modulos topic:
#remainder = friends % 3

#print(remainder)
# basics covered next are more examples:

#x = 3.14
#y = 4
#z = 5

#result = round(x)
#result = abs(y)
#result = pow(4, 3)
#result = max(x, y, z)
#result = min(x, y, z)

#print(result)
# section 2: 
#import math
#x = 63.9
# useful for physics

#print(math.pi)
#print(math.e)
#result = math.sqrt(x)
#result = math.ceil(x)
#result = math.floor(x)

#print(result)
# next use the math to determine the circumfernce of a cirle:
# C = 2*pi*r
''' This was ex. 1
import math

radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius
print(f"The circumference is : {round(circumference,3)} in cm.")
'''
# ex 2: area of a circle:
'''
import math
# area = pi * r ** 2
radius = float(input("Enter a radius of a circle in cm: "))

Area = math.pi * pow(radius,2)
print(f"The area of the circle is: {round(Area,2)}cm^2")
'''
# ex 3: find hypothnesis: of right triangle
# c = sqrt(a^2 + b^2)
import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The hypothnes is {round(c,2)} cm:")
