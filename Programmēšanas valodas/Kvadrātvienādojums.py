import math #importēju moduli, kas māk aprēķināt kvadrātsakni

print('ax^2+bx+c=0 ')

#Mainigo ievade
a = int(input('ievadi a: '))
if a == 0:
    print('a nevar būt 0.  Ievadi citu sakni') #Neļauj atstāt "0", kā "a" vērtību, un prasa ievadīt vēlreiz
    a = int(input()) #Ja 0 ievadīs otro reizi, tad programma ies tālāk xD

b = int(input('ievadi b: '))
c = int(input('ievadi c: '))


#Mainīgo izvade aizstājot burtus ar atiecīgi ievadītajiem cipariem.
print('Saknes tiek aprēķinātas vienādojumam  {}x^2+{}x+{}=0'.format (a, b, c))


D = b*b - (4 * a * c)  #Diskriminanta formula

#Trīs uzdevuma izpildes iespējas
if D < 0:
    print('Diskriminants negatīvs - sakņu nav.')

elif D == 0:
    x1 = (-b+math.sqrt(D))/2*a
    print('Diskriminants = 0, Risinājumam tikai viena sakne \nX=', x1)

elif D > 0:
    print('Diskriminants ir =', D)
    x1 = (-b+math.sqrt(D))/2*a
    print('x1 =', x1)
    x2 = (-b-math.sqrt(D))/2*a
    print('x2 =', x2)
