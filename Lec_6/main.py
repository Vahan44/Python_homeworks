import random

def generate_random_matrix(rows,cols):
    matrix=[]
    for i in range(rows):
        row=[]
        for i in range(cols):
            row.append(random.randrange(1, 100))
        matrix.append(row)
    return matrix 
   

def get_column_sum(matrix, col_index):
    sum=0
    if 0 <= col_index < len(matrix[0]):
        for row in matrix:
            sum += row[col_index]
        return f"Sum of column {col_index} is {sum}"
    else:
       return "Invalid column index."


def get_row_average(matrix,row_index):
    avg = 0
    if 0 <= row_index < len(matrix):
        row=matrix[row_index]
        avg = sum(row)/2
        return f"Average of row {row_index} is {avg}"
    else:
       return "Invalid row index."
    
matrix = generate_random_matrix(3,4)

print(matrix)

print(get_column_sum(matrix, 3))

print(get_row_average(matrix, 2))
