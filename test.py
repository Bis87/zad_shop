import sqlite3

con = sqlite3.connect('data.db')

cur = con.cursor()

# create_table = "CREATE TABLE users(id int, username text, password text)"
#
# cur.execute(create_table)

user = (1, 'paul', '1111')

users = [(2, 'her', '2222'),
         (3, 'o4ko', '3333')]

create_user = "INSERT INTO users VALUES (?, ?, ?)"
cur.execute(create_user, user)
cur.executemany(create_user, users)

select_q = 'SELECT * FROM  users'
print(cur.execute(select_q))

con.commit()
con.close()
