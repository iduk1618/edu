import psycopg2 as pg


def popuni_magacin(naziv):
    try:
        con=pg.connect(
            database='prodavnica',
            user='postgres',
            password='qwer1234',
            host='localhost',
            port='5432'
        )

        s='''INSERT INTO MAGACIN (NAZIV) VALUES ('{}');'''.format(naziv)

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

naziv=input('Unesite naziv magacina')
popuni_magacin(naziv)