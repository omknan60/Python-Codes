#!/bin/python3

import os
import sys

#
# Complete the circularPalindromes function below.
#
def circularPalindromes(n, s):
    result = []
    def check(new):
        s = 0
        for i in range(n):
            for j in range(n):
                if new[i:j] == new[j:i:-1]:
                    if j - i > s:
                        s = j - i + 1
        return s
    for i in range(n):
        new = s[i:]+ s[:i]
        result.append(check(new))
    return result
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = circularPalindromes(n, s)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
