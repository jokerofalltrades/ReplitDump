def _3n1(n):
    numofsteps = 0
    while n != 1:
        if n % 2 == 1:
            n = n * 3 + 1
        else:
            n /= 2
        numofsteps += 1
    return numofsteps

i = 1
highestsequence = 1
highestnumber = 1
while i <= 100000:
    print(f"{i}: {_3n1(i)}")
    i += 1

# v = int(input("What num would you like to calculate?"))
# print(f"{v}: {_3n1(v)}")