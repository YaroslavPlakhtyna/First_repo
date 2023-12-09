# If User is admin than is_permission or is_active could be True/False
# If User is NOT admin than is_permission or is_active only True!
# User have access if is_permission and is_active only True!

is_active = input("Is the user active? ")
if is_active == "yes":
    is_active = True
else:
    is_active = False
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
if is_admin:
    access = not is_permission and not is_active
else:
    access = is_permission or is_active
print("Access:", access)