print("Binary to Decimal")
binary_input = input("Enter binary number: ")
binary = int(binary_input)
power = 0
decimal = 0
is_valid = True

for char in binary_input:
    if char not in '01':
        is_valid = False
        break

while binary > 0:
    digit = binary % 10
    decimal = decimal + digit * (2 ** power)
    power = power + 1
    binary = binary // 10

print("Decimal value:", decimal)

if not is_valid:
    print("Invalid binary number")
else:
    print("Valid binary")

if decimal % 2 == 0:
    print("Even decimal")
else:
    print("Odd decimal")