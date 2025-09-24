"""The program should have 
customizable parameters for square 
size, space between squares, 
number of rows, number of 
columns, square color, and 
background color
"""

from expyriment import design, control, stimuli
from expyriment.misc import constants
import expyriment

"""control.set_develop_mode()"""

black = constants.C_BLACK
white = constants.C_WHITE
grey  = constants.C_GREY




def hermann(square_size = 100 , space_between = 50, rows = 5, columns = 5, square_color = white , background_color = black):
    
    exp = design.Experiment(name="edges" , background_colour = background_color )
    control.initialize(exp)
    control.start(subject_id=1)
    
    square = stimuli.Rectangle(size=(square_size, square_size), colour = square_color, position=(0, 0)) 
    width,height = exp.screen.size
    
   
    valeur = space_between + square_size
    total_largeur2 = columns * (valeur)
    total_longueur2 = rows * (valeur)
    total_largeur = columns * square_size + (columns - 1) * space_between
    total_longueur = rows * square_size + (rows - 1) * space_between
    
    tab = []
    for i in range(columns):
        for j in range(rows):
            tab.append((total_largeur//2 - square_size//2 - j*valeur , total_longueur//2 - square_size//2 - i*valeur))
            
    print(len(tab))
    
    for i,(j,k) in enumerate(tab):
        
        
        if i == 0:
            square.reposition((j,k))
            square.present(clear=True, update=False)
            
        elif i != rows*columns-1 :
            square.reposition((j,k))
            square.present(clear=False, update=False)
            
        else :
            square.reposition((j,k)) 
            square.present(clear=False, update=True)


    exp.keyboard.wait()

    control.end()
    
hermann(square_size = 100 , space_between = 50, rows = 5, columns = 5, square_color = white , background_color = black)