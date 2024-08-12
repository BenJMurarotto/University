def mapcoord(rank, file):
    return rank + file

class Board:
    def __init__(self):
        self.xcoord = ['1', '2', '3', '4', '5', '6', '7', '8']
        self.ycoord = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.boardpos = [mapcoord(rank, file) for rank in self.xcoord for file in self.ycoord]

board = Board()
print(board.boardpos)
