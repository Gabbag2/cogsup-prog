from expyriment import design, control, stimuli
import expyriment

control.set_develop_mode()

exp = design.Experiment(name="edges")
control.initialize(exp)

size_of_screen,height = exp.screen.size 

taille = 5/100*size_of_screen
square = stimuli.Rectangle(size=(taille, taille), colour=(255, 0, 0), position=(0, 0), line_width=(1)) 
position=[(size_of_screen//2- taille//2,height//2 - taille//2), (-size_of_screen//2 + taille//2, height//2- taille//2),(size_of_screen//2 - taille//2,-height//2 + taille//2),(-size_of_screen//2+ taille//2,-height//2+ taille//2)]

control.start(subject_id=1)

for i in range(4):
    
    if i==0 : 
        square.reposition(position[i]) 
        square.present(clear=True, update=False) 
    
    elif i != 3 and i != 0:
        square.reposition(position[i])
        square.present(clear=False, update=False) 
         
    else :
        square.reposition(position[i]) 
        square.present(clear=False, update=True) 
        


exp.keyboard.wait()

control.end()