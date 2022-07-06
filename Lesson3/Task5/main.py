# The program asks the user for a string of numbers separated by a space.
# When you press Enter, the sum of the numbers should be displayed.
# The user can continue entering numbers separated by a space and press Enter again.
# The sum of the newly entered numbers will be added to the already calculated amount.
# But if a special character is entered instead of a number, the program execution ends.
# If a special character is entered after several numbers,
# then first you need to add the sum of these numbers to the amount received earlier and then terminate the program.

# Special symbol to stop is 'e'

def getNumbersSum():
    resultSum = 0
    print("Enter numbers using space as separator.")
    print("Enter 'e' to stop the program.")
    while True:
        inputString = input()
        if  inputString[-1] == 'e':
            resultSum += sum([float(i) for i in inputString[:len(inputString) - 1].split()])
            print(f"Current sum is: {resultSum}")
            break
        else:
            resultSum += sum([float(i) for i in inputString.split()])
        print(f"Current sum is: {resultSum}")

getNumbersSum()