# Khan Path Finding Maze

from copy import deepcopy

# Function to open a file using exception handling
def openFile():
    goodFile = False
    while goodFile == False:
        fname = input("Enter name of data file: ")
        # Begin exception handling
        try:
            # Try to open the file using the name given
            inFile = open(fname, 'r')
            # If the name is valid, set Boolean to true to exit loop
            goodFile = True
        except IOError:
            # If the name is not valid - IOError exception is raised
            print("Invalid filename, please try again ... ")
    return inFile
    
# Function to read the maze from the data file
def getMaze():
    mazeFile = openFile()
    line = mazeFile.readline()

    maze = []
    r = 0
    for line in mazeFile:
        line = line.strip()
        mazeRow = list(line)
        if 'G' in mazeRow:
            goalR = r
            goalC = mazeRow.index('G')
        maze.append(mazeRow)
        r += 1
    mazeFile.close()
    return maze, goalR, goalC

# Function to print the maze
def printMaze(maze):
    for row in maze:
        rStr = ''
        for c in row:
            space = ' '*(4-len(str(c)))
            rStr = rStr + space + str(c)
        print(rStr)
    return

# Function to assign cost to each cell based on distance from goal
#   This function will assign a cost value to the current cell, go to each adjacent cell to
#   recursively assign a cost value to each of them
#
# Input Parameters:  costmaze
#                    gR - row position of the Goal cell
#                    gC - column position of the Goal cell
#                    val - cost value of the current cell 
def mazeCost(costmaze, r, c, val):
    # Compute the value for the current cell
    costmaze[r][c] = val
    
    # Make sure the current cell is not on an edge
    #
    # For each cell adjacent to the current cell (UP, DOWN, LEFT and RIGHT)
    # Make sure the cell is not a wall (X)
    # If the cell is empty (-)
    #       call mazeCost with val+1 as its value
    # Otherwise, if the cell has a value already, but the value is higher than val+1
    #       call mazeCost with val+1 as its value
    
    # UP
    if r > 0:
        if costmaze[r-1][c] != 'X':
            if costmaze[r-1][c] == '-':
                mazeCost(costmaze, r-1,c, val+1)
            elif costmaze[r-1][c] > val+1:
                mazeCost(costmaze, r-1,c, val+1)
    # DOWN
    if r < len(costmaze):
        if costmaze[r+1][c] != 'X':
            if costmaze[r+1][c] == '-':
                mazeCost(costmaze, r+1, c, val+1)
            elif costmaze[r+1][c] > val+1:
                mazeCost(costmaze, r+1, c, val+1)
    # LEFT
    if c > 0:
        if costmaze[r][c-1] != 'X':
            if costmaze[r][c-1] == '-':
                mazeCost(costmaze, r, c-1, val+1)
            elif costmaze[r][c-1] > val+1:
                mazeCost(costmaze, r, c-1, val+1)
    # RIGHT
    if c < len(costmaze[0]):
        if costmaze[r][c+1] != 'X':
            if costmaze[r][c+1] == '-':
                mazeCost(costmaze, r, c+1, val+1)
            elif costmaze[r][c+1] > val+1:
                mazeCost(costmaze, r, c+1, val+1)
    return


# Function to find the next move (min cost) towards the goal
def nextMove(maze, r, c):
    if maze[r][c] == 'X':
        return 'Invalid cell'
    min = 9999
    # LEFT
    leftCell = maze[r][c-1]
    if leftCell != 'X':
        min = leftCell
        move = 'LEFT' 
    # RIGHT
    rightCell = maze[r][c+1]
    if rightCell != 'X':
        if rightCell < min:
            min = rightCell
            move = 'RIGHT'
    # UP
    upCell = maze[r-1][c]
    if upCell != 'X':
        if upCell < min:
            min = upCell
            move = 'UP'
    # DOWN
    downCell = maze[r+1][c]
    if downCell != 'X':
        if downCell < min:
            min = downCell
            move = 'DOWN'
    return move


# Function to solve the maze
def solveMaze(maze, startR, startC):
    row = startR
    col = startC
    while maze[row][col] != 0:
        move = nextMove(maze, row, col)
        print(move)
        if move == 'UP':
            row = row - 1
        elif move == 'DOWN':
            row = row + 1
        elif move == 'LEFT':
            col = col - 1
        elif move == 'RIGHT':
            col = col + 1
        else:
            return
    return
            

# Function to get start point for maze
def getStart(maze):
    good = False
    while good == False:
        row = int(input("Enter starting row: "))
        col = int(input("Enter starting column: "))
        if row > len(maze) or col > len(maze[0]) or maze[row][col] == 'X':
            print('Invalide cell -- try again')
        else:
            good = True
    return row, col
    
    
                    
    
def main():
    maze, goalR, goalC = getMaze()
    printMaze(maze)
    costmaze = deepcopy(maze)
    mazeCost(costmaze, goalR, goalC, 0)
    print('\nCost Maze: \n')
    printMaze(costmaze)
    row, col = getStart(maze)
    solveMaze(costmaze, row, col)

                   

    
        
