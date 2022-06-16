#Tomas Vera
#grid_helper.py

def compress(grid):
    new_grid = []
    for i in range(4):
        new_grid.append([0] * 4)
    for i in range(4):
        pos = 0
        for j in range(4):
            if(grid[i][j] != 0):
                new_grid[i][pos] = grid[i][j]           
                pos += 1
    return new_grid
 
def merge(grid):
    for i in range(4):
        for j in range(3):
            if(grid[i][j] == grid[i][j + 1] and grid[i][j] != 0):
                grid[i][j] = grid[i][j] * 2
                grid[i][j + 1] = 0
    return grid

def reverse(grid):
    new_grid =[]
    for i in range(4):
        new_grid.append([])
        for j in range(4):
            new_grid[i].append(grid[i][3 - j])
    return new_grid

def transpose(grid):
    new_grid = []
    for i in range(4):
        new_grid.append([])
        for j in range(4):
            new_grid[i].append(grid[j][i])
    return new_grid
 
def move_left(grid):
    new_grid = compress(grid)
    new_grid = merge(new_grid)
    new_grid = compress(new_grid)
    return new_grid

def move_right(grid):
    new_grid = reverse(grid)
    new_grid = move_left(new_grid)
    new_grid = reverse(new_grid)
    return new_grid

def move_up(grid):
    new_grid = transpose(grid)
    new_grid = move_left(new_grid)
    new_grid = transpose(new_grid)
    return new_grid
 
def move_down(grid):
    new_grid = transpose(grid)
    new_grid = move_right(new_grid)
    new_grid = transpose(new_grid)
    return new_grid
 
def move(grid, code):
    if code == 0:
        return move_up(grid)
    elif code == 1:
        return move_down(grid)
    elif code == 2:
        return move_left(grid)
    elif code == 3:
        return move_right(grid)
    else:
        return grid

def largest_num(grid):
    max = 0
    for i in range(4):
        for j in range(4):
            if(grid[i][j] > max):
                max = grid[i][j]
    return max

def sum_grid(grid):
    sum = 0
    for i in range(4):
        for j in range(4):
            sum += grid[i][j]
    return sum

def count_empty(grid):
    count = 0
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                count += 1
    return count

def print_grid(grid):
    print("--------")
    for i in range(4):
        for j in range(4):
            print(grid[i][j], end=' ')
        print()
    print("--------")

