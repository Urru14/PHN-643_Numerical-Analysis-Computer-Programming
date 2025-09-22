def lst_input(name):
    
    rows = int(input(f"Enter number of rows for matrix {name}: "))
    cols = int(input(f"Enter number of columns for matrix {name}: "))
    
    print(f"Enter the elements of matrix {name}, row by row:")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = float(input(f"Element [{i+1}, {j+1}]: "))
            row.append(value)
        matrix.append(row)
    
    return matrix

def add_lst(A, B):
    
    rows = len(A)
    cols = len(A[0])
    
    result = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j] + B[i][j]
    
    return result

def multiply_lst(A, B):
    
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    
    if cols_A != rows_B:
        raise ValueError("Incompatible matrices for multiplication")
    
    result = [[0] * cols_B for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(cols_A))
    
    return result



print("Input for Matrix A")
A = lst_input("A")
print (A)
    
print("\nInput for Matrix B")
B = lst_input("B")
print (B)   
# Check if matrices can be added
if len(A) == len(B) and len(A[0]) == len(B[0]):
        sum_matrix = add_lst(A, B)
        print("\nSum of A and B:")
        print(sum_matrix)
else:
        print("\nMatrices A and B cannot be added due to incompatible dimensions.")

# Check if matrices can be multiplied
if len(A[0]) == len(B):
        product_matrix = multiply_lst(A, B)
        print("\nProduct of A and B:")
        print(product_matrix)
else:
        print("\nMatrices A and B cannot be multiplied due to incompatible dimensions.")
