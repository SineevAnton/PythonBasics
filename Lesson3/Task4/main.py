# The program accepts a real positive number x and a negative integer y.
# Perform the exponentiation of the number x to the power of y.
# Implement the task as a function my_func(x, y).
# When solving a task, you need to do it without the built-in exponentiation function.

number = float(input("Enter a positive Real number: "))
powNumber = int(input("Enter an integer negative number: "))

def my_func(x, y):
    result1 = x ** y
    print(f"Answer using **: {result1:.5f}")
    result2 = 1
    for _ in range(y, 0, 1):
        result2 = result2 * (1 / x)
    print(f"Answer using for-loop: {result2:.5f}")
    return result1

my_func(number, powNumber)