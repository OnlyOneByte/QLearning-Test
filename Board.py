"""
    Author: Rengang (Angelo) Yang

"""
from Mouse import Mouse

class BoardObj:


    # Constructs a new board using boardLayout input
    def __init__(self, boardLayoutFile):
        # Defined Class Variables
        self.cols, self.rows = None, None
        self.startCol, self.startRow = None, None
        self.endCol, self.endRow = None, None

        # 2d arrays. To be initialized later when length is known.
        self.gridVals = None
        self.obstacles = None

        # Read in file.
        self.readIn(boardLayoutFile)

        # Create the has-a mouse.
        self.mouse = Mouse(self.startCol, self.startRow)



    def drawState(self):
        
        
        
        return
        
    

    # Reads in file and initializes the variables.
    def readIn(self, file):
        boardReader = open(file, "r+")
        boardData = boardReader.readlines()
        boardReader.close()

        self.cols = int(boardData[0].split(',')[0])
        self.rows = int(boardData[0].split(',')[1])

        self.startCol = int(boardData[1].split(',')[0])
        self.startRow = int(boardData[1].split(',')[1])

        self.endCol = int(boardData[2].split(',')[0])
        self.endRow = int(boardData[2].split(',')[1])

        self.obstacles = []
        self.gridVals = [[0] * self.cols] * self.rows

        # TODO: Error checking to makesure that number of rows/cols is correct
        # TODO: Error checking to make sure that unknown characters dont exist
        for line in boardData[3:]:
            tempLine = line.strip('\n').split(' ')
            tempLineInt = [int(x) for x in tempLine]
            self.obstacles.append(tempLineInt)



        # TESTING ONLY. TODO: Remove when done.
        if(0):
            print("----------------")
            print("x:", self.cols, "y:", self.rows)
            print("sx:", self.startCol, "sy:", self.startRow)
            print("ex:", self.endCol, "ey:", self.endRow)
            print(self.obstacles)
            print(self.gridVals)
        
