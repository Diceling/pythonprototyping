from chessGame import ChessGame
from chessGame import BoardState
from chessGame import LogEntry
import chess
import chess.pgn
import chessDao

log = LogEntry("",0,0,0,0,0)

def playGames(file, hashes):
    games = []
    pgn = open(file)
    game = chess.pgn.read_game(pgn)
    log.fileName = file

    while game != None:
        log.nrOfGames+=1
        print "New Game"
        counter = 1
        hash = ""
        fens = []
        board = game.board()
        for move in game.main_line():
            board.push(move)
            fenParts = board.fen().split(" ")
            fens.append("%s - %s" %(fenParts[0], fenParts[1]))
            moveId = "%s_%s_%d" % (board.piece_at(move.to_square),str(move),counter)
            counter = counter+1
            hash = "%s%s" % (hash,move)
        if hash not in hashes:
            chessGame = ChessGame(hash,fens, game.headers["Result"], board.is_game_over())
            games.append(chessGame)
        else:
            print "Game already played, moving on to next."
        game = chess.pgn.read_game(pgn)
        ##for f in fens:
        ##    print "%d. %s" %(counter, f)
        ##    counter = counter+1
    return games


def createBoardStatesFromGames(games, bStates):
    connections= []
    boardStates = {}
    if isinstance(bStates, dict):
        boardStates = bStates
    for game in games:
        white = 0
        black = 0
        ties = 0
        if game.outcome == "1-0":
            white = 1
        elif game.outcome == "0-1":
            black = 1
        else:
            ties = 1
        log.totalBoardStates+=len(game.fens)
        for x in range(0, len(game.fens)):
            fen = game.fens[x]
            endingMove = False
            if x == len(game.fens)-1 and game.isOver:
                endingMove = True
            if x > 0:
                connections.append([game.fens[x-1], fen])
                log.totalConnections+=1
            bs = BoardState(fen, white, black, ties, endingMove)
            if fen not in boardStates:
                boardStates[fen] = bs
                log.newBoardStates+=1
            else:
                boardStates[fen].addStats(white, black,ties)
                boardStates[fen].updated = True
    return boardStates, connections

def divideBoardStates(boardStates):
    inserts = []
    updates = []

    for k,v in boardStates.iteritems():
        if v.id == -1:
            inserts.append(v)
        if v.updated == True:
            updates.append(v)
    return inserts, updates

def handleConnections(fenConnections):
    newConnections = []
    allBoardStates = getAllBoardStates()
    allConnections = getAllConnections()
    for fencon in fenConnections:
        src = allBoardStates[fencon[0]].id
        dest = allBoardStates[fencon[1]].id
        con = [src,dest]
        if con not in newConnections:
            if con not in allConnections:
                log.newConnections+=1
                newConnections.append(con)
    return newConnections


def getAllBoardStates():
    rows = chessDao.getAllBoardStates()
    boardStates = {}
    for row in rows:
        bs = BoardState(row[1],row[2],row[3],row[4],row[8],row[0])
        boardStates[row[1]] = bs
    return boardStates

def getAllConnections():
    rows = chessDao.getAllConnections()
    connections = []
    for row in rows:
        con = [row[0],row[1]]
        connections.append(con)
    return connections

def separateHashesFromGames(games):
    hashes = []
    for game in games:
        hashes.append(game.hash)
    return hashes


#chessDao.initialize()
pgnFile = "firstGame.pgn"
pgnFile = "WorldChamp2018.pgn"
pgnFile = "Dortmund2019.pgn"
pgnFile = "Gibraltar2019.pgn"
pgnFile = "Moscow2019.pgn"
pgnFile = "SaintLouis2019.pgn"
pgnFile = "Shamkir2019.pgn"
pgnFile = "Shenzhen2019.pgn"
pgnFile = "Stavanger2019.pgn"
pgnFile = "WijkaanZee2019.pgn"
pgnFile = "Zagreb2019.pgn"
hashes = chessDao.getAllGameHashes()
games = playGames(pgnFile, hashes)

if len(games) > 0:
    bStates = getAllBoardStates()
    boardStates, connections = createBoardStatesFromGames(games,bStates)
    inserts, updates = divideBoardStates(boardStates)
    newHashes = separateHashesFromGames(games)

    if isinstance(newHashes, list) and len(newHashes) > 0:
        chessDao.insertNewHashes(newHashes)
    else:
        print "No new Hashes"

    if isinstance(inserts, list) and len(inserts) > 0:
        chessDao.insertNewBoardStates(inserts)
        print "Inserts: %d" % len(inserts)
    else:
        print "No new Inserts"

    if isinstance(updates, list) and len(updates) > 0:
        print "Updates: %d" % len(updates)
        chessDao.updateBoardStates(updates)
    else:
        print "No updates"


    if len(connections) > 0:
        newConnections = handleConnections(connections)
    if isinstance(newConnections, list) and len(newConnections)>0:
        print "New Connections: %d" %len(newConnections)
        chessDao.insertNewConnections(newConnections)
    else:
        print "No new connections"

    if log.validate():
        chessDao.insertLog(log)
