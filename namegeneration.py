import numpy as np
import pandas as pd
import torch

words = open('names.txt', 'r').read().splitlines()
print(words[:3])

def countword():
    for i in words[:3]:
        ch="."+i
        ch2=i+"."
        for wr1,wr2 in zip(ch,ch2):
            print(wr1,wr2)

countword()