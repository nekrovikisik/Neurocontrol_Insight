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

def start(win):
    text = visual.TextStim(win, text='Press spacebar to start the trial', color='red', height=20)

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
while timer2.getTime() <= 5: #ToDo add the exit key
    keys = event.getKeys()
    print(timer.getTime())
    if timer.getTime() / (1/60) == float(timer.getTime() // (1/60)):
        countFrames += 1
        timer.reset()
        timer.add(1 / 60)
    if countFrames == 7:
        stim_left.draw()
        print('7')
        win.flip()
    if countFrames == 6:
        stim_right.draw()
        win.flip()
        print('6')

    if countFrames == 5:
        stim_top.draw()
        win.flip()
        print('5')

    if countFrames == 4:
        stim_bottom.draw()
        print('4')

        win.flip()

    stim_left = visual.circle.Circle(win=win, lineColor='black', fillColor='red', units='norm', pos=(-0.5, 0), radius=0.1)
    stim_right = visual.circle.Circle(win=win, lineColor='black', fillColor='red', units='norm', pos=(0.5, 0), radius=0.1)
    stim_top = visual.circle.Circle(win=win, lineColor='black', fillColor='red', units='norm', pos=(0, 0.5), radius=0.1)
    stim_bottom = visual.circle.Circle(win=win, lineColor='black', fillColor='red', units='norm', pos=(0, -0.5), radius=0.1)

    stim_left.draw();stim_right.draw();stim_top.draw();stim_bottom.draw()

win.close()
core.quit()

