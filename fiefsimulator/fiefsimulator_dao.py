import json
import mysql.connector


# 1. Create the Fief
# 2. Create yearly income plan
# 3. Create yearly expense plan
# 4. Roll all dice to decide outcome
# 5. Create yearly actual incomes
# 6. Create yearly actual expenses
# 7. Update fief
# 8. Repeat steps 2-7

mydb = None
mycursor = None
def initialize():
    global mydb
    global mycursor
    mydb = mysql.connector.connect(
    host = "localhost",
    user="fief",
    password="fiefdom",
    db="fiefdomSimulator",
    auth_plugin="mysql_native_password"
    )
    mycursor = mydb.cursor()
    print "Dao Initialized"
    print mycursor


#1.

def updateIndustries(industriesDict):
    global mydb
    global mycursor
    id = industriesDict["id"]
    industryDict = industriesDict["industries"]

    mysqlString = "UPDATE fiefdom SET "
    for k,v in industryDict.iteritems():
        mysqlString = mysqlString + "%s = %d," %(k,v)
    mysqlString = mysqlString[:-1] +" where id = %d" % id
    print mysqlString
    mycursor.execute(mysqlString)
    mydb.commit()
    print industriesDict

def insertIntoFiefdom(fiefdom_json):
    global mydb
    global mycursor
    jsonDict = json.loads(fiefdom_json)
    cols = ", ".join(jsonDict.keys())
    vals = ", ".join(jsonDict.values())
    mysqlString = "INSERT INTO fiefdom (%s) values(\"%s\")" % (cols, vals)
    print mysqlString
    mycursor.execute(mysqlString)
    mydb.commit()

def getFiefdom(id):
    global mydb
    global mycursor
    mysqlString = "SELECT * from fiefdom where id = %d" % id
    mycursor.execute(mysqlString)
    vals = mycursor.fetchone()
    mysqlString = "SHOW columns FROM fiefdom"
    mycursor.execute(mysqlString)
    tableInfo = mycursor.fetchall()
    cols = getColumnNamesOfTable("fiefdom")
    fiefDict = dict(zip(cols, vals))
    return fiefDict

def getIncomePlanByYearAndFief(year, fief):
    global mydb
    global mycursor
    mysqlString = "SELECT * from income_plan where year = %d and fief_id = %d" %(year, fief)
    mycursor.execute(mysqlString)
    vals = mycursor.fetchone()
    cols = getColumnNamesOfTable("income_plan")
    planDict = dict(zip(cols,vals)
    return planDict



def getColumnNamesOfTable(table):
    global mydb
    global mycursor
    mysqlString = "SHOW columns FROM %s" %table
    mycursor.execute(mysqlString)
    tableInfo = mycursor.fetchall()
    cols = []
    for column in tableInfo:
        cols.append(column[0])
    return cols
