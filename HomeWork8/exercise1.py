import sqlite3 as sq
with sq.connect('new db') as con:
    cur = con.cursor()
# VARCHAR
    cur.execute(''' 
    CREATE TABLE IF NOT EXISTS Books(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    date_published TEXT
    )
    ''')

    cur.execute('''
       INSERT INTO Books(title,author,date_published)
VALUES('De Profundis','Oscar Wilde','1905')       
    ''')
    con.commit()

    cur.execute('''
           INSERT INTO Books(title,author,date_published)
    VALUES('Harry Potter and the chamber of secrets','J.K Rowling','1998')       
        ''')
    con.commit()

    cur.execute('''
           INSERT INTO Books(title,author,date_published)
    VALUES('Harry Potter and the prisoner of Azkaban','J.K Rowling','1999')       
        ''')
    con.commit()

    cur.execute('''
           INSERT INTO Books(title,author,date_published)
    VALUES('Lyrebird','Cecelia Ahern','2017')       
        ''')
    con.commit()

    cur.execute('''
           INSERT INTO Books(title,author,date_published)
    VALUES('Murder on the Orient Express','Agatha Christie','1934')       
        ''')
    con.commit()

    cur.execute('''
           INSERT INTO Books(title,author,date_published)
    VALUES('Perfect','Cecelia Ahern','2017')       
        ''')
    con.commit()

    cur.execute('''
           INSERT INTO Books(title,author,date_published)
    VALUES('The marble collector','Cecelia Ahern','2016')       
        ''')
    con.commit()

    cur.execute('''
           INSERT INTO Books(title,author,date_published)
    VALUES('The murder on the links','Agatha Christie','1923')       
        ''')
    con.commit()

    cur.execute('''
           INSERT INTO Books(title,author,date_published)
    VALUES('The picture of Dorian Gray','Oscar Wilde','1890')       
        ''')
    con.commit()
