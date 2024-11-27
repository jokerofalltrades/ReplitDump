number = 1
uInput = int(input("What number would you like to go up to?"))
for number in range(uInput):
    output = ""
    if number % 3 == 0:
        output += "Fizz"
    if number % 5 == 0:
        output += "Buzz"
    if output == "":
        output = str(number)
    print(output)
    number += 1
