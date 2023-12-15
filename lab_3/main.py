def multiply_matrix_by_vector(matrix, vector):
    matrix_rows = len(matrix)
    matrix_cols = len(matrix[0]) if matrix_rows > 0 else 0
    vector_length = len(vector)

    if matrix_cols == 0:
        raise ValueError('Matrix must have at least one column.')
    if matrix_rows == 0:
        raise ValueError('Matrix must have at least one row.')
    if any(len(row) != matrix_cols for row in matrix):
        raise ValueError('All rows in the matrix must have the same number of columns.')
    if vector_length != matrix_cols:
        raise ValueError('The length of the vector must be equal to the number of columns in the matrix.')

    result = []
    for row in matrix:
        sum = 0
        for a, b in zip(row, vector):
            sum += a * b
        result.append(sum)
    return result


def write_to_file(filename, data):
    with open(filename, 'w') as file:
        for element in data:
            file.write(str(element) + '\n')


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, -11, 12]]
vector = [1, 0, 3]

10
22
34
46

try:
    result = multiply_matrix_by_vector(matrix, vector)
    filename = 'matrix_vector_multiplication.txt'
    write_to_file(filename, result)
    print(f'Result successfully written to {filename}')
except ValueError as e:
    print('Error happened:', str(e))