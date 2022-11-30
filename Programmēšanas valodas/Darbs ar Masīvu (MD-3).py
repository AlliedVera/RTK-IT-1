import numpy as np

def check(count, Data): #visu datu izvades funkcija
    print('\nN.pk.''\tVārds', '\tUzvārds', 'Vecums', '\tAugums', '\tDzimums')
    while count!=Data.shape[0]: #data.shape, pasaka cik daudz rindu masīvā
        print(" {}.\t".format(count + 1), "\t".join(Data[count]))
        count=count+1
        
def checkAlt(count, Data, amountInt): #konkrēta daudzuma datu izvades funkcija
    print('\nN.pk''\tVārds', '\tUzvārds', 'Vecums', '\tAugums', '\tDzimums')
    while count!=amountInt: 
        print(" {}.\t".format(count + 1), "\t".join(Data[count]))
        count=count+1

def create(Data):#Datu izveides funkcija
    print("Ievadiet prasīto informāciju")
    name = input("Vārds - ")
    surname = input("Uzvārds - ")
    age = int(input("Vecums - "))
    height = float(input("Augums - "))
    if height > 3:#ja ievadītais skaitlis lielāks par 3, tad secināt, ka ievadīti cm
        height = height / 100 #tādā gadījumā izdala ar 100, lai iegūtu metrus
    gender = input("Dzimums(M/F) - ")#Paļaujos uz lietotāja kompetenci 
    newData = np.append(Data, [[name, surname, age, height, gender]], axis=0)#ievadīto ielieku jaunā mainīgajā
    return newData#atgriežu mainīgo ārpus funkcijas

Data = np.array([['John', 'Doe', 11, 1.80, 'M'],
     ['Mark', 'Gate', 24, 1.65, 'M'],
     ['Tom', 'Xin', 18, 1.90, 'M'],
     ['Sarah', 'Blake', 14, 2.00, 'F'],
     ['Otto', 'Ming', 19, 1.95, 'M'],
     ['Lee', 'Gato', 20, 1.88, 'M'],
     ['Kate', 'Cote', 21, 1.60, 'F'],
     ['Marta', 'Bell', 16, 1.78, 'F'],
     ['Alice', 'York', 15, 1.65, 'F'],
     ['Colm', 'Pete', 25, 1.99, 'M']])
choice = int #izvēles mainīgais
count = int(0) #mainīgais, kas skaita cikla izpildes

while choice!= 3: #cikls, kurš beigsies, kad lietotājs ievadīs skailti 3
    print("\nNospiediet:\n1 - Lai apskatītu datus\n2 - Lai pievienotu jaunus datus\n3 - Lai beigtu darbu")
    choice = int(input())
    if choice == 1:#izpildās cikls ciklā, lai noteiktu izvadāmo datu daudzumu(negluži cikls)
        amount = input("Cik datu rindas vēlaties apskatīt?\nJa visas - spied taustiņu \"Enter\"\n")
        if amount == '' or int(amount) > Data.shape[0] :#pielaboju šo rindu, lai strādātu arī kad lietotājs ievada lielāku rindu skaitu, nekā programma var izvadīt
            check(count, Data)#tiek palaista pirmā apskates funkcija
        else:
            amountInt = int(amount)#nomaina mainīgo no string uz integer
            checkAlt(count, Data, amountInt)#tiek palaista otrā apskates funkcija
    elif choice == 2:#tiek palaista datu ievades funkcija
        newData = create(Data)#mainīgais newData vienāds ar funkcijas create(Data) atgriezto vērtību
        Data = newData#mainīgais newData tiek pārsaukts par globālo mainīgo Data

print("Darba beigas")
