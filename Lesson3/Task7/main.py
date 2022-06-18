# The program should include a string of words separated by a space.
# Each word consists of lowercase Latin letters. You need to output the original string,
# but each word must begin with a capital letter. Use the previously written int_func() function.

def int_func(text):
    return text.capitalize()

def CapitalizeString():
    print("Please enter a string:")
    str = input().split()
    for i in range(len(str)):
        str[i] = int_func(str[i])
    return " ".join(str)

print(CapitalizeString())