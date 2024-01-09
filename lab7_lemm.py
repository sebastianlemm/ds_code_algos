def printMatrix(m):
    for row in m:
        print(row)

def chainMatrix(dims):
    # Create the empty 2D table
    n = len(dims)-1
    m = [[0 for _ in range(n)] for _ in range(n)]
    s = [[0 for _ in range(n)] for _ in range(n)]  # Trace-back table

    # Fill in the base case values
    for i in range(n):
        m[i][i] = 0

    # Fill in the rest of the table diagonal by diagonal
    for chainLength in range(2, n+1):
        for i in range(n+1-chainLength):
            j = i + chainLength - 1
            m[i][j] = float("inf")
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + dims[i]*dims[k+1]*dims[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k  

    print("Optimal cost matrix:")
    printMatrix(m)
    print("Trace-back table:")
    printMatrix(s)
    return m, s

def parenStr(s, start, end):
    if start == end:
        return f"A{start}"
    else:
        k = s[start][end]
        return "(" + parenStr(s, start, k) + parenStr(s, k+1, end) + ")"

dims = [30, 35, 15, 5, 10, 20, 25]
m, s = chainMatrix(dims)
optimal_parentheses = parenStr(s, 0, len(dims)-2)  
print("Optimal multiplication order:")
print(optimal_parentheses)

