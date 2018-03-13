#loads map from text file- and inserts into an array Map
def getmap(filename):
    num_lines = sum(1 for line in open(filename))
    #print(num_lines)
    f = open(filename,'r')
    w, h = 4, 4
    Map = [['' for x in range(w)] for y in range(h)] 
    for y in range(0,num_lines):
        message = f.readline()
        rowraw = list(message)
        row = rowraw[0:num_lines]
        #print(row)
        for x in range(0,num_lines):
            Map[y][x] = row[x]
    f.close()
    return Map

Map = getmap("maze1.txt")
print(Map)
