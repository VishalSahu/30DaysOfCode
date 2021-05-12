#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
numberOfSwaps = 0
for i in range(0,n):
    for j in range(0,n-1):
        temp=0
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1]=temp
            numberOfSwaps +=1
print("Array is sorted in "+str(numberOfSwaps)+" swaps.")
print("First Element:",a[0])
print("Last Element:",a[n-1])
