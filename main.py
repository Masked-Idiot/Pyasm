from sys import argv as args
file = open(args[1], "r")
for line in file.readlines():
    print(line.split("!"))
