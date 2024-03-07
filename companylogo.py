#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
alphas=[]
nums=[]
for i in set(s):
    alphas.append((i,s.count(i)))
final_l=sorted(alphas, key=lambda x: (-x[1],x[0]) )
for i in final_l[0:3]:
    for j in i:
        print(j,end=' ')
    print()
