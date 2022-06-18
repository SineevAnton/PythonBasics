# Perform a function that accepts several parameters describing the user's data:
# first name, last name, year of birth, city of residence, email, phone.
# The function must accept parameters as named arguments. Output user data in one line.

def ShowUserData(name, surname, birthYear, city, email, phone):
    print(f"User: {surname} {name}, {birthYear} year birth, live in {city}, contacts: email: {email}; phone: {phone}")

ShowUserData(name="User", city="Linux", email="root@root", surname="Root", birthYear=1791, phone="+9999")