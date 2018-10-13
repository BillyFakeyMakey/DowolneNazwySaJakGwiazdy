#Pobieranie danych od uzytkownika

ileKotow = input("Podaj jak wysokie schody z kotow chcesz miec: ")
#ileKotow = int(ileKotow)
try:
    ileKotow = int(ileKotow)
except ValueError as owcaError:
    #tutaj piszecie instrukcje ktore sie zdarz ktore sie wykonaja kiedy zdarzy sie error
    print(f'Wystapil Blad Liczbowy, program przujmuje tylko liczby naturalne')

"""
zadanie 1
napisac program ktory wypisze w linijce iles kotow
przyklad kota (=^.^=)
przyklad
wpisujecie 3:
wypisuje: (=^.^=) (=^.^=) (=^.^=)
INFO
data oddania: 27.10.2018
jezeli wyslecie do 20 macie 0.5 punkta wiecej
jezeli wyslecie zadanie githubem to +1pkt
zadanie mozecie wyslac snipetem
Zadanie 2 
    Napisać program który generuje schody z kotów
    Przykład
    Wpisujecie: 4
    Wypisuje: 
    (=^.^=)
    (=^.^=)(=^.^=)
    (=^.^=)(=^.^=)(=^.^=)
    (=^.^=)(=^.^=)(=^.^=)(=^.^=
"""



