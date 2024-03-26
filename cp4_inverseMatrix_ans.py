def determinant(mat):
    return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
def inverse_matrix(det, mat):
    if det == 0:
        return None
    else:
        #new_mat = [[round(mat[1][1] / det, 3), round(-1 * mat[0][1] / det, 3)],
                #[round(-1 * mat[1][0] / det, 3), round(mat[0][0] / det, 3)]]
        new_mat = [[mat[1][1] / det, -1 * mat[0][1] / det],
                [-1 * mat[1][0] / det, mat[0][0] / det]]
        for i in range(2):
            for j in range(2):
                new_mat[i][j] = round(new_mat[i][j], 3)
        return new_mat
        
def main():
    matrix = [[1,2],
              [6,5]]
    det = determinant(matrix)
    inv = inverse_matrix(det, matrix)
    print(inv)

if __name__ == "__main__":
    main()