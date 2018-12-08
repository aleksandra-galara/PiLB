from random import randint
rozmiar=8
macierz1=[[0]*rozmiar for a in range(rozmiar)]
macierz2=[[0]*rozmiar for a in range(rozmiar)]
#macierz1=[[-1,-2,3],[0,2,-1],[-1,3,0]]
#macierz2=[[1,5,1],[2,1,2],[3,2,3]]
iloczyn_macierzy=[[0]*rozmiar for a in range(rozmiar)]

for i in range(0,rozmiar):
    for j in range(0,rozmiar):
        macierz1[i][j]=randint(0,2)
        macierz2[i][j]=randint(0,2)

for i in range(0,rozmiar):
    for j in range(0,rozmiar):
        iloczyn_macierzy[i][j]=macierz1[i][0]*macierz2[0][j]+macierz1[i][1]*macierz2[1][j]+macierz1[i][2]*macierz2[2][j]+macierz1[i][3]*macierz2[3][j]+macierz1[i][4]*macierz2[4][j]+macierz1[i][5]*macierz2[5][j]+macierz1[i][6]*macierz2[6][j]+macierz1[i][7]*macierz2[7][j]

print("\n\nMACIERZ1:")
for i in range(0,rozmiar):
    print(macierz1[i])

print("\n\nMACIERZ2:")
for i in range(0,rozmiar):
    print(macierz2[i])

print("\n\nILOCZYN MACIERZY:")
for i in range(0,rozmiar):
    print(iloczyn_macierzy[i])
