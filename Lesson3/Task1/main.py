# Task 1.
# Create a function that accepts two numbers (positional arguments) and performs their division.
# Get numbers from the user input. Provide the processing of the situation of division by zero.

devisible = float(input("Please, enter the divisible: "))
devider = float(input("Please, enter the devider: "))

# Function 'Devide' accepts two float arguments (devis, devid) and prints
# and print the result of devision 'devis' by 'devid', or print error
# if 'devid' equals 0

def Devide(devis, devid):
    if devid == 0:
        print("Error: devision by zero unsupported.")
    else:
        print(f"Answer is: {(devis / devid):.3f}")

Devide(devisible, devider)