import pandas as pd

p=pd.DataFrame({'Ime':['Marko','Miljana','Stefan','Marija','Sofija','Nenad'],
                'Prezime':['Savic','Milovanovic','Nikolic','Simic','Marijanovic','Loviric'],
                'Ocena':[3,4,5,5,5,1],
                'Razred':[7,6,8,7,7,8]})

print(p)
print(p.iloc[0:2,0:1])
print(p.iloc[-2:,1:2])
print(p.loc[0:2,('Ime','Prezime','Razred')])
print(p.loc[:,'Ime'])

p['Odeljenje']=[1,2,3,4,5,6]
print(p)

print(p.head(2))
print(p.tail(3))
print(p.shape)
print(p.describe())

print(p.size)
print(p.sum())
print('Suma ocena',p.loc[:,('Ocena')].sum())  
print('Srednja ocena',p.loc[:,('Ocena')].mean())
print('Najmanja ocena',p.loc[:,('Ocena')].min())
print('Najveca ocena',p.loc[:,('Ocena')].max())