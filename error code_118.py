print("Binary to Decimal")

binary = int(input("Enter binary number: "))

power = 0
decimal = 0

while binary > 0:
    digit = binary % 10
    decimal = decimal + digit * (2 ** power)
    power = power + 1

    binary = binary // 10

print("Decimal value:", decimal)

if digit > 1:
    print("Invalid binary number")
else:
    print("Valid binary")

if decimal % 2 == 0:
    print("Even decimal")
else:
    print("Odd decimal")