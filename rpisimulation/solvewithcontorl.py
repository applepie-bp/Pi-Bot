from solvers import astar_solver
from maze import Maze
#from draw_maze import draw_maze
from maze import Maze
import urllib.request

ip="http://127.0.0.1:5000"
maze = Maze.load_from_file('mazes/small.txt')
start = (1,1)
target = (7,6)
path = astar_solver.solve_maze(maze, start, target)
prev = (1,1)
for x in path:
    #print(x[0] , x[1]) # y then x
    if x[0] > prev[0]:
        print("down")
        #urllib.request.urlopen(ip+"/down")
    elif x[0] < prev[0]:
        print("up")
        #urllib.request.urlopen(ip+"/up")
    if x[1] > prev[1]:
        print("right")
        #urllib.request.urlopen(ip+"/right")
    elif x[1] < prev[1]:
        print("left")
        #urllib.request.urlopen(ip+"/left")
    if x[0] == prev[0] and x[1] == prev[1]:
        print("stay")
    prev = x
#draw_maze(maze, path)
