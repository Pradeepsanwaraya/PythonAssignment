dbdata="insert into student values(%s,%s,%s,%s,%s)"
dblist=[(1,'pradeep','bca',100000.00,'dhar'),(2,'ravi','bba',5000.00,'lebad'),(3,'raj','mca',45000.00,'dhar')]
dbcursor.executemany(dbdata,dblist)
mydb.commit()