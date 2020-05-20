class ChessGame:
    def __init__(self, hash, fens, outcome, isOver):
        self.hash = hash
        self.fens = fens
        self.outcome = outcome
        self.isOver = isOver
class BoardState:
    def __init__(self, fen, white, black, ties, endingMove,id=-1,updated=False):
        self.id = id
        self.fen = fen
        self.white = white
        self.black = black
        self.ties = ties
        self.endingMove = endingMove
        self.updated = updated
    def addStats(self, white,black,ties):
        self.white = self.white+white
        self.black = self.black+black
        self.ties = self.ties+ties
    def __str__(self):
        return "ID: %d, Fen: %s, White: %d, Black: %d, Ties: %d, Ending move: %d" %(self.id, self.fen, self.white, self.black, self.ties, self.endingMove)

class LogEntry:
    def __init__(self, fileName, nrOfGames, newConnections, totalConnections, newBoardStates, totalBoardStates):
        self.fileName = fileName
        self.nrOfGames = nrOfGames
        self.newConnections = newConnections
        self.totalConnections = totalConnections
        self.newBoardStates = newBoardStates
        self.totalBoardStates = totalBoardStates
    def __str__(self):
        return "File: %s, Games run: %d, New connections: %d, Total connections: %d, New board states: %d, Total board states: %d" %(self.fileName, self.nrOfGames, self.newConnections, self.totalConnections, self.newBoardStates, self.totalBoardStates)
    def validate(self):
        return self.newConnections >0 or self.totalConnections > 0 or self.newBoardStates > 0 or self.totalBoardStates > 0
