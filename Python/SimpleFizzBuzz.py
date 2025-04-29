uInput = int(input("What number would you like to go up to? "))
for number in range(1, uInput + 1):
    output = ""
    if number % 3 == 0:
        output += "Fizz"
    if number % 5 == 0:
        output += "Buzz"
    if output == "":
        output = str(number)
    print(output)
