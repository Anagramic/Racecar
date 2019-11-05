from tkinter import *
import time

def turn_left(down):
    print('left')

def turn_right(down):
    print('right')

def up_pressed(down):
    global up
    accelerating = True

def down_pressed(down):
    global down_arow
    braking = True

def coast():
    global acceleration, velocity
    acceleration = 0
    velocity -= 0.1
    time.sleep(0.1)

def accelerate(down):
    global velocity, acceleration, accelerating
    accelerating == True
    acceleration = 0.2
    velocity += acceleration
    time.sleep(0.1)
    print("up")
    
def brake(down):
    global  velocity, acceleration
    acceleration = 0
    if velocity <= 0:
        velocity-= 3
#    else:
#        acceleration-=0.2
#        velocity+=acceleration
    print("down")
    accelerating == False
    time.sleep(0.2)

def main():
    global velocity, acceleration, accelerating, braking    
    acceleration = 0
    Height = 795
    Width = 500
    x = Width/2
    y = Height/2
    velocity = 0
    tk = Tk()
    pointsize = 10
    tk.title('Brains')
    canvas = Canvas(height = Height, width = Width, bg = 'white')
    canvas.pack()

    while True:
        print(velocity)
        x = x + velocity
        if accelerating == False:
            coast()
        if down_pressed == False:
            pass
        if x >= Width or y >= Height:
            velocity = 0
            acceleration = 0
        tk.bind("<Left>", turn_left)
        tk.bind("<Right>", turn_right)
        tk.bind("<Up>", up_pressed)
        tk.bind("<Down>", down_pressed)
        
        point = canvas.create_oval(x,y, x + pointsize, y + pointsize, fill = '#000000' )

        canvas.update()
        canvas.after(3)
        canvas.delete(point)
        



    
main()
