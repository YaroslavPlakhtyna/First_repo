is_active = input("Is the user active? ")
is_admin = input("Is the user administrator? ")
is_permission = input("Does the user have access? ")

is_active = bool(is_active)
is_admin = bool(is_admin)
is_permission = bool(is_permission)

access = bool(is_admin) or (bool(is_active)) and bool(is_permission)
print(access)