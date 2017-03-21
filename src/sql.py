import MySQLdb

# connect
def getDbConn():
	db = MySQLdb.connect(host="localhost", user="finadvisor", passwd="finadvisor",db="finadv")
	return db

def getDbCursor(db):
	cursor = db.cursor()
	return cursor
# execute SQL select statement
dbb = getDbConn()
cursors = getDbCursor(dbb)
# cursors.execute("SELECT * FROM temp")

# # commit your changes
# dbb.commit()

# # get the number of rows in the resultset
# numrows = int(cursors.rowcount)

# # get and display one row at a time.
# for x in range(0,numrows):
#     row = cursors.fetchone()
#     print row[0],row[1]


def tempIns(strng):
	sql = "INSERT INTO temp(b)VALUES ('%s')" % (strng)
	try:
	   # Execute the SQL command
	   cursors.execute(sql)
	   # Commit your changes in the database
	   dbb.commit()
	except:
	   # Rollback in case there is any error
	   print "problem"
	   dbb.rollback()

	# disconnect from server
	dbb.close()

def consultantInsert(lst):
	sql = "INSERT INTO consultant(username, password, email,contact, name, middlename, lastname) VALUES ('%s','%s','%s','%s','%s','%s','%s');" % (lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6])
	try:
	   # Execute the SQL command
	   cursors.execute(sql)
	   print sql
	   # Commit your changes in the database
	   dbb.commit()
	   #dbb.close()
	   return 0
	except:
	   # Rollback in case there is any error
	   print "problem"
	   dbb.rollback()
	   #dbb.close()
	   return 1

	# disconnect from server
	dbb.close()
