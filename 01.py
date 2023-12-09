# password, username
# admin and guest
# alt+shift+up/down

username =input("Enter please your username")
password = input("Enter please your password")

if username == "admin":
    if password == "qwerty":
        print("Login successful! Welcomne admin!")
    elif password == "12345":
        print("Weak password! Change it immediaely")
    else:
        print("Incorrect password")

