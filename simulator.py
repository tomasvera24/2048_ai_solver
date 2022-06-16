#0 means UP, 1 means DOWN, 2 means LEFT, 3 means RIGHT, 4 means QUIT GAME

import grid_helper
import random
import search
import time
import turtle

turtle.colormode(255)
# Set up the screen
wn = turtle.Screen()
wn.title("2048 AI Solver")
wn.bgcolor(250, 248, 239)
wn.setup(width=600, height=600)
wn.tracer(0)

# Score
score = 0

box = turtle.Turtle()
box.speed(0)
box.shape("square")
box.color((119, 110, 101))
box.penup()
box.hideturtle()
box.turtlesize(stretch_wid=18, stretch_len=18, outline=18)

score = turtle.Turtle()
score.speed(0)
score.penup()
score.hideturtle()

box.goto(0, -65)
box.stamp()

box.turtlesize(stretch_wid=4, stretch_len=4, outline=4)

box.goto(0, 230)
box.color((119, 110, 101))
box.write("2048", align="center", font=("Courier", 50, "bold"))

def draw_grid():
    colors = {
        0: (204, 192, 179),
        2: (238, 228, 218),
        4: (237, 224, 200),
        8: (242, 177, 121),
        16: (245, 149, 99),
        32: (246, 124, 95),
        64: (246, 94, 59),
        128: (237, 207, 114),
        256: (237, 204, 97),
        512: (237, 200, 80),
        1024: (237, 197, 63),
        2048: (237, 194, 46),
        4096: (218,112,214),
        8192: (0,250,154)
    }

    score.goto(0, 180)

    score.color((119, 110, 101))
    score.write("Number of moves: " + str(step), align="center", font=("Courier", 26, "bold"))
    grid_y = 0
    y = 160
    for row in grid:
        grid_x = 0
        x = -225
        y -= 90
        for column in row:
            x += 90
            box.goto(x, y)
            
            value = grid[grid_y][grid_x]
            color = colors[value]

            box.color(color)
            box.stamp()

            box.color((119, 110, 101))
            if column == 0:
                number = ""
            else:
                number = str(column)

            box.sety(box.ycor() - 14)
            box.write(number, align="center", font=("Courier", 26, "bold"))
            box.sety(box.ycor() + 14)

            grid_x += 1
        
        grid_y += 1
    score.clear()


def decision(probability):
    return random.random() < probability

grid = [[0,0,0,0],
        [0,2,0,0],
        [0,0,2,0],
        [0,0,0,0]]

print("starting timer")
start_time = time.time()

""" 
grid = [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
x1 = random.randint(0, 3)
y1 = random.randint(0, 3)
x2 = random.randint(0, 3)
y2 = random.randint(0, 3)
while(grid[x2][y2] != 0):
    x2 = random.randint(0, 3)
    y2 = random.randint(0, 3)

grid[x1][y1] = 2
grid[x2][y2] = 2
 """
step = 0
while True:
    
    
    grid_helper.print_grid(grid)
    draw_grid()
    print(step)
    print("--- %s seconds ---" % (time.time() - start_time))
    move = search.NextMove(grid,step)

    if move == 4:
        print("done")
        break
    grid = grid_helper.move(grid, move)
    
    x = random.randint(0, 3)
    y = random.randint(0, 3)
    if grid_helper.count_empty(grid) != 0:
        while(grid[x][y] != 0):
            x = random.randint(0, 3)
            y = random.randint(0, 3)
    else:
        print("done")
        break
    if decision(0.9):
        grid[x][y] = 2
    else:
        grid[x][y] = 4
    
    step += 1



