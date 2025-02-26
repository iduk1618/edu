import psycopg2 as pg

try:
    con=pg.connect(
        database='prodavnica',
        user='postgres',
        password='qwer1234',
        host='localhost',
        port='5432'
    )

    s='''CREATE TABLE MAGACIN(
        ID_MAGACINA SERIAL PRIMARY KEY,
        NAZIV VARCHAR(15)
        );'''

    cursor=con.cursor()

    cursor.execute(s)

    con.commit()

    cursor.execute('SELECT * FROM MAGACIN')
    r=cursor.fetchall()
    print(r)

except(Exception, pg.Error) as e:
    print(e)

finally:
    cursor.close()
    con.close()
