# Polling for pizza:
hungry = True #I need a pizza!
while(hungry):
    print('open the front door')
    front_door = open('front_door.txt','r')
    if "delivery guy" in front_door:
        print('pizza is here')
        hungry = False
    else:
        print("not yet ..")
        print('close front door. ')
        front_door.close()
        
# A brief study in handling life events:
import tkinter
# handler for timer event
def alarm():
    print('calling the pizza company!')
# handler for ringing doorbell
def doorbell():
    print('Ding Dong!')
    print('Open the door')
# handler for when the phone rings:
def phonecall():
    print('Answer the phone')
# create buttons and assign callbacks:
root = tkinter.Tk()
tkinter.Button(root, text = 'Ring Doorbell', command = doorbell).pack()
tkinter.Button(root, text = 'Call Phone', command=phonecall).pack()
# set a timer for 1 second:
root.after(4000, alarm)
# start the event loop:
root.mainloop()