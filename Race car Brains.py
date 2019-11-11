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
    turning_radius = 5
    turning_left = False
    turning_right = False
    acceleration = 0
    accelerating = False
    braking = False
    zero_to_sixty = 0.2
    Height = 795
    Width = 1500
    grid_xsf = Width/100
    grid_ysf = Height/100
#staring location
    x = 0
    y = Height/2

    dx = 0
    dy = 0
    velocity = 0
    tk = Tk()
    pointsize = 10
    tk.title('Brains')
    canvas = Canvas(height = Height, width = Width, bg = 'white')
    canvas.pack()

    while True:
#        print('--------------------------------------------------------------------------------')
#        print('v: '+str(velocity))
#        print('x: '+str(x))
#        print('y: '+str(y))
#        print('dx: '+str(dx))
#        print('dy: '+str(dy))
#        print('Direction: '+str(direction))
        if x >= Width or y >= Height:
             velocity = 0  
             acceleration = 0
             
        dx = velocity*math.cos(math.radians(direction))
        dy = velocity*math.sin(math.radians(direction))
        x = x + dx
        y = y + dy
#        print(x)
#        print(y)

             
        if accelerating == True:
            accelerate()
            accelerating = False

        elif braking == True:
            brake()

        else:
            coast()

        if turning_left == True:
            direction -= turning_radius
            turning_left = False
        if turning_right == True:
            direction += turning_radius
            turning_right = False       


        tk.bind("<Left>", turn_left)
        tk.bind("<Right>", turn_right)
        tk.bind("<Up>", up_pressed)
        tk.bind("<Down>", down_pressed)
        
        arrow = canvas.create_line(x,y,x+(dx*5),y+(dy*5),fill = '#000000')
        point = canvas.create_oval(x,y, x + pointsize, y + pointsize, fill = '#000000' )

        canvas.update()
        canvas.after(1)
        canvas.delete(point,arrow)
        

main()
