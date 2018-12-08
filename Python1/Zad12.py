from random import randint
rozmiar=128
macierz1=[[0]*rozmiar for a in range(rozmiar)]
macierz2=[[0]*rozmiar for a in range(rozmiar)]
suma_macierzy=[[0]*rozmiar for a in range(rozmiar)]

for i in range(0,rozmiar):
    for j in range(0,rozmiar):
        macierz1[i][j]=randint(0,100)
        macierz2[i][j]=randint(0,100)

for i in range(0,rozmiar):
    for j in range(0,rozmiar):
        suma_macierzy[i][j]=macierz1[i][j]+macierz2[i][j]

print("\n\nMACIERZ1:")
for i in range(0,rozmiar):
    print(macierz1[i])

print("\n\nMACIERZ2:")
for i in range(0,rozmiar):
    print(macierz2[i])

print("\n\nSUMA MACIERZY:")
for i in range(0,rozmiar):
    print(suma_macierzy[i])


