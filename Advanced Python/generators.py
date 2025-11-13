def zaehle_bis(n):
    zahl = 0
    while zahl < n:
        yield zahl
        zahl += 1

g = zaehle_bis(5)
print(next(g))
print(next(g))