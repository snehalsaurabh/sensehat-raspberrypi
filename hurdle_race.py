from sense_hat import SenseHat
from random import randrange
from time import sleep
sense = SenseHat()

purple = (200,0,139)
orange = [0,200,200]
black=[0 , 0, 0]

matrix = [[orange for column in range(8)] for row in range(8)]

def flatten(matrix):
  
  flattened = [pixel for row in matrix for pixel in row]
  flattened[24]=black
  return flattened

def gen_pipes(matrix):
   for row in matrix:
       row[-1]=purple
   gap = randrange(0,7)
   matrix[gap][-1]=orange
   matrix[gap-1][-1]=orange
   matrix[gap+1][-1]=orange
   return matrix

def move_pipes(matrix):
    for row in matrix:
        for i in range(7):
            row[i] = row[i+1]
        row[-1]=orange
    return matrix

while True:
    matrix = gen_pipes(matrix)
    for event in sense.stick.get_events():
        clear_spot(matrix, x, y)
        if event.direction == 'up':
            y = max(y - 1, 0)
        elif event.direction == 'down':
            y = min(y + 1, 7)
        elif event.direction == 'left':
            x = max(x - 1, 0)
        elif event.direction == 'right':
            x = min(x + 1, 7)
        matrix = move_spot(matrix, x, y)
        sense.set_pixels(flatten(matrix))
    for i in range(10):
        sense.set_pixels(flatten(matrix))
        matrix = move_pipes(matrix)
        sleep(0.1)

matrix = gen_pipes(matrix)
sense.set_pixels(flatten(matrix))
matrix = move_pipes(matrix)
def clear_spot(matrix, x, y):
    matrix[y][x] = orange

def move_spot(matrix, x, y):
    matrix[y][x] = black
    return matrix

x, y = 0, 0
matrix[y][x] = black
sense.set_pixels(flatten(matrix))