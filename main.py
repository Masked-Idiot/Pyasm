from sys import argv as args
file = open(args[1], "w")
for line in file.readlines():
    print(line.split("!"))