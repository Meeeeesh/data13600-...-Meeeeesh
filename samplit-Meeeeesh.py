import random
import fileinput
import numpy as np

for line in fileinput.input():
    if random.random()<0.01:
        print(line, end="")
