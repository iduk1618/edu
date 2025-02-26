import pandas as pd

df=pd.read_csv('data.csv')

print(df)

p=pd.DataFrame({'Ime':['Marko','Miljana','Stefan','Marija','Sofija','Nenad'],
                'Prezime':['Savic','Milovanovic','Nikolic','Simic','Marijanovic','Loviric'],
                'Ocena':[3,4,5,5,5,1],
                'Razred':[7,6,8,7,7,8]})

p.to_csv('file.csv',index=False)