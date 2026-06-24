import sqlite3
try:
    # conn=sqlite3.connect("dbdata.db")
    # print("Data Connection established")
    # conn.close()
    with sqlite3.connect("dbdata.db") as conn:
        cmd="delete from tbemp where empno=?"
        conn.execute(cmd,(2,))
        conn.commit()
        # cmd="update tbemp set empnam=?,empdpt=?,empsal=? where empno=?"
        # conn.execute(cmd,('shalini sharma','Sales','123456',1))
        # conn.commit()

        # cmd="select * from tbemp where empnam like '_t%'"
        # cursor=conn.execute(cmd).fetchall()
        # for row in cursor:
        #     print(row[0],"\t",row[1],"\t",row[2],"\t",row[3])


        # cmd="insert into tbemp values(?,?,?,?)"
        # lst=[(3,'atul',"Sales",45600),(4,'Abha','Finance',35000),(5,'shiven',"Sales",56000)]
        # conn.executemany(cmd,lst)
        # conn.commit()



        # cmd="insert into tbemp values(?,?,?,?)"
        # lst=input("Enter empno,name,dept,salary").split(" ")
        # conn.execute(cmd,((int)(lst[0]),lst[1],lst[2],(int)(lst[3])))
        # conn.commit()
        # print("Data inserted successfully")
except sqlite3.Error as e:
     print(e)