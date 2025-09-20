# Import the main modules of expyriment
from expyriment import design, control, stimuli
import expyriment
"""expyriment.control.defaults.initialise_delay = 0 # No countdown
expyriment.control.defaults.window_mode = True # Not full-screen
expyriment.control.defaults.fast_quit = True # No goodbye message"""



exp = design.Experiment(name = "square")

control.initialize(exp)

fixation = stimuli.FixCross()

square = stimuli.Rectangle(size=(50, 50), colour=(0, 0, 255))

control.start(subject_id=1)

square.present(clear=True, update=False)
fixation.present(clear=False, update=True)


exp.clock.wait(500)

square.present(clear=True, update=True)

exp.keyboard.wait()

control.end()