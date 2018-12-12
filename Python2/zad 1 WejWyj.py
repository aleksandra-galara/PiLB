with open('zad 1 Odczyt.txt', 'r') as odczytany:
    with open('zad 1 Zapis.txt', 'w') as zapisany:
        i = 0
        for line in odczytany:
            print(line)
            zapisany.write(line)
