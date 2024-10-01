hexadecimal = ["0",0,"0000","1",1,"0001","2",2,"0010","3",3,"0011","4",4,"0100","5",5,"0101","6",6,"0110","7",7,"0111","8",8,"1000","9",9,"1001","A",10,"1010","B",11,"1011","C",12,"1100","D",13,"1101","E",14,"1110","F",15,"1111"]
hexnum = input("Enter a hex number:")
binarynum = ""
denarynum = 0
v = 0
while v < len(hexnum):
    i = 0
    while i <= 15:
        if hexadecimal[i*3] == hexnum[v]:
            binarynum += hexadecimal[i*3+2]
            denarynum += hexadecimal[i*3+1]*(16**(len(hexnum)-(v+1)))
        i+=1
    v+=1
print("Binary: "+binarynum+"\n"+"Denary: "+str(denarynum))
