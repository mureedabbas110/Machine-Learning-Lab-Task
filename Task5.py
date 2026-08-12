import numpy as np
 
matrix = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
print('Shape:', matrix.shape)
print('Row 0:', matrix[0])
print('Column 1:', matrix[:, 1])
print('Transpose:\n', matrix.T)
print('Row sums:', matrix.sum(axis=1))
print('Column sums:', matrix.sum(axis=0))
 
zeros = np.zeros((2, 4))
ones = np.ones((2, 4))
seq = np.arange(0, 10, 2)
print(zeros, ones, seq, sep='\n')
