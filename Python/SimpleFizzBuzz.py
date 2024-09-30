number = 1
uInput = int(input("What number would you like to go up to?"))
while number <= uInput:
  if number%15 == 0:
    print("FizzBuzz")
  elif number%3 == 0:
    print("Fizz")
  elif number%5 == 0:
    print("Buzz")
  else:
    print(number)
  number += 1
