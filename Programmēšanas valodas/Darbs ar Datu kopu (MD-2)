from functools import reduce 
# ^ importēju vienu elemento no bibliotēkas, kas cikliski veiks darbības ar Masīvu/List, līdz pēdējam masīva simbolam.

def summa(n):
    print("Ievadīto Sešu skaitļu summa =", reduce(lambda x,y: x+y, n))
def starpiba(n):
    print("Ievadīto Sešu skaitļu starpība =", reduce(lambda x,y: x-y, n))
def reizinajums(n):
    print("Ievadīto Sešu skaitļu dalījums =", reduce(lambda x,y: x*y, n))
def dalijums(n):
    print("Ievadīto Sešu skaitļu reizinājums =", reduce(lambda x,y: x/y, n))

n = [] #nodefinēju mainīgo "n", kā masīvu/list

print("---Sešu skaitļu secīgu aritmētisko darbību kalkulators---") #pirmā programmas izvades rinda
while len(n)<6: #Atkārtot komandas līdz masīva garums nepārsniedz 6(0->5), iepriekš izmantoju "while c<int(7):"
    print("Ievadi {}. Skaitli".format(len(n)+1)) #skaitu mainīgā garumu + 1, jo sākas no 0
    t = int(input()) #ievadītā vērtība, noteikta par integrāli. Varbūt labāk izmantot "float"
    n.append(t) #pievienoju iepriekš iegūto vērtību pie, jau definē†ā masīva
print(n) #izvadu masīvu ārpus cikla, lai tiktu izvadīts tikai vienu reizi
    


Symbol = int(input("Ievadi Veicamās darbības skaitli \n1.\"+\" \n2.\"-\" \n3.\":\" \n4.\"*\" "))
# ^ ar /n sadalu rindās, lai pārredzamāk, un ar "\" norādu, ka pēdiņas nav jāņem vērā ārpus stringa

if Symbol == 1:
    summa(n)
elif Symbol == 2:
    starpiba(n)
elif Symbol == 3:
    dalijums(n)
elif Symbol == 4:
    reizinajums(n)
# ^ attiecīgi no ievadītās vērtības izpildīt norādīto funkciju  
