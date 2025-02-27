import pyautogui as pg
from time import sleep
# pg.moveTo(1000,500,0.5)                   Pomera mis na koordinate iz gornje leve tacke ekrana (sirina ekrana,visina ekrana,vreme)
# sleep(1)
# pg.moveRel(100,100,0.2)                   Pomera mis na koordinate iz trenutne pozicije (sirina ekrana,visina ekrana,vreme)

# pg.rightClick(x=200,y=200)                Aktivira desni klik na zeljenim koordinatama
# pg.leftClick(x=200,y=200)                 Aktivira levi klik na zeljenim koordinatama
# pg.middleClick(x=500,y=300)               Aktivira srednji (tockic) levi klik na zeljenim koordinatama
# pg.doubleClick(x=550,y=200)               Aktivira dupli levi klik na zeljenim koordinatama
# pg.tripleClick(x=550,y=300)               Aktivira tri klik na zeljenim koordinatama
# pg.scroll(1000)                           Skroluje na zeljene koordinate

# pg.mouseDown(x=500,y=200,button='left')   Drzi zeljeni klik na zeljenim koordinatama
# sleep(0.5)
# pg.mouseUp(x=500,y=300,button='right')    Drzi zeljeni klik na zeljenim koordinatama

# print(pg.position())                      Ispisuje trenutnu poziviju misa
# print(pg.size())                          Ispisuje velicinu ekrana
# print(pg.onScreen(1080,520))              Ispisuje da li koorodinate postoje na ekranu
# pg.PAUSE=2.5                              Pauza izmedju koraka
# pg.FAILSAFE=True                          Sigurnosna mera - ako se u toku izvrsavanja koraka rucno pomeri mis, lanac koraka se prekida
