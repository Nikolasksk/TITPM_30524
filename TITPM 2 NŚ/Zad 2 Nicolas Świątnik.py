#!/usr/bin/env python3

from collections import Counter 
if __name__ == "__main__":
	zn=input("Prosze podac dowolny ciag znakow: ")
	q=dict(Counter(zn))
	q=sorted(q.items(), key=lambda x: x[1], reverse=True)
	q.sort()
	print("Zliczenie ilosci danego znaku w ciagu: " +str(q))