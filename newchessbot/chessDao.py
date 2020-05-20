import db_config
import pymysql

mydb = None
mycursor = None


#try:
conn = pymysql.connect(db_config.address,
                            user=db_config.user,
                            passwd=db_config.password,
                            db=db_config.name,
                            connect_timeout=5)
#except:
#    print "ERROR: Unexpected error: Could not connect to MySQL instance."


def getAllBoardStates():
    item_count=0
    vals = []
    mysqlString = "Select * from boardStates"
    with conn.cursor() as cur:
        cur.execute("select * from boardStates")
        for row in cur:
            item_count += 1
            vals.append(row)
            #print(row)
    return vals

def getAllConnections():
    vals = []
    with conn.cursor() as cur:
        cur.execute("select * from connections")
        for row in cur:
            vals.append(row)
            #print(row)
    return vals

def getAllGameHashes():
    item_count=0
    vals = []
    with conn.cursor() as cur:
        cur.execute("select * from games")
        for row in cur:
            item_count += 1
            vals.append(row[1])
            #print(row)
    return vals

def insertNewHashes(hashes):
    mysqlString = "Insert into games(hash) VALUES "
    for hash in hashes:
        mysqlString = mysqlString+"(\'%s\')," %hash
    mysqlString = mysqlString[:-1]
    mysqlString = mysqlString+";"
    with conn.cursor() as cur:
        cur.execute(mysqlString)
        conn.commit()

def insertNewConnections(connections):
    mysqlString = "Insert into connections(source, destination) VALUES "
    for x in connections:
        mysqlString = mysqlString+"(%d,%d)," %(x[0],x[1])
    mysqlString = mysqlString[:-1]
    mysqlString = mysqlString+";"
    try:
        with conn.cursor() as cur:
            cur.execute(mysqlString)
            conn.commit()
    except:
        print "Error"

def insertNewBoardStates(inserts):
    mysqlString = "Insert into boardStates(fen, white, black, ties, endingMove) VALUES "
    for x in inserts:
        mysqlString = mysqlString+"(\'%s\',%d,%d,%d,%d), " %(x.fen,x.white,x.black,x.ties,x.endingMove)
    mysqlString = mysqlString[:-2]
    mysqlString = mysqlString+";"
    with conn.cursor() as cur:
        cur.execute(mysqlString)
        conn.commit()
def updateBoardStates(updates):
    with conn.cursor() as cur:
        for update in updates:
            mysqlString = "Update boardStates SET fen=\"%s\",white=%d, black=%d, ties=%d, endingMove=%d where id=%d" % (update.fen,update.white,update.black,update.ties, update.endingMove, update.id)
            cur.execute(mysqlString)
        conn.commit()
def insertLog(log):
    mysqlString = "Insert into log(filename, gamesRun, newConnections, totalConnections, newBoardStates, totalBoardStates) VALUES "
    mysqlString = mysqlString+"(\'%s\',%d,%d,%d,%d,%d);" % (log.fileName,log.nrOfGames, log.newConnections, log.totalConnections, log.newBoardStates, log.totalBoardStates)
    with conn.cursor() as cur:
        cur.execute(mysqlString)
        conn.commit()
