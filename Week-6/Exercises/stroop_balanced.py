from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, C_GREEN, C_RED, C_BLUE
from expyriment.misc.constants import K_o , K_r , K_g , K_b

from expyriment.misc import Colour
import random
import itertools


exp = design.Experiment(name="Stroop", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)

def derangements(lst): 
    ders = [] 
    for perm in itertools.permutations(lst): 
        if all(original != perm[idx] for idx, original in enumerate(lst)): 
            ders.append(perm)
    return ders

WORDS = ["red", "blue", "green", "orange"]
COLORS_MAP = {
    "red": C_RED,
    "blue": C_BLUE,
    "green": C_GREEN,
    "orange": Colour((255, 165, 0))  
}

PERMS = derangements(WORDS)

trials_list = []

for word in WORDS:
    trials_list.append({
        "trial_type": "match",
        "word": word,
        "color_name": word 
    })

for word, color_name in zip(WORDS, PERMS[0]):
    trials_list.append({
        "trial_type": "mismatch",
        "word": word,
        "color_name": color_name
    })

block = design.Block("Block 1")

for trial_dict in trials_list:
    trial = design.Trial()
    trial.set_factor("trial_type", trial_dict["trial_type"])
    trial.set_factor("word", trial_dict["word"])
    trial.set_factor("color_name", trial_dict["color_name"])
    
    color_obj = COLORS_MAP[trial_dict["color_name"]]
    stim = stimuli.TextLine(trial_dict["word"], text_colour=color_obj, text_size=100)
    trial.add_stimulus(stim)
    trial.preload_stimuli()
    
    block.add_trial(trial)

block.shuffle_trials()
exp.add_block(block)

def run_stroop():

    instructions = stimuli.TextScreen(
        "Instructions", "Press o if it's orange, r if it's red, g if it's green, b if it's blue, please press any key to start.",
        text_colour=C_BLACK
    )
    instructions.present()
    exp.keyboard.wait()
    
    fixation = stimuli.FixCross(size=(50, 50), line_width=10, colour=C_BLACK)
    
    for block_num in range(2):
        for trial_num, trial in enumerate(block.trials):

            trial_type = trial.get_factor("trial_type")
            word = trial.get_factor("word")
            color_name = trial.get_factor("color_name")
            
            fixation.present(clear=True, update=True)
            exp.clock.wait(500)
            
            trial.stimuli[0].present(clear=True, update=True)
            key, rt = exp.keyboard.wait(keys=[K_o , K_r , K_g , K_b])
            
            accuracy = "correct" if key == K_o and color_name == "orange" or key == K_r and color_name == "red" or key == K_g and color_name == "green" or key == K_b and color_name == "blue" else "incorrect"
            exp.data.add([block_num + 1, trial_num + 1, trial_type, word, color_name, 
                         key, rt, accuracy])
    
            feedback_color = C_GREEN if accuracy == "correct" else C_RED
            feedback_text = f"{'Correct' if accuracy == 'correct' else 'Incorrect'} Temps: {rt} ms"
            feedback = stimuli.TextLine(feedback_text, text_colour=feedback_color, text_size=30)
            feedback.present(clear=True, update=True)
            exp.clock.wait(1000)


control.start()

exp.data.add_variable_names(["block", "trial_number", "trial_type", "word", "color_name", "key_pressed", "RT", "accuracy"])

run_stroop()

control.end()