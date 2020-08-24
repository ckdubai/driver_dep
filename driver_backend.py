import sqlite3

def connect():
    conn=sqlite3.connect("transport.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS driver (id INTEGER PRIMARY KEY, emp_id INTEGER, name text, vehicle text, plate_no text, work_location text, img_path text)")
    conn.commit()
    conn.close()

def insert(emp_id,name,vehicle,plate_no,work_location,img_path):
    conn=sqlite3.connect("transport.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO driver VALUES(NULL,?,?,?,?,?,?)",(emp_id,name,vehicle,plate_no,work_location,img_path))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("transport.db")
    cur=conn.cursor()
    cur.execute("SELECT id,emp_id,name,vehicle,plate_no,work_location,img_path FROM driver")
    rows=cur.fetchall()
    conn.close()
    return rows

def getDriverId(driver_name):
    conn=sqlite3.connect("transport.db")
    #conn.row_factory = sqlite3.Row
    cur=conn.cursor()
    cur.execute("SELECT emp_id FROM driver WHERE name=?",(driver_name,))
    #rows=cur.fetchall()
    data = []
    for row in cur.fetchall():
        data.append(row[0])
    return data
    #result = [dict(row) for row in cur.fetchall()]
    conn.close()
    #return rows

def getDriverName():
    conn=sqlite3.connect("transport.db")
    #conn.row_factory = sqlite3.Row
    cur=conn.cursor()
    cur.execute("SELECT name FROM driver")
    #rows=cur.fetchall()
    data = []
    for row in cur.fetchall():
        data.append(row[0])
    return data
    #result = [dict(row) for row in cur.fetchall()]
    conn.close()
    #return rows

def update(id,emp_id,name,vehicle,plate_no,work_location,img_path):
    conn=sqlite3.connect("transport.db")
    cur=conn.cursor()
    cur.execute("UPDATE driver SET emp_id=?, name=?, vehicle=?, plate_no=?,work_location=?,img_path=? WHERE id=?",(emp_id,name,vehicle,plate_no,work_location,img_path,id))
    conn.commit()
    conn.close()

def delete(id):
    conn=sqlite3.connect("transport.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM driver WHERE id=?",(id,))
    conn.commit()
    conn.close()

def search(emp_id="",name="",vehicle="",plate_no="",work_location=""):
    conn=sqlite3.connect("transport.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM driver WHERE emp_id=? OR name=? OR vehicle=? OR plate_no=? OR work_location=?",(emp_id,name,vehicle,plate_no,work_location))
    rows=cur.fetchall()
    conn.close()
    return rows

connect()



#insert("jamandhi","Mayoori",1977,55355000)
#delete(2)
#update(3,"Nalukettuu","MT Vasudevan",1999,21312)
#print(view())
#print(search(author="Benyaamin"))
