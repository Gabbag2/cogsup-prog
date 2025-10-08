from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, C_GREEN, C_RED , C_BLUE
from expyriment.misc.constants import K_LEFT, K_RIGHT
from expyriment.misc import Colour
import random

exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)

def stroop():
    C_ORANGE = Colour((255, 165, 0))
    for j in range(2):
        for i in range(10):
            stimuli.TextScreen("Instructions", "Press K_right if it's good and K_left if it's bad").present()
        
            fixation = stimuli.FixCross(size=(50, 50), line_width=10, position=[0, 0])
            text = ["red", "blue", "green", "orange"]
            colors = [C_RED, C_BLUE, C_GREEN, C_ORANGE]
            word = random.choice(text)
            color = random.choice(colors)
            stim = stimuli.TextLine(word, text_colour=color, text_size=100)
            fixation.present(True, True)
            exp.clock.wait(500)
            stim.present(True, True)
            key, rt = exp.keyboard.wait(keys = [K_LEFT, K_RIGHT])
            """ trial block, trial number, trial type, word meaning, 
            text color, RTs, and accuracy"""
            type_trial = "good" if (word == "red" and color == C_RED) or (word == "blue" and color == C_BLUE) or (word == "green" and color == C_GREEN) or (word == "orange" and color == C_ORANGE) else "bad"
            accuracy = "True" if (type_trial == "good" and key == K_RIGHT) or (type_trial == "False" and key == K_LEFT) else "False"
            exp.add_data_variable_names(["trial block", "trial number", "trial type", "word meaning", "text color", "RTs", "accuracy"]) 
            exp.data.add([j,i,type_trial,word,color,rt,accuracy]) 
    
control.start(subject_id=1)       
stroop()
control.end()