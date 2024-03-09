# ZADANIA LAB2.docx
# ZADANIE 1

# zdanie = input("Podaj zdanie: ")
# slowa = zdanie.split()
# ilosc_slow = len(slowa)
# print (ilosc_slow)

# ZADANIE 2

# import sys
# sys.stdout.write("Podaj pierwszą liczbę całkowitą: ")
# a = int(sys.stdin.readline())
# sys.stdout.write("Podaj drugą liczbę całkowitą: ")
# b = int(sys.stdin.readline())
# sys.stdout.write("Podaj trzecią liczbę całkowitą: ")
# c = int(sys.stdin.readline())
# wynik = pow(a, b) + c
# print (wynik)

# ZADANIE 3

# tekst = input("Podaj zdanie: ")
# dlugosc = len(tekst)
# polowa_dlugosci = dlugosc // 2
# for i in range(polowa_dlugosci):
#     if tekst[i] != tekst[dlugosc -i -1]:
#         print("Nie jest")
#         break
#     else:
#         print("Nie jest")
#         break
# ZADANIE 4

# x=0
# liczba = int(input("Podaj liczbe: "))
# if liczba < 2:
#         print ("Liczba musi być większa od 1")
# i = 2
# while i * i <= liczba:
#     if liczba % i == 0:
#         print("Nie jest liczba pierwsza")
#         x+=1
#         break
#     i += 1
# if(x==0):
#      print ("Jest liczba pierwsza")

# ZADANIE 5

# liczba=1
# max1=1000
#
#
# wynik=0
# while liczba<max1:
#     dzielnik=1
#     suma=0
#     while liczba/2>=dzielnik:
#         if liczba%dzielnik==0:
#             suma+=dzielnik
#         dzielnik+=1
#     if(liczba==suma):
#         wynik+=1
#     liczba += 1
# print(wynik)
# ZADANIE 6
# liczby = [2, 3.5, 5, 7.7, 9]
#
# for i in range(len(liczby)):
#     liczby[i] = liczby[i] ** 2
# print(liczby)

# ZADANIE 7

# parzyste_liczby = []
# slownik = 0
#
# while slownik < 10:
#     liczba = float(input("Podaj liczbę: "))
#     if liczba % 2 == 0:
#         parzyste_liczby.append(liczba)
#     slownik += 1
#
# print(parzyste_liczby)

# ZADANIE 8

# Lista z elementami różnego typu
# lista = [42, 3.14, 'Ala ma kota', 42, 3.14]
# slownik = {}
#
# for element in lista:
#     if element in slownik:
#         slownik[element] += 1
#     else:
#         slownik[element] = 1
# for key in list(slownik.keys()):
#     if isinstance(key, str):
#         del slownik[key]
# print(slownik)

# ZADANIA lab1.pdf

# ZADANIE1

# liczba_calkowita1 = 7
# liczba_calkowita2 = 42
#
# liczba_zmiennoprzecinkowa1 = 3.14
# liczba_zmiennoprzecinkowa2 = 2.718
#
# napis1 = "Ala ma kota"
# napis2 = "Kot ma Ale"
#
# prawda = True
# falsz = False
#
# print("Zmienne typu int:", liczba_calkowita1, liczba_calkowita2)
# print("Zmienne typu float:", liczba_zmiennoprzecinkowa1, liczba_zmiennoprzecinkowa2)
# print("Zmienne typu string:", napis1, napis2)
# print("Zmienne typu bool:", prawda, falsz)

# ZADANIE2

# liczba1 = float(input("Podaj pierwszą liczbę: "))
# liczba2 = float(input("Podaj drugą liczbę: "))
# operacja = input("Wybierz operację (+, -, *, /, %): ")
#
# if operacja == '+':
#     wynik = liczba1 + liczba2
# elif operacja == '-':
#     wynik = liczba1 - liczba2
# elif operacja == '*':
#     wynik = liczba1 * liczba2
# elif operacja == '**':
#     wynik=liczba1**liczba2
# elif operacja == '/':
#     if liczba2 != 0:
#         wynik = liczba1 / liczba2
#     else:
#         print("Błąd: Dzielenie przez zero!")
#         wynik = "Błąd"
# elif operacja == '%':
#     wynik = liczba1 % liczba2
# else:
#     print("Niepoprawna operacja!")
#     wynik = "Błąd"
# print("Wynik:",wynik)

# ZADANIE 3

# a = 10
# b = 3
#
# a += b
# print("a po dodaniu b:", a)
# a -= b
# print("a po odjęciu b:", a)
# a *= b
# print("a po pomnożeniu przez b:", a)
# a /= b
# print("a po podzieleniu przez b:", a)
# a **= b
# print("a do potęgi b:", a)
# a %= b
# print("reszta z dzielenia a przez b:", a)

# ZADANIE4
# import math
#
# edo10 = math.exp(10)
# pierwiastek = (math.log(5 + math.sin(8)**2))**(1/6)
# zaokraglenie_w_dol = math.floor(3.55)
# zaokraglenie_w_gore = math.ceil(4.80)
#
# print("Pierwszy wynik", edo10)
# print("Drugi wynik",pierwiastek)
# print("Trzeci wynik",zaokraglenie_w_dol)
# print("Czwarty wynik",zaokraglenie_w_gore)

# ZADANIE5
# imie = "JAN"
# nazwisko = "NOWAK"
#
# sformatowane_imie = imie.capitalize()
# sformatowane_nazwisko = nazwisko.capitalize()
#
# print("Imię:", sformatowane_imie)
# print("Nazwisko:", sformatowane_nazwisko)

# ZADANIE6
# tekst = "la la la, la la la, la la la la"
# ilosc_la = tekst.count("la")
# print("Ilość wystąpień słowa 'la':",ilosc_la)

# ZADANIE7
# zdanie = "Ala ma kota"
#
# print("Druga litera:", zdanie[1])
# print("Ostatnia litera:", zdanie[-1])

# ZADANIE8
# tekst_piosenki = "la la la, la la la, la la la la "
# wyrazy = tekst_piosenki.split()
# print(wyrazy)

# ZADANIE9
# tekst = "Ala ma kota"
# liczba_float = 3.14159
# liczba_szestnastkowa = 0x1a2b
# print("Zmienna typu string:", tekst)
# print("Zmienna typu float: {:.2f}".format(liczba_float))
# print("Zmienna typu szestnastkowe:", hex(liczba_szestnastkowa))

# ZADANIA lab2.pdf

# ZADANIE1

# ulubione_sporty = ['piłka nożna', 'snooker', 'piłka ręczna']
#
# ulubione_sporty.reverse()
#
# mniej_lubiane_sporty = ['kolarstwo', 'hokej']
# ulubione_sporty.extend(mniej_lubiane_sporty)
# print(ulubione_sporty)

# ZADANIE2

# skroty = {
#     'np.': 'na przykład',
#     'itd.': 'i tak dalej',
#     'm.in.': 'między innymi',
#     'tzn.': 'to znaczy',
#     'wg': 'według',
#     'art.': 'artykuł'
# }
# print(skroty)

# ZADANIE3

# ulubione_gry = {
#     'Wiedzmin 3': 'RPG',
#     'Resident Evil 2 Remake': 'Survival Horror',
#     'Gothic 2:Noc Kruka': 'RPG',
#     'Tomb Raider 4': 'Action/Adventure',
#     'Call of Duty 2': 'Action',
#     'Batman: Arkham Asylum': 'Action',
#     'Heroes of Might and Magic IV': 'Strategy'
#  }
# print("Liczba ulubionych gier komputerowych:", len(ulubione_gry))

# ZADANIE4

# zdanie = input("Wpisz zdanie: ")
#
# ilosc_a = zdanie.count('a') + zdanie.count('A')
# print("Ilość wystąpień litery 'a':",ilosc_a)

# ZADANIE5

# import sys
#
# sys.stdout.write("Podaj liczbę całkowitą a: ")
# a = int(sys.stdin.readline())
#
# sys.stdout.write("Podaj liczbę całkowitą b: ")
# b = int(sys.stdin.readline())
#
# sys.stdout.write("Podaj liczbę całkowitą c: ")
# c = int(sys.stdin.readline())
#
# wynik = a**b + c
#
# sys.stdout.write("Wynik obliczeń a^b + c to:"+str(wynik))

# ZADANIE6

# a = int(input("Podaj liczbę całkowitą a: "))
# b = int(input("Podaj liczbę całkowitą b: "))
# c = int(input("Podaj liczbę całkowitą c: "))
# if a > b:
#     if a > c:
#         print("Największa liczba to a:", a)
#     else:
#         print("Największa liczba to c:", c)
# else:
#     if b > c:
#         print("Największa liczba to b:", b)
#     else:
#         print("Największa liczba to c:", c)

# ZADANIE7

# liczby = [2, 3.5, 5, 7.7, 9]
#
# for i in range(len(liczby)):
#     liczby[i] = liczby[i] ** 2
# print(liczby)

# ZADANIE8

# parzyste_liczby = []
#
# licznik = 0
#
# while licznik < 10:
#     liczba = int(input("Podaj liczbę całkowitą: "))
#     if liczba % 2 == 0:
#         parzyste_liczby.append(liczba)
#     licznik += 1
#
# print("Parzyste liczby to:", parzyste_liczby)

# ZADANIE9

# liczba = float(input("Podaj liczbę, z której chcesz obliczyć pierwiastek kwadratowy: "))
#
# if liczba >= 0:
#     pierwiastek = liczba ** 0.5
#     print("Pierwiastek kwadratowy to",pierwiastek)
# else:
#     print("Błąd Podałeś liczbę ujemną.")
