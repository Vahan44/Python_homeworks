import random
def generate_random_matrix(rows,cols):
    matrix=[]
    for i in range(rows):
        row=[]
        for i in range(cols):
            row.append(random.randrange(1, 100))
        matrix.append(row)
    return matrix 

class Matrix:
    def __init__(self, n, m):
        if n <= 0 or m <= 0:
            raise ValueError('Matrix dimensions n and m must be positive integers.')
        self.rows = n
        self.cols = m
        self.data = generate_random_matrix(n, m)

    def __str__(self):
        return '\n'.join([' '.join(f'{elem:>3}' for elem in row) for row in self.data])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('Matrices must have the same dimensions to add')
        result = Matrix(self.rows, self.cols)
        result.data = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return result

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('Matrices must have the same dimensions to subtract')
        result = Matrix(self.rows, self.cols)
        result.data = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError('The number of columns in the first matrix must be equal'
                             ' to the number of rows in the second matrix')
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
        return result


m1 = Matrix(2, 3)
print('Matrix1:')
print(m1)

m2 = Matrix(3, 2)
print('Matrix2:')
print(m2)

m3 = m1 * m2
print('Multiplied Matrices:')
print(m3)

m4 = Matrix(2, 3)
print('Matrix4:')
print(m4)

m5 = m1 + m4
print("Added Matrices (1 and 4):")
print(m5)

m6 = m1 - m4
print("Subtracted Matrices (1 and 4):")
print(m6)