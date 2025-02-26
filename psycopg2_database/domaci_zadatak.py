# Kreirati tabelu i bazu, bazu kroz pgAdmin a tabelu korz python
# Baza ce se zvati covek
# Tabela ce se zvati isto covek i imace sledeca polja (JMBG varchar(13),Ime varchar(15),Prezime varchar (15)))
# Popuniti tu tabelu sa makar 5 osoba kroz python
# Ucitati sve podatke iz te tabele u python i ispisati ih u tekstualni fajl covek.txt
# Sa sledecim formatom
# JMBG: 12345
# Ime: Nikola
# Prezime: Martinovic
# ===================

import psycopg2 as pg

try:
    con=pg.connect(
        database='covek',
        user='postgres',
        password='qwer1234',
        host='localhost',
        port='5432'
    )
    cursor = con.cursor()

    cursor.execute('DROP TABLE IF EXISTS COVEK')

    create_script='''CREATE TABLE IF NOT EXISTS COVEK(
                        JMBG VARCHAR(13) PRIMARY KEY NOT NULL,
                        IME VARCHAR(15),
                        PREZIME VARCHAR(15)
                        );'''
    
    cursor.execute(create_script)

    input_script='''INSERT INTO COVEK (JMBG,IME,PREZIME) VALUES (%s,%s,%s)'''
    insert_values=[(13245,'Ivan','Djukanovic'),
                   (13246,'Nikola','Stankovic'),
                   (13247,'Vladimir','Gvozdenovic'),
                   (13248,'Milos','Danilovic'),
                   (13249,'Davor','Kuser')]
    for record in insert_values:
        cursor.execute(input_script,record)

    con.commit()

    cursor.execute('SELECT * FROM COVEK')
    records = cursor.fetchall()

    with open('covek.txt', 'w') as file:
        for record in records:
            file.write(f'JMBG: {record[0]}\n')
            file.write(f'IME: {record[1]}\n')
            file.write(f'PREZIME: {record[2]}\n')
            file.write(f'====================\n')

except(Exception,pg.Error) as error:
    print(error)
finally:
    cursor.close()
    con.close()