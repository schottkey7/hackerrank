#!/bin/python3

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

for i in range(n - 1, -1, -1):
    print(arr[i], end=' ')
