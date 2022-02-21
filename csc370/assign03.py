import psycopg2,sys,csv
psql_user = 'zhengyin216'
psql_db = 'zhengyin216'
psql_password = 'V00915261'
psql_server = 'studentdb1.csc.uvic.ca'
psql_port = 5432
connection = psycopg2.connect(dbname = psql_db,
                                    user = psql_user, password = psql_password,
                                    host = psql_server, port = psql_port)
def print_table(table):
	for tup in table:
		for item in tup:
			print (str(item).strip()),
		print()    
        
if __name__ == '__main__':
    cur = connection.cursor()
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    print(db_version)

    print ("pid, first_name, last_name, gender, prefered_name, birthday, country")
    cur.execute('SELECT * FROM users')
    print_table(cur.fetchall())
    print ("\n")
    print ("student information")
    cur.execute('SELECT * FROM student,users WHERE student.sid= users.userid')
    print_table(cur.fetchall())
    print("\n")
    print("student contact information")
    cur.execute("SELECT connection FROM users")
    print_table(cur.fetchall())

    print("\n")
    print("the language of users connection is 'student2@uvic.ca'")
    cur.execute("SELECT language FROM users WHERE users.connection ='student2@uvic.ca'")
    print_table(cur.fetchall())

    print("\n")
    print("original student list")
    cur.execute("SELECT * FROM student")
    print_table(cur.fetchall())

    print("\n")
    print("After inserting the new student")
    cur.execute("INSERT INTO student(SID,Levels,sCommits) VALUES (20016542,'3',' ')")
    cur.execute('SELECT * FROM student')
    print_table(cur.fetchall())


    print("\n")
    print("update the level of one worksheet to next level")
    cur.execute("UPDATE worksheet SET Levels='2' WHERE worksheet.WSID=40001001")
    cur.execute('SELECT * FROM worksheet')
    print_table(cur.fetchall())

    print("\n")
    print("delete the new student")
    cur.execute("DELETE FROM student WHERE SID=20000021")
    cur.execute("SELECT * FROM student")
    print_table(cur.fetchall())
