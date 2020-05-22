def lcs_table(x, y):
    lcs = [ [0] * (len(y) + 1) for _ in range(len(x) + 1)]
    
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            if x[i-1] == y[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

    return lcs

def reconstruct_lcs(x, y, lcs, i=None, j=None):
    if i is None:
        i = len(x)
    if j is None:
        j = len(y)
    
    if i == 0 or j == 0:
        return ''

    if x[i-1] == y[j-1]:
        return reconstruct_lcs(x, y, lcs, i-1, j-1) + x[i-1]

    if lcs[i-1][j] > lcs[i][j-1]:
        return reconstruct_lcs(x, y, lcs, i-1, j)
    
    return reconstruct_lcs(x, y, lcs, i, j-1)

def lcs(x, y):
    table = lcs_table(x, y)
    return reconstruct_lcs(x, y, table)