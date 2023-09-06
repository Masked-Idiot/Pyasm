from sys import argv as prgmargs
lines = []
try:
    file = open(prgmargs[1], "r")
except:
    interact = input()
    while interact.split("!")[0] != "run":
        lines.append(interact)
ram = []
for i in range(64):
    ram.append("")
print(ram)
def arglist(args):
    pass
for line in lines:
    tokens = line.split("!")
    print(tokens)
    if tokens[0] == "var":
        pass
    elif tokens[0] == "lbl":
        pass
    elif tokens[0] == "slc":
        pass
    elif tokens[0] == "say":
        pass
    elif tokens[0] == "end":
        pass
    elif tokens[0] == "inp":
        pass
    elif tokens[0] == "fun":
        pass
    elif tokens[0] == "add":
        pass
    elif tokens[0] == "sub":
        pass
    elif tokens[0] == "mul":
        pass
    elif tokens[0] == "div":
        pass
    elif tokens[0] == "and":
        pass
    elif tokens[0] == "not":
        pass
    elif tokens[0] == "nor":
        pass
    elif tokens[0] == "xor":
        pass
    elif tokens[0] == "equ":
        pass
