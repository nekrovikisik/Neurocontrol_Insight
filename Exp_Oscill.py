import time

from psychopy import visual, core, event, gui, data #import some libraries from PsychoPy
from psychopy.visual.circle import Circle
from psychopy.hardware import keyboard

exp_info = {}
exp_name = 'Case 2'
dlg = gui.DlgFromDict(dictionary=exp_info, title=exp_name)

exp_info = {
            'email': '',
            'gender': ('male', 'female'),
            'age':tuple(range(18, 41))
            }
stimFreq = {'left': 8.57, 'right': 10, 'forward': 12, 'back': 15} # if monitor with a 60 Hz refresh rate

# get info by user
exp_info['date'] = data.getDateStr()
exp_info['date'] = data.getDateStr()

def fixation():
    cross = visual.TextStim(win, text='+', color='red', height=20)
    cross.pos = (0, 0)
    cross.draw()


def start(win):
    text = visual.TextStim(win, text='Press spacebar to start the trial', color='red', height=20)
    pass
def addStimulus():
    visual.circle.Circle(win, radius=3, pos=(0.5, 1))

win = visual.Window([800,600],monitor="testMonitor", units="deg", fullscr=True)

timer2 = core.Clock()
timer2.add(5)

timer = core.Clock()
timer.add(1/60)

 #ToDo: class Circle
# stimFreq = {'left': 8.57, 'right': 10, 'forward': 12, 'back': 15} # if monitor with a 60 Hz refresh rate
countFrames = 0

stims = [visual.circle.Circle(win=win, lineColor='black', fillColor='black', units='norm', pos=(-0.5, 0), radius=0.1),
    visual.circle.Circle(win=win, lineColor='black', fillColor='black', units='norm', pos=(0.5, 0), radius=0.1),
    visual.circle.Circle(win=win, lineColor='black', fillColor='black', units='norm', pos=(0, 0.5), radius=0.1),
    visual.circle.Circle(win=win, lineColor='black', fillColor='black', units='norm', pos=(0, -0.5), radius=0.1)]

# stim_left = visual.circle.Circle(win=win, lineColor='black', fillColor='black', units='norm', pos=(-0.5, 0), radius=0.1)
# stim_right = visual.circle.Circle(win=win, lineColor='black', fillColor='black', units='norm', pos=(0.5, 0), radius=0.1)
# stim_top = visual.circle.Circle(win=win, lineColor='black', fillColor='black', units='norm', pos=(0, 0.5), radius=0.1)
# stim_bottom = visual.circle.Circle(win=win, lineColor='black', fillColor='black', units='norm', pos=(0, -0.5), radius=0.1)

[stim.draw() for stim in stims]
# stim_left.draw();
# stim_right.draw();
# stim_top.draw();
# stim_bottom.draw()
win.flip()

keys = []
fps = 60
time_delta = 1./fps
freq = [15, 12, 10, 8.57]
timestamps = [4, 5, 6, 7] # каждую i-тую секунду меняется цвет

mytime = 0
arr = []
count = 0 # count of frames
t0 = time.clock()
while 'escape' not in keys and 'q' not in keys : #ToDo add the exit key
    keys = event.getKeys()

    t1 = time.clock()
    # mytime = t1-t0
    time.sleep(time_delta)
    count += 1
    for i in timestamps:
        if count % int(i) == 0:
            stims[i].color = 'black'
            arr.append(i)

    # stim_left = visual.circle.Circle(win=win, lineColor='black', fillColor='red', units='norm', pos=(-0.5, 0), radius=0.1)
    # stim_right = visual.circle.Circle(win=win, lineColor='black', fillColor='red', units='norm', pos=(0.5, 0), radius=0.1)
    # stim_top = visual.circle.Circle(win=win, lineColor='black', fillColor='red', units='norm', pos=(0, 0.5), radius=0.1)
    # stim_bottom = visual.circle.Circle(win=win, lineColor='black', fillColor='red', units='norm', pos=(0, -0.5), radius=0.1)
    #
    # stim_left.draw();stim_right.draw();stim_top.draw();stim_bottom.draw()

win.close()
core.quit()

'''
Flash frequency = refreshrate/(frame_on+frame_off)



'''