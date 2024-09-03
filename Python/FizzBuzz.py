number = 1
numbera = 3
numberb = 5
numberc = 15
totalmultiples = 0
times3tables = [3,]
times5tables = [5,]
times15tables = [15,]
while numbera <= 999:
  numbera = numbera + 3
  times3tables.append(numbera)
while numberb <= 999:
  numberb = numberb + 5
  times5tables.append(numberb)
while numberc <= 999:
  numberc = numberc + 15
  times15tables.append(numberc)
while number <= 1000:
  if times15tables.__contains__(number):
    print("FizzBuzz")
    totalmultiples += number
  elif times3tables.__contains__(number):
    print("Fizz")
    totalmultiples += number
  elif times5tables.__contains__(number):
    print("Buzz")
    totalmultiples += number
  else:
    print(number)
  number += 1

print(totalmultiples)
