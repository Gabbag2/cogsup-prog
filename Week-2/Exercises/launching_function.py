from expyriment import design, control, stimuli
import expyriment

expyriment.control.defaults.initialise_delay = 0  # No countdown
expyriment.control.defaults.window_mode = True    # Not full-screen
expyriment.control.defaults.fast_quit = True      # No goodbye message

exp = design.Experiment(name="square")
control.initialize(exp)

square_gauche = stimuli.Rectangle(size=(50, 50), colour=(255, 0, 0), position=(-400, 0))  
square_droite = stimuli.Rectangle(size=(50, 50), colour=(0, 255, 0), position=(0, 0)) 

control.start(subject_id=1)

square_gauche.present(clear=True, update=False)  
square_droite.present(clear=False, update=True) 
exp.clock.wait(1000) 

distance_to_move = 200 
animation_duration = 1500  # Animation duration in ms
frame_rate = 60  # Frames per second
frame_delay = 1000 // frame_rate  # Delay between frames (~16.67ms)
num_frames = animation_duration // frame_delay
step_size = distance_to_move / num_frames  # Distance to move each frame

for frame in range(num_frames):
    square_gauche.move((step_size, 0))  # Move by step_size pixels to the right

    # Redraw both squares
    square_gauche.present(clear=True, update=False)
    square_droite.present(clear=False, update=True)
    
    exp.clock.wait(frame_delay)

exp.clock.wait(500)

for frame in range(num_frames):
    square_droite.move((step_size, 0))  # Move by step_size pixels to the right

    square_gauche.present(clear=True, update=False)
    square_droite.present(clear=False, update=True)

    exp.clock.wait(frame_delay/3)

# Step 4: Show final display for 1 second
exp.clock.wait(1000)

exp.keyboard.wait()

control.end()