work_experience = int(input("Enter your full work experience in years: "))

if work_experience >= 2 and work_experience <= 5:
    developer_type = "Middle"
elif work_experience <= 1:
    developer_type = "Junior"
elif work_experience >= 5:
    developer_type = "Senior"

print (developer_type)