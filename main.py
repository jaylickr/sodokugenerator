from random import randint

GridWidth = 9
GridHeight = 9


def Generate_Rand_Grid():

    grid = []
    tilelen = []

    for y in range(GridHeight):
        for x in range(GridWidth):
            if len(tilelen) == 0:
                tilelen.append(randint(1,9))
            else:
                while True:
                    nextNum = randint(1,9)
                    if nextNum in tilelen:
                        nextNum = randint(1,9)
                    else:
                        tilelen.append(nextNum)
                        break

        grid.append(tilelen)
        tilelen = []

    return grid

def display_grid(grid):
    for tile in grid:
        print(tile)

def fix_collum(grid):
    dupetile = []
    newgrid = grid

    for collum in range(len(grid)):
        for row in range(len(grid)):
            while True:
                if newgrid[row][collum] in dupetile:
                    nextNum = randint(1,9)
                    newgrid[row][collum] = nextNum
                else:
                    dupetile.append(grid[row][collum])
                    break
        dupetile = []
        
    return newgrid

grid1 = Generate_Rand_Grid()
display_grid(grid1)
print("")
grid1 = fix_collum(grid1)
display_grid(grid1)