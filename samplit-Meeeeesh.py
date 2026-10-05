import random
import fileinput
import matplotlib.pyplot as plt

for line in fileinput.input():
    if random.random()<0.01:
        print(line, end="")
    else:
        pass
