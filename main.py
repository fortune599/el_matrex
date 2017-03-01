from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
m2 = [[],[],[],[]]

ident(matrix)
scalar_mult(matrix, 2)
print_matrix(matrix)

i = 2
while (i < 10):
    add_edge(m2, i, i, 0, i * 2, i, 0)
    add_edge(m2, i, i, 0, i, i * 2, 0)
    m2 = matrix_mult(matrix, m2)
    i += 1
add_edge(m2, 0, 0, 0, 500, 500, 0)
add_edge(m2, 10, 0, 0, 500, 256, 0)
add_edge(m2, 0, 10, 0, 256, 500, 0)
i = 0.5
while ( i < 10 ):
    d = i * ((500 - 256) / 10)
    add_edge(m2, int(10 - i), 0, 0, 500, int(256 + d), 0)
    i += 0.5

print_matrix(m2)

draw_lines( m2, screen, color )
display(screen)
save_extension(screen, 'img.png')
