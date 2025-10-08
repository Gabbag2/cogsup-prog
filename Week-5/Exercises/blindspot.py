from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK
from expyriment.misc.constants import K_DOWN, K_UP, K_LEFT, K_RIGHT, K_SPACE, K_1, K_2

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
def make_circle(r, pos=(0,0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=100)
    "c.preload()"
    return c 

""" Experiment """
def run_trial():
    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[300, 0])
    fixation.preload()
    stimuli.TextScreen("Instructions", "Press SPACE when you found your blind spot and press 1 for larger, 2 for smaller and the direction ").present()
    radius = 75
    circle = make_circle(radius)

    fixation.present(False, True)
    circle.present(False, True)
    modifications(circle, fixation)
    exp.keyboard.wait()

def modifications(circle, fixation):
    "(position: keyboard arrows; size: 1 = smaller, 2 = larger)"
    test = True
    while test == True :
        key, rt = exp.keyboard.wait(keys = [K_DOWN, K_UP, K_LEFT, K_RIGHT, K_SPACE, K_1, K_2])
        if key == K_SPACE:
            test = False
        elif key == K_UP:
            circle.move((0, 10))
        elif key == K_DOWN:
            circle.move((0, -10))
        elif key == K_LEFT:
            circle.move((-10, 0))
        elif key == K_RIGHT:
            circle.move((10, 0))
        elif key == K_1:
            circle.scale(1.2)
        elif key == K_2:
            circle.scale(0.8)
        circle.present(True, False)
        fixation.present(False, True) 
        """x, y = circle.position
            radius = circle.radius
            exp.add_data_variable_names(["which_eye", "x", "y", "radius"]) 
            exp.data.add(["left", x, y, radius]) """
    x, y = circle.position
    radius = circle.radius
    exp.add_data_variable_names(["which_eye", "x", "y", "radius"]) 
    exp.data.add(["left", x, y, radius]) 

        

control.start(subject_id=1)

run_trial()
    
control.end()