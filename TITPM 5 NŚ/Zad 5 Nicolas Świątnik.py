from collections import Counter
tekst=input("Podaj wiadomość: \n") 
sl=[]
inx=[]
ms=[]
for i in tekst: 
    if i in sl: 
        continue 
    else: 
        sl.append(i) 
sl.sort() 
if sl[0]=="": 
    x=(sl) 
    sl.remove(), sl.insert(x) 
print("Słownik podstawowy: \n"+str(sl)) 
c=tekst[0]
dlugosc=len(tekst) 
for j in range(dlugosc): 
    if j+1<dlugosc:
        s=tekst[j+1] 
        suma=c+s 
        if suma in sl: 
            c=c+s 
        else: 
            indeks=sl.index(c)
            indeks=indeks+1
            ms.append(indeks)
            sl.append(suma) 
            c=s 
    else: 
        break
indeks=sl.index(c)
indeks=indeks+1
ms.append(indeks)
print("Słownik pełny: \n"+str(sl))
print("Zakodowana wiadomość: \n"+str(ms)) 
# wabbawabba