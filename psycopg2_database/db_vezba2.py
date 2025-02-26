import psycopg2 as pg

try:
    con=pg.connect(
        database='auto',
        user='postgres',
        password='qwer1234',
        host='localhost',
        port='5432'
    )

    cursor=con.cursor()

    drop_table='''DROP TABLE IF EXISTS AUTO'''
    cursor.execute(drop_table)

    create_script='''CREATE TABLE IF NOT EXISTS AUTO(
                   REGISTRACIJA VARCHAR(10) PRIMARY KEY,
                   MARKA VARCHAR(20),
                   MODEL VARCHAR(20),
                   GODINA_PROIZVODNJE INTEGER
                   );'''

    cursor.execute(create_script)
    
    upit=input('Da li zelite da dodate novi auto? ')
    
    def input_script(registracija,marka,model,godina_proizvodnje):
        insert_script='''INSERT INTO AUTO (REGISTRACIJA,MARKA,MODEL,GODINA_PROIZVODNJE) VALUES (%s,%s,%s,%s)'''
        cursor.execute(insert_script, (registracija,marka,model,godina_proizvodnje))

    registracija=input('Unesite registraciju: ')
    marka=input('Unesite marku: ')
    model=input('Unesite model: ')
    godina_proizvodnje=int(input('Unesite godinu proizvodnje: '))
    
    
    input_script(registracija,model,marka,godina_proizvodnje)

    con.commit()

    cursor.execute('SELECT * FROM AUTO') 
    records=cursor.fetchall()
    print(records)

    with open('AUTO.txt', 'w') as file:
        for record in records:
            file.write(f'REGISTRACIJA: {record[0]}\n')
            file.write(f'MARKA: {record[1]}\n')
            file.write(f'MODEL: {record[2]}\n')
            file.write(f'GODINA_PROIZVODNJE: {record[3]}\n')
            file.write(f'====================\n')

except(Exception,pg.Error) as error:
    print(error)
finally:
    cursor.close()
    con.close()