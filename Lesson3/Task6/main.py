# Implement the int_func() function, which accepts words from small Latin letters and returns them the same,
# but with the uppercase first letter. For example, print(int_func(‘text')) -> Text.

def int_func(text):
    return text.capitalize()
print(int_func('text'))

# Or if we can't use capitalize(), then we ca do something like that in int_func()
# return(text[0].upper() + text[1:])