from expyriment import design, control, stimuli
import expyriment
import math

expyriment.control.defaults.initialise_delay = 0 # No countdown
expyriment.control.defaults.window_mode = True # Not full-screen
expyriment.control.defaults.fast_quit = True # No goodbye message


exp = design.Experiment(name = "square")

control.initialize(exp)

pi = math.pi
r = 33.333
triangle = stimuli.Shape(
    colour=(128, 0, 128),
    vertex_list = [(r*math.cos(math.pi/2), r*math.sin(math.pi/2)),
    (r*math.cos(7*math.pi/6), r*math.sin(7*math.pi/6)),     
    (r*math.cos(11*math.pi/6), r*math.sin(11*math.pi/6))],
    position=(-200, 0)   
)
test= [(r*math.cos(math.pi/2), r*math.sin(math.pi/2)),
    (r*math.cos(7*math.pi/6), r*math.sin(7*math.pi/6)),     
    (r*math.cos(11*math.pi/6), r*math.sin(11*math.pi/6))]
print(test)
tab = []
r2=25
for i in range(6):
    tab.append((r2*math.cos(math.pi+pi/3*i),(r2*math.sin(math.pi+pi/3*i))))

polygone = stimuli.Shape(colour=(128, 128, 0), 
                         position=(200, 0),
                         vertex_list=tab
                         )

trait_tri = stimuli.Line(line_width = 3 ,start_point= (-200+r*math.cos(math.pi/2), r*math.sin(math.pi/2)) ,end_point= (-200+r*math.cos(math.pi/2), r*math.sin(math.pi/2)+50))
trait_ply = stimuli.Line(line_width = 3 ,start_point = (200,tab[-1][1]),end_point = (200,tab[-1][1]+50))
nom_tri = stimuli.TextLine(text="triangle", position=(r*math.cos(math.pi/2)-200, r*math.sin(math.pi/2)+50))
nom_ply = stimuli.TextLine(text="polygone", position=(200,tab[-1][1]+52))
control.start(subject_id=1)

triangle.present(clear=True, update=False)
trait_tri.present(clear=False, update=False)
trait_ply.present(clear=False, update=False)
nom_tri.present(clear=False, update=False)
nom_ply.present(clear=False, update=False)
polygone.present(clear=False, update=True)

exp.clock.wait(2000)
exp.keyboard.wait()

control.end()