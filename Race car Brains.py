from tkinter import *
import time
import math

def turn_left(down):
    global turning_left, turning_right
    turning_right = False
    turning_left = True
    print('left')

def turn_right(down):
    global turning_left, turning_right
    turing_left = False
    turning_right = True
    print('right')

def up_pressed(down):
    global up,accelerating
    accelerating = True

def down_pressed(down):
#    print("down")
    global down_arow, braking
    braking = True

def coast():
    global acceleration, velocity
    acceleration = 0
    if velocity > -0.1:
        if velocity <0.1:
            veloctiy = 0
    if velocity > 0:
        velocity -= 0.1
    elif velocity == 0:
        pass
    elif velocity < 0:
        velocity += 0.1
    time.sleep(0.1)

def accelerate():
    global velocity, acceleration, accelerating, zero_to_sixty
    accelerating = True
    acceleration = zero_to_sixty
    velocity += acceleration
    time.sleep(0.1)
#    print("Accelerating")
    
def brake():
    global  velocity, acceleration, accelerating, braking
    acceleration = 0
    if velocity > 0:
        velocity-= 3
    elif velocity <= 0:
        velocity = 0
    accelerating == False
    time.sleep(0.1)
    braking = False
#    print("Braking")

def main():
    global velocity, acceleration, accelerating, braking, zero_to_sixty, turning_left, turning_right
    direction = 0
    turning_radius = 1
    turning_left = False
    turning_right = False
    acceleration = 0
    accelerating = False
    braking = False
    zero_to_sixty = 0.2
    Height = 795
    Width = 1500
    x = 0
    y = Height/2
    velocity = 0
    tk = Tk()
    pointsize = 10
    tk.title('Brains')
    canvas = Canvas(height = Height, width = Width, bg = 'white')
    canvas.pack()

    while True:
#        print(velocity)
        dx = velocity*math.acos(math.radians(direction))
        dy = velocity*math.asin(math.radians(direction))
        x = x + dx
        y = y + dy

        if accelerating == True:
            accelerate()
            accelerating = False

        elif braking == True:
            brake()

        else:
            coast()

        if turning_left == True:
            direction -= turning_radius

        if turning_right == True:
            direction += turning_radius
        
        if x >= Width or y >= Height:
             x = -x
             acceleration = 0
             
        tk.bind("<Left>", turn_left)
        tk.bind("<Right>", turn_right)
        tk.bind("<Up>", up_pressed)
        tk.bind("<Down>", down_pressed)
        
        point = canvas.create_oval(x,y, x + pointsize, y + pointsize, fill = '#000000' )

        canvas.update()
        canvas.after(1)
        canvas.delete(point)
        

main()
