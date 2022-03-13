from tkinter import *
import time
import math
def create_track():
    create_grid()

def reset():
    global acceletration, velocity, direction, x, y
    acceleration = 0
    velocity = 0
    x = 0
    y = Height/2


def create_grid():
    global grid_xsf, grid_ysf
    grid_xsf = Width/200
    grid_ysf = Height/200

def grid(grid_position_x, grid_position_y):
    x = grid_position_x * grid_xsf
    y = grid_position_y * grid_ysf
    return(x,y)
    
def turn_left(down):
    global turning_left, turning_right
    turning_right = False
    turning_left = True
#    print('left')

def turn_right(down):
    global turning_left, turning_right
    turing_left = False
    turning_right = True
#    print('right')

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
    global velocity, acceleration, accelerating, braking, zero_to_sixty, turning_left, turning_right, Width, Height
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
#staring location
    x = 0
    y = Height/2

    create_track()
    dx = 0
    dy = 0
    velocity = 0
    tk = Tk()
    pointsize = 10
    tk.title('Brains')
    canvas = Canvas(height = Height, width = Width, bg = 'white')
    canvas.pack()
    create_track()
    

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
        tk.bind("<space>", reset)
        
        arrow = canvas.create_line(x,y,x+(dx*5),y+(dy*5),fill = '#000000')
        point = canvas.create_oval(x,y, x + pointsize, y + pointsize, fill = '#000000' )

        canvas.update()
        canvas.after(1)
        canvas.delete(point,arrow)
        

main()
