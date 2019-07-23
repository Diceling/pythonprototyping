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

mydb = mysql.connector.connect(
host = "localhost",
user="fief",
password="fiefdom",
db="fiefdomSimulator",
auth_plugin="mysql_native_password"
)

mycursor = mydb.cursor()

#1.

def updateIndustries(json_string):
    jsonDict = json.loads(json_string)
    id = jsonDict["id"]
    industryDict = jsonDict["industries"]

    mysqlString = "UPDATE fiefdom SET "
    for k,v in industryDict.iteritems():
        mysqlString = mysqlString + "%s = %d," %(k,v)
    mysqlString = mysqlString[:-1] +" where id = %d" % id
    print mysqlString
    mycursor.execute(mysqlString)
    mydb.commit()
    print jsonDict

def insertIntoFiefdom(fiefdom_json):
    jsonDict = json.loads(fiefdom_json)
    cols = ", ".join(jsonDict.keys())
    vals = ", ".join(jsonDict.values())
    mysqlString = "INSERT INTO fiefdom (%s) values(\"%s\")" % (cols, vals)
    print mysqlString
    mycursor.execute(mysqlString)
    mydb.commit()



updateString = "{\"id\":1, \"industries\": {\"farming\": 3, \"livestock\":4,\"fishing\":1,\"hunting\":2}}"
insertString = "{\"name\":\"Oakheart\"}"
#insertIntoFiefdom(insertString)
updateIndustries(updateString)
