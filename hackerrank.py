#!/bin/python3

import os
import sys

#
# Complete the buildPalindrome function below.
#
def buildPalindrome(c,b):
    len_c = len(c)
    len_b = len(b)
    l_c = []
    l_b = []
    for i in range(len_c):
        z = 1
        while True:
            if z + i > len_c:
                break
            l_c.append(c[i:i+z])
            z += 1
    for i in range(len_b):
        z = 1
        while True:
            if z + i > len_b:
                break
            l_b.append(b[i:i+z])
            z += 1

    sol = ""

    for i in l_c:
        for j in l_b:
            d = ""
            if i + j == (i + j)[::-1]:
                d += i + j
            if len(d) > len(sol):
                sol = d

    if sol == "":
        print("-1")
    else:
        print(sol + "\n")


t = int(input())

for t_itr in range(t):
    c = input()

    b = input()

    result = buildPalindrome(c, b)
