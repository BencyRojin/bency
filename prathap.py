import sqlite3
conn=sqlite3.connect('pr.db');
print('opened database successfully');
##conn.execute('''create table user (rollno int not null,
##            name text not null, age int not null, address char(50),
##            salary real);''')
##print('table created successfully')
##conn.close()
conn.execute('''insert into user (rollno,name,age,address,salary)
             values(11321,'john',30,'chennai',30000.00)''');
conn.commit()
print('records created successfully');
conn.close
