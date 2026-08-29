import numpy as np

class matrix_op:
    def __init__(self,matrix_1,matrix_2):
        self.matrix_1=matrix_1
        self.matrix_2=matrix_2
    def multiplie_matrix(self):
        return np.matmul(self.matrix_1,self.matrix_2)

m1=matrix_op([[1, 2, 3],[4, 5, 6]],[[7, 8],[9, 10],[11, 12]])
print(m1.multiplie_matrix())