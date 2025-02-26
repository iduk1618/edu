import psycopg2 as pg

con=pg.connect(
    database='prodavnica',
    user='postgres',
    password='qwer1234',
    host='localhost',
    port='5432'
)

cursor=con.cursor()
cursor.execute('SELECT * FROM PROIZVOD')

result=cursor.fetchall()
print(result)

for i in result:
    print('='*10)
    print('ID proizvoda',i[0])
    print('Naziv proizvoda',i[1])
    print('Cena proizvoda',i[2])
    print('Kolicina proizvoda',i[3])

con.close()