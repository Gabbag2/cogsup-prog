from expyriment import design, control, stimuli

def draw(stims): 
    """Draw a sequence of stimuli in order and show on-screen.""" 
    if not stims: 
        raise ValueError("Stimuli list must be nonempty.") 
    # Clear the back buffer and draw the first stimulus 
    stims[0].present(clear=True, update=False) 
    # Continue drawing the middle stimuli 
    for stim in stims[:-1]: 
        stim.present(clear=False, update=False) 
        # Add the last stimulus and swap the buffers 
        stims[-1].present(clear=False, update=True)


exp = design.Experiment(name="Square")

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
square = stimuli.Rectangle(size=(100, 100), line_width=5)

control.start(subject_id=1)

draw([fixation,square])
  
exp.clock.wait(500)

exp.keyboard.wait()
 
control.end()