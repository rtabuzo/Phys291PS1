import numpy as np
import sys

input1 = sys.argv[1]
input2 = sys.argv[2]

A = np.loadtxt(input1)
B = np.loadtxt(input2)

result = [[0, 0], [0, 0]]

for i in range(len(A)):
	for j in range(len(B[0])):
		for k in range(len(B)):
			result[i][j] += A[i][k]*B[k][j]

for r in result:
	print(r)
