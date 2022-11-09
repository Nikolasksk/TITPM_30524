from collections import Counter 
import numpy as np 
c=input("Podaj ciąg znaków:") 
l=dict(Counter(c)) 
l=dict(sorted(l.items())) 
l2=list(l.values()) 
s=sum(l.values()) 
praw=np.divide(l2,s) 
print("Znaki i lista: "+str(l)+","+str(praw))
d=len(praw) 
p=[] 
z=0 
for x in range(d): 
    p.append(z) 
    z=round(z+praw[x], 8) 
    p.append(z) 
d=len(p) 
print("Przedziały:") 
for i in range(d)[::2]: 
    if (i+1<d): 
        print("("+str(p[i])+", "+str(p[i+1])+")") 
    else: 
        break 
    # ABRAADABRA