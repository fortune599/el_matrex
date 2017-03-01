import math

def print_matrix( matrix ):
    roah = ""
    for row in matrix:
        for coord in row:
            roah += str(coord) + ","
        roah += "\n"
    print roah
    return

def ident( matrix ):
    for i in range( len(matrix) ):
        for j in range( len(matrix[i]) ):
            if (i == j):
                matrix[i][j] = 1
            else: matrix[i][j] = 0
    return matrix

def scalar_mult( matrix, s ):
    for i in range( len(matrix) ):
        for j in range ( len(matrix[i]) ):
            matrix[i][j] *= s
    return matrix

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m3 = new_matrix( len(m2[0]), len(m1) )
    for i in range( len(m1) ):
        for j in range( len(m2[0]) ):
            for k in range( len(m2) ):
                m3[i][j] += m1[i][k] * m2[k][j]
    return m3

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
