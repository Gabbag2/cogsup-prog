from expyriment import design, control, stimuli
import expyriment

expyriment.control.defaults.initialise_delay = 0 # No countdown
expyriment.control.defaults.window_mode = True # Not full-screen
expyriment.control.defaults.fast_quit = True # No goodbye message


exp = design.Experiment(name = "square")

control.initialize(exp)

square_gauche = stimuli.Rectangle(size=(50, 50), colour=(0, 255, 0), position= (-100,0))
square_droite = stimuli.Rectangle(size=(50, 50), colour=(255, 0, 0), position=(100, 0))

control.start(subject_id=1)

square_gauche.present(clear=True, update=False)
square_droite.present(clear=False, update=True)

exp.keyboard.wait()

control.end()