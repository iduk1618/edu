import psycopg2 as pg

try:
    con=pg.connect(
        database='prodavnica',
        user='postgres',
        password='qwer1234',
        host='localhost',
        port='5432'
    )

    s=['''INSERT INTO MAGACIN (NAZIV) VALUES ('MAGACIN A2');'''
       '''INSERT INTO MAGACIN (NAZIV) VALUES ('MAGACIN A3');'''
       '''INSERT INTO MAGACIN (NAZIV) VALUES ('MAGACIN A4');''']



    cursor=con.cursor()
    for i in s:
        cursor.execute(i)

    con.commit()

    cursor.execute('SELECT * FROM MAGACIN')
    r=cursor.fetchall()
    print(r)

except(Exception, pg.Error) as e:
    print(e)

finally:
    cursor.close()
    con.close()
