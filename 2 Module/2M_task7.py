num = int(input("Enter the integer (0 to 100): "))
sum = 0
current_number = 1

while current_number <= num:
    sum += current_number
    current_number += 1
print(f"{num}, {sum}")