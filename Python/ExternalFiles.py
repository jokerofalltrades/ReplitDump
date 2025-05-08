with open("Python/example.txt", "wt") as myFile:
    myFile.write("I have written to a file.\n")
    myFile.write("It now has 3 lines.\n")
    myFile.write("The third being this one.\n")
with open("Python/example.txt", "a") as myFile:
    myFile.write("PS here is another line I forgot to add.\n")
with open("Python/example.txt","rt") as myFile:
    contents = myFile.read()
    print(contents)