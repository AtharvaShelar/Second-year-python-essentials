#assignment 6
while True:
    password = input("Enter password: ")

    if password == "stop":
        break

    length = len(password) >= 8
    upper = any(i.isupper() for i in password)
    lower = any(i.islower() for i in password)
    digit = any(i.isdigit() for i in password)

    if length and upper and lower and digit:
        print("Strong password")
    else:
        print("Weak password")