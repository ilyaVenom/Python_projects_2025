# type casting = The process of converting a value of one data type to another
#                          (string, integer, float, boolean)
#                          Explicit vs Implicit

name = "Ilya"
age = 35
gpa = 2.5
student = True

# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(student)) 

age = int(age)
print(age)

gpa = float(gpa)
print(gpa)

student = str(student)
print(student)

name = (name)
print(name)