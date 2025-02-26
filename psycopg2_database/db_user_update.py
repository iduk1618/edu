import psycopg2 as pg


def promena_cene(cena,id_proizvoda):
    try:
        con=pg.connect(
            database='prodavnica',
            user='postgres',
            password='qwer1234',
            host='localhost',
            port='5432'
        )

        s='''UPDATE PROIZVOD
            SET CENA={}
            WHERE ID_PROIZVODA={}'''.format(cena, id_proizvoda)

        cursor=con.cursor()

        cursor.execute(s)

        con.commit()

        cursor.execute('SELECT * FROM PROIZVOD')
        r=cursor.fetchall()
        print(r)

    except(Exception, pg.Error) as e:
        print(e)

    finally:
        cursor.close()
        con.close()

cena=float(input('Unsite novu cenu proizvoda '))
id_proizvoda=int(input('Unesite ID proizvoda '))

promena_cene(cena, id_proizvoda)