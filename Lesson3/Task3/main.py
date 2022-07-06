# Create the my_func() function, which takes three positional arguments
# and returns the sum of the largest two arguments.

def my_func(num1, num2, num3):
    numbers = [num1, num2, num3]
    return sum(numbers) - min(numbers)

print(my_func(5, 10, 5))

# In case when we can't use built-in functions we can use if-else structure, example:
# if num1 <= num2 and num1 <= num3
# sum = num2 + num3
# and do it for each number