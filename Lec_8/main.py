import random

class Matrix:
    def __init__(obj, rows, cols):
        obj.rows = rows
        obj.cols = cols
        obj.matrix = [[random.randint(1,50) for col in range(obj.cols)] for row in range(obj.rows)]
        
    def printMatrix(obj):
        for row in obj.matrix:
            print(row) 

    def meanOfMatrix(obj):
        sum = 0
        count = len(obj.matrix)*len(obj.matrix[0])
        for i in range(len(obj.matrix)):
            for j in range(len(obj.matrix[i])):
                sum += obj.matrix[i][j]
        mean=sum/count
        return f"Mean of matrix is {round(mean,2)}"
    
    def sumOfRows(obj,row=0):
        if row>=0 and row<len(obj.matrix):
            return f"Sum of the row {row} is {sum(obj.matrix[row])}"
        return f"Invalid row index"

    def avgOfColumn(obj,col=0):
        sum=0
        if col>=0 and col<len(obj.matrix[0]):
            for row in obj.matrix:
                sum+=row[col]
                avg=sum/(len(obj.matrix))
            return f"Average of column {col} is {round(avg,2)}"
        return f"Invalid column index"

    def print_submatrix(obj, col1,col2,row1,row2):
        submatrix=[]
        for r in range(row1,row2+1):
            sub_row=[]
            for c in range(col1,col2+1):
                sub_row.append(obj.matrix[r][c])
            submatrix.append(sub_row)
        print("Submatrix is")
        for row in submatrix:
            print(row)

matrix=Matrix(3,3)
matrix.printMatrix()
print(matrix.meanOfMatrix())
print(matrix.sumOfRows(2))
print(matrix.avgOfColumn(2))
matrix.print_submatrix(1,2,1,2)