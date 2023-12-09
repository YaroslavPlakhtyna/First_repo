# НСД (gcd) - найбільший спільний дільник
first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

gcd = min(first, second)
while not (first % gcd == 0 and second % gcd == 0):
    gcd -= 1

print (gcd)