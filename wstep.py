# Tego kompjuter nje czyta
"""
Ala ma kota,
Kto ma Ale
"""
owca = "Ala ma kota"
owca1 ="Ala ma kota, kot ma Ale i koze krowe"
owca[0] #wybierze pierwszy znak z napisu
owca[0:4] #wyciaga znaki od indeksu 0 do indeksu 3
print(owca1[:24]) #wyciaganie znakow
#sprawdzanie dlugosci
len("napis")
#liczby
#sa dwa typy liczbowe w pythonie int ii float
owcaInt = -5
owcaFloat = 7.5
#ciekawe zapisy
2**5 #32 -> 2 do 5
2e2 # 2x (10 do 2)
2e-2 #2 * (10 do -2)
7%5 # zwrca reszte z dzielenia
#Boolean
prawda = True
falsz = False
##Uwaga roznice
# 1 + "7" zwraca Error
str(1) + "7"
print(1,"7", owca)
#formatowanie napisow
print(f'Ala ma {17} kotow : {prawda}')

