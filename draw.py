from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    i = 0
    while (i < len(matrix[0])):
        draw_line(matrix[0][i], matrix[1][i], matrix[0][i+1], matrix[1][i+1], screen, color)
        i += 2
    return

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0 )
    return add_point( matrix, x1, y1, z1 )

def add_point( matrix, x, y, z=0 ):
    matrix[0].append(x)
    matrix[1].append(y)
    matrix[2].append(z)
    matrix[3].append(1)
    return matrix

def draw_line( x0, y0, x1, y1, screen, color ):
  x = x0
  y = y0
  x2 = x1
  y2 = y1
  B = x - x2
  if ( B == 0 ):
    B = -1
  slope = -float(y2 - y) / B
  if (B > 0):
    x = x1
    y = y1
    x2 = x0
    y2 = y0
  A = y2 - y
  B = x - x2
  #print("x0 " + str(x) + " x1 " + str(x1))
  if ( slope > 1 ):
    return drawline_q2( x, y, x2, y2, screen, color, A, B )
  elif ( slope > 0 ):
    return drawline_q1( x, y, x2, y2, screen, color, A, B )
  elif ( slope < -1 ):
    return drawline_q7( x, y, x2, y2, screen, color, A, B )
  else:
    return drawline_q8( x, y, x2, y2, screen, color, A, B )

def drawline_q1( x, y, x1, y1, screen, color, A, B ):
  d = 2 * A + B
  while ( x <= x1 ):
    plot( screen, color, x, y )
    if (d > 0):
      y+=1
      d += 2 * B
    x+=1
    d += 2 * A
  return True

def drawline_q2( x, y, x1, y1, screen, color, A, B ):
  d = A + 2 * B
  while ( y <= y1 ):
    plot( screen, color, x, y )
    if (d < 0):
      x+=1
      d += 2 * A
    y+=1
    d += 2 * B
  return True

def drawline_q7( x, y, x1, y1, screen, color, A, B ):
  d = A - 2 * B
  while ( y >= y1 ):
    plot( screen, color, x, y )
    if (d > 0):
      x+=1
      d += 2 * A
    y-=1
    d -= 2 * B
  return True

def drawline_q8( x, y, x1, y1, screen, color, A, B ):
  d = 2 * A + B
  while ( x <= x1 ):
    plot( screen, color, x, y )
    if (d < 0):
      y-=1
      d -= 2 * B
    x+=1
    d += 2 * A
  return True
