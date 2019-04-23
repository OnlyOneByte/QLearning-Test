"""
    Author: Rengang (Angelo) Yang

"""


class BoardObj:

    # Constructs a new board using boardLayout input
    def __init__(self, boardLayoutFile):
        # Defined Class Variables
        self.x, self.y = None, None
        self.startx, self.starty = None, None
        self.endx, self.endy = None, None

        # 2d arrays. To be initialized later when length is known.
        self.gridVals = None
        self.obstacles = None

        self.readIn(boardLayoutFile)
    

    # Reads in file and initializes the variables.
    def readIn(self, file):
        boardReader = open(file, "r+")
        boardData = boardReader.readlines()
        boardReader.close()

        print(boardData)