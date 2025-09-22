
def input_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    # Take input for each row of the matrix
    print("Enter the matrix row by row (space-separated values):")
    for i in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            print(f"Error: Row {i + 1} does not have {cols} elements.")
            return None
        matrix.append(row)

    return matrix

def transpose_matrix(matrix):
    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Initialize the transposed matrix with dimensions cols x rows
    transposed = []

    for i in range(cols):
       new_row = []
       for j in range(rows):
          new_row.append(0)
       transposed.append(new_row)

    # Loop through the matrix and swap rows with columns
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed

matrix = input_matrix()

if matrix:
    transposed = transpose_matrix(matrix)

    print("Transposed matrix:")
    for row in transposed:
        print(row)


