#MP2 Tomas Vera
#search.py

#0 means UP, 1 means DOWN, 2 means LEFT, 3 means RIGHT, 4 means QUIT GAME

import grid_helper

def heuristic(grid):
    weights = [1,0.3,100]
    order_sum = 0
    largest_num = 0
    empty_count = 0
    heuristic_grid = [[1,1,1,1],
                    [2,2,2,2],
                    [3,3,3,3],
                    [4,4,4,4]]
    for i in range(4):
        for j in range(4):
            order_sum += grid[i][j] * heuristic_grid[i][j]
            if(grid[i][j] > largest_num):
                largest_num = grid[i][j]
            if grid[i][j] == 0:
                empty_count += 1
            
    return (weights[0]*largest_num)+(weights[1]*order_sum)+(weights[2]*empty_count)

def calc_cost(grid):
    return heuristic(grid)

def min_search(grid, depth, alpha, beta): 
    costs = []
    if depth == 0:
        return calc_cost(grid)
    else:
        tmp_grid = grid.copy()
        for i in range(4):
            for j in range(4):
                if grid[i][j] == 0:
                    tmp_grid[i][j] = 2
                    curr_cost, move = max_search(tmp_grid, depth - 1, alpha, beta)
                    costs.append(curr_cost)
                    beta = min(beta, curr_cost)
                    if beta <= alpha:
                        if not costs:
                            return calc_cost(grid)
                        return min(costs)
                    tmp_grid[i][j] = 0
                    tmp_grid[i][j] = 4
                    curr_cost, move = max_search(tmp_grid, depth - 1, alpha, beta)
                    costs.append(curr_cost)
                    beta = min(beta, curr_cost)
                    if beta <= alpha:
                        if not costs:
                            return calc_cost(grid)
                        return min(costs)
                    tmp_grid[i][j] = 0
    if not costs:
        return calc_cost(grid)
    return min(costs)

def max_search(grid, depth, alpha, beta):
    costs = []
    if depth == 0:
        return calc_cost(grid), 1
    else:
        for i in range(4):
            curr_grid = grid_helper.move(grid, i)
            curr_cost = min_search(curr_grid, depth - 1, alpha, beta)
            costs.append(curr_cost)
            alpha = max(alpha, curr_cost)
            if beta <= alpha:
                if not costs:
                    return calc_cost(grid), 1
                res = max(costs)
                return res, costs.index(res)
    res = max(costs)
    return res, costs.index(res)

def min_max_search(grid):
    cost, move = max_search(grid, 6, -1000, 10000)
    return move
        


def NextMove(grid: list,step: int)->int: 
    return min_max_search(grid)
