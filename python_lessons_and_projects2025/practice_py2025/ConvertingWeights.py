# Converting weights in Python

weight = float(input("Enter your weight: "))
# An improvement to handle case-sensitive for caps or not below:
unit = input("Kilograms or Pounds? (Kg or Lb): ").strip().lower()

def convert_weight():
    try:
        weight = float(input("Enter your weight: "))
        unit = input("Kilograms or Pounds? (Kg or Lb): ").strip().lower()

        if unit == "kg":
            converted = weight * 2.205
            print(f"Your weight is: {round(converted, 1)} Lbs.")
        elif unit == "lb":
            converted = weight / 2.205
            print(f"Your weight is: {round(converted, 2)} Kgs.")
        else:
            print(f"'{unit}' is not valid. Please enter 'Kg' or 'Lb'.")
    except ValueError:
        print("Invalid input. Please enter a number for weight.")

convert_weight()

while True:
    convert_weight()
    again = input("Convert another? (y/n): ").strip().lower()
    if again != 'y':
        break

else:
    print(f"{unit} was not valid. Try again!")