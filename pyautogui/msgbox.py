import pyautogui as pg

#Ispisuje tekst u GUI prozoru (neko obavestenje)
pg.alert('This is some message')

#Nudi konfirmaciju u GUI prozoru, na onsnovu kliknutog
print(pg.confirm('This is some confirmation window',buttons=['Da','Ne'],title='Naslov'))

#Nudi prompt za neki unos koji se vraca i moze se ispsati printom
print(pg.prompt('Unesite nesto'))

#Nudi prompt za unos zasticen maskom (*,#...) kako bi korisnik sigurnije unosio npr. sifru
print(pg.password('Unesite sifru',title='Sifra',mask='#'))