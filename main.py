from sys import argv as args
file = args[0]
def parse(line):
    tokens = []
    tokens.append(line.split("!")[0])
    tokens.append(line.split("!")[1])
    return tokens
print(parse("put! 0"))