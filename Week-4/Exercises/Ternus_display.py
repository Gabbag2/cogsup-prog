from expyriment import design, control, stimuli
from expyriment.misc import constants
from expyriment.misc.constants import K_SPACE # top of script 



def termus(radius, ISI ,color_tags = None, duration_circle = 200 ):
    
    global exp
    i=1
    while True: 
        i = i+1
        position = i % 2
        circle(radius = radius , position = position, color_tags = color_tags)

        exp.clock.wait(duration_circle)
        
        image_blanc()
        exp.clock.wait(ISI)
        if exp.keyboard.check(K_SPACE):
            break
            
        exp.clock.wait(duration_circle)
        image_blanc()
        exp.clock.wait(ISI)
        if exp.keyboard.check(K_SPACE):
            break
        

def circle(radius=50, position=1, color_tags=None):
    global exp
    width, height = exp.screen.size
    espace_inter = (width - 4*radius) / 5
    
    # Calculer les positions
    tab = []
    for i in range(4):
        if i == 0:
            tab.append((-(espace_inter*1.5 + radius*1.5), 0))
        else:  # CORRECTION: else ajouté ici
            tab.append((tab[-1][0] + radius + espace_inter, 0))
    
    # Choisir les indices
    if position == 1:
        indices = [0, 1, 2]
    else:
        indices = [1, 2, 3]
    
    # Dessiner les cercles
    for idx, i in enumerate(indices):
        # Cercle noir
        circle_obj = stimuli.Circle(radius=radius, position=tab[i], colour=constants.C_BLACK)
        
        if idx == 0:
            circle_obj.present(clear=True, update=False)
        else:
            circle_obj.present(clear=False, update=False)
        
        if color_tags is not None:
            fixed_indices = [0, 1, 2, 3] 
            for idx, i in enumerate(fixed_indices):
                if position == 1 and i == 3:
                    continue
                if position == 0 and i == 0:
                    continue
                small_circle = stimuli.Circle(radius=radius/5, position=tab[i], colour=color_tags[idx])
                small_circle.present(clear=False, update=False)
    
    # Update à la fin
    exp.screen.update()
            
    
def image_blanc():
    global exp
    width,height = exp.screen.size
    square = stimuli.Rectangle(size=(width,height), colour = constants.C_WHITE)
    square.present(clear=True, update=True)


exp = design.Experiment(name="Ternus", background_colour = constants.C_WHITE)
control.set_develop_mode()
control.initialize(exp)
color_tags = [constants.C_RED, constants.C_GREEN, constants.C_BLUE, constants.C_RED]
termus(radius = 50, ISI = 100, color_tags = color_tags , duration_circle = 200)