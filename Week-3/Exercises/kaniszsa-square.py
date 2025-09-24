from expyriment import design, control, stimuli
from expyriment.misc import constants


import expyriment

control.set_develop_mode()

black = constants.C_BLACK
white = constants.C_WHITE
grey  = constants.C_GREY

exp = design.Experiment(name="edges" , background_colour = grey )
control.initialize(exp)



widht,height = exp.screen.size 

taille_carre = 25/100*widht
radius_circle = 5/100*widht

control.start(subject_id=1)
square = stimuli.Rectangle(size=(taille_carre, taille_carre), colour = grey, position=(0, 0)) 

circle = stimuli.Circle(radius=radius_circle, colour = white)


tab = []
for i in (taille_carre,-taille_carre):
    for j in (taille_carre, -taille_carre):
        tab.append((i,j))
        
for i,(j,k) in enumerate(tab):
    
    if i != 0 :
        circle.reposition((j//2,k//2))
        circle.present(clear=False, update=False)
         
    else :
        circle.reposition((j//2,k//2)) 
        circle.present(clear=True, update=False)
        
    if (i+1)%2 == 0 : 
        circle.colour = black

square.present(clear=False, update=True)

exp.keyboard.wait()

control.end()