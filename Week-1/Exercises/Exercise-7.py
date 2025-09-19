"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""

def dico(valeur,test, alpha1 , alpha2):
    if valeur < test:
        print('tu es trop haut')
        print("valeur",valeur,"test",test)
        return (alpha2+test)//2 , test , alpha2
    elif valeur > test:
        print('tu es trop bas')
        print("valeur",valeur,"test",test)
        return (alpha1+test)//2 , alpha1 , test

def test(valeur,test):
    if valeur == test:
        print('tu as trouvé')
        return 0
    else:
        return 1
    
vraie_valeur = 31
alpha1 = 100
alpha2 = 0
val_init = alpha1//2
iterateur = 0
while test(vraie_valeur, val_init) == 1:
    iterateur += 1
    val_init, alpha1 , alpha2 = dico(vraie_valeur, val_init, alpha1 , alpha2)
    print('alpha1',alpha1,'alpha2',alpha2 )
    print(val_init)
    print("alors que vv", vraie_valeur)
print("en ", iterateur , 'nombre dessai')

        
