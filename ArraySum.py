'''
Problem
You are given an array A consisting of N integers.

Task
Print the sum of the elements in the array.
'''
name = input()
n = input()
a = n.split()
total = 0

for i in range(len(a)):
    total += int(a[i])

print(total)
