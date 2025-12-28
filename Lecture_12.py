B = [[1, 2, 4],
     [2, 5, 9],
     [4, 3, 3]]

A = [[1, 2, 4],
     [2, 5, 3],
     [4, 3, 9]]

def is_symmetric(M):
    ''' Return True if M is a symmetric matrix'''
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] != <[j][i]:
                return False
            
    return True

def is_almost_symmetric(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            for il in range(len(M)):
                for jl in range(len(M[0])):
                    M[i][j], M[i][jl] = M[i][jl]
