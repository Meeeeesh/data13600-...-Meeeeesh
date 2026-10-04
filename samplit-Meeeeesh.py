import random
import fileinput

for line in fileinput.input():
    if random.random() < 0.01:
        print(line, end="")
