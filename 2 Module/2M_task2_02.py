is_active = input("Is the user active? ")
if is_active == "yes":
    user = True
else:
    user = False

is_admin = input("Is the user administrator? ")
if is_admin == "yes":
    is_admin = True
else:
    is_admin = False

is_permission = input("Does the user have access? ")
if is_permission == "yes":
    is_permission = True
else:
    is_permission = False

access = 