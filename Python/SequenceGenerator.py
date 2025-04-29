depth = int(input("Enter the depth of the sequence: "))
options = ["U", "D", "L", "R"]
sequences = {}
for i in range(4**depth):
    sequence = []
    for _ in range(depth):
        sequence.append(options[i % 4])
        i //= 4
    sequences["".join(sequence)] = 0
