def formulas(n):
    # pad size
    size = n + 1
    #create zero-filled matrix
    matrix = [[0 for _ in xrange(size)] for _ in xrange(size)]
    
    #base value is always padded and skipped
    matrix[0][0] = 1
    for i in xrange(1, size):
        for j in xrange(0, size):
            matrix[i][j] = matrix[i - 1][j]
            if j >= i:
                matrix[i][j] += matrix[i - 1][j - i]
    return matrix[n][n] - 1

def solution(n):
    # Your code here
    return formulas(n)

    