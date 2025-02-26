import psycopg2 as pg

def funkcija_all():
    try:
        con=pg.connect(
            database='prodavnica',
            user='postgres',
            password='qwer1234',
            host='localhost',
            port='5432'
        )

        cursor=con.cursor()
        cursor.execute("SELECT * FROM PROIZVOD")
        result=cursor.fetchall()

        for i in result:
            print('='*10)
            print('ID proizvoda',i[0])
            print('Naziv proizvoda',i[1])
            print('Cena proizvoda',i[2])
            print('Kolicina proizvoda',i[3])

    except(Exception, pg.Error) as e:
        print(e)

    finally:
        cursor.close()
        con.close()

def funkcija_many():
    try:
        con=pg.connect(
            database='prodavnica',
            user='postgres',
            password='qwer1234',
            host='localhost',
            port='5432'
        )

        cursor=con.cursor()
        cursor.execute("SELECT * FROM PROIZVOD")
        result=cursor.fetchmany(2)

        for i in result:
            print('='*10)
            print('ID proizvoda',i[0])
            print('Naziv proizvoda',i[1])
            print('Cena proizvoda',i[2])
            print('Kolicina proizvoda',i[3])

    except(Exception, pg.Error) as e:
        print(e)

    finally:
        cursor.close()
        con.close()

def funkcija_one():
    try:
        con=pg.connect(
            database='prodavnica',
            user='postgres',
            password='qwer1234',
            host='localhost',
            port='5432'
        )

        cursor=con.cursor()
        cursor.execute("SELECT * FROM PROIZVOD")
        result=cursor.fetchone()

        print(result)

    except(Exception, pg.Error) as e:
        print(e)

    finally:
        cursor.close()
        con.close()


funkcija_all()
print("-"*30)
funkcija_many()
print("-"*30)
funkcija_one()