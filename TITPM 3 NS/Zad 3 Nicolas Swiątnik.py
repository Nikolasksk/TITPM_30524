from collections import Counter

znaki=input("Podaj swój ciąg znaków: \n")
l1=dict(Counter(znaki))
l1=dict(sorted(l1.items(), key=lambda x: x[1], reverse=True))
l2=list(l1.values())
print("Liczba poszczególnych znaków i ich ilości: "+str(l1)+"\n")
print("Lista wartości: "+str(l2)+"\n")
print("Suma: "+ str(sum(l1.values())))
        # abcafdadcecedabadbbeffbbfaeaeeebddddebdd

    
        