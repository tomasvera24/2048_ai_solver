# 2048 AI Solver

To search for the best move in the game 2048, I implemented the min max search algorithm with alpha beta pruning. The max min search algorithm uses recursion between its max and min counterparts at each level of the decision tree. The algorithm uses its max search to calculate the best (lowest cost) of the 4 possible moves at each step and uses its min search to calculate the worst possible (highest cost) random placement of a 2 or a 4 after performing the step. As such this min max algorithm will calculate the best possible move assuming the worst random placement of 2 or 4 takes place. My algorithm is set to look 6 layers deep of its decision tree on each move. I have additionally built a simulator application to the game 2048, where my constructed AI will make the best move, and this will be displayed to a user through gui. My implementation of this algorithm has yeilded a maximum 2048 block with value 4096.

## Usage

From root directory run this command on the command line

    Python3 simulator.py

## Project Features

* Min Max search algorithm with alpha-beta pruning
* Tailored heuristic to calculate the cost of each 2048 grid position
* Python turtle library implementation for the game gui display

## Search tree cost heuristic

To calculate the cost of each grid position I used a heuristic function. My heuristic adds the number of empty slots in the board, adds the largest number of the board, and adds a grid heuristic which prioritizes putting higher numbers at the bottom of the board on each move. I weighted each aspect of the heuristic by multiplying them by a constant and tuned these weights to get the best results. I found that with this implementation the algorithm got a good result in a reasonable time. I developed this heuristic by playing the game and realizing that I got the best results when I attempted to organize the higher numbers at the bottom of the board. By adding the highest number on the board, the algorithm prioritizes getting the best score with each configuration, and by adding the number of zeros on the board, the algorithm prioritizes surviving at each step.

