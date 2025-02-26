import pandas as pd
import openpyxl as op

wb=op.load_workbook(r'C:\Users\Djuka\Downloads\QA moji projekti\git\my_git\dataframes\eksel.xlsx')

ws=wb.active

def popuni_recnik(kolona):
    ime=ws[kolona]
    r_ime={}
    r_ime[ime[0].value]=[]
    for i in range(1,len(ime)):
        r_ime[ime[0].value].append(ime[i].value)

    return r_ime

r_ime=popuni_recnik('A')
r_prezime=popuni_recnik('B')
r_plata=popuni_recnik('C')

print(r_ime)
print(r_prezime)
print(r_plata)

r={}
r.update(r_ime)
r.update(r_prezime)
r.update(r_plata)

print(r)
df=pd.DataFrame(r)
print(df)