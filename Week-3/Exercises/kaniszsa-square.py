from expyriment import design, control, stimuli
import expyriment

control.set_develop_mode()

exp = design.Experiment(name="edges")
control.initialize(exp)

widht,height = exp.screen.size 

taille_carre = 25/100*widht
radius_circle = 5/100*widht

control.start(subject_id=1)
square = stimuli.Rectangle(size=(taille_carre, taille_carre), colour=(255, 0, 0), position=(0, 0), line_width=(10)) 
square.present(clear=True, update=False)
circle = stimuli.Circle(radius=radius_circle, line_width=(10))

tab = []
for i in (taille_carre,-taille_carre):
    for j in (taille_carre, -taille_carre):
        tab.append((i,j))
        
for i,(j,k) in enumerate(tab):
    
    if i != 3 :
        circle.reposition((j,k))
        circle.present(clear=False, update=False)
         
    else :
        circle.reposition((j,k)) 
        circle.present(clear=False, update=True)
     

exp.keyboard.wait()

control.end()