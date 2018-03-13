from solvers import astar_solver
from maze import Maze
from draw_maze import draw_maze

maze = Maze.load_from_file('mazes/small.txt')
path = astar_solver.solve_maze(maze, (1,1), (7,6))
prev = (1,1)
for x in path:
    #print(x[0] , x[1]) # y then x
    if x[0] > prev[0]:
        print("down")
    elif x[0] < prev[0]:
        print("up")
    if x[1] > prev[1]:
        print("right")   
    elif x[1] < prev[1]:
        print("left")
    if x[0] == prev[0] and x[1] == prev[1]:
        print("stay")
    prev = x    
#draw_maze(maze, path)
