import builtins
n = 3
v = float(3)
def print(inputs = list[str]):
    input = " ".join(str(string) for string in inputs)
    builtins.print(input, sep="\n",end="!\n",flush=True)
print([n, v])
if n == v:
    print(["Yup"])