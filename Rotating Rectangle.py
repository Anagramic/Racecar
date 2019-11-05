from tkinter import *
import math

def setup():
    global tk, length, radius, canvas,point1,point2,point3,point4,Width,Height
    tk = Tk()
    Height = 1000
    Width = 1000
    length = 100
    radius = math.sqrt((length/2)**2 + (length + length/2)**2)
    angle = math.asin((length/2) / (length + length/2))
    angle = math.degrees(angle)+75
    point1,point2,point3,point4 = find_points(angle)
    tk.title("It's a fuckin' rectangle!!!!!!!!!")
    canvas = Canvas (height = Height, width = Width, bg = 'white')
    canvas.pack()
    rect = canvas.create_polygon(point1,point2,point3,point4, fill = 'red')
    canvas.update()
    main()

def left_keydown(down):
    global angle,point1,point2,point3,point4 
    angle += 1
    point1, point2, point3, point4 = find_points(angle)
    canvas.delete('all')
    canvas.create_polygon(point1,point2,point3,point4, fill = 'red')
    canvas.update()
    print('Left')

def right_keydown(down):
    global angle,point1,point2,point3,point4
    angle -= 1
    point1, point2, point3, point4 = find_points(angle)
    canvas.delete("all")
    canvas.create_polygon(point1,point2,point3,point4, fill = 'red')
    canvas.update()
    print('Right')

def find_points(angle):
    global radius
    all_points = []

    angle = math.radians(angle)
    
    x = radius*math.sin(angle)
    y = radius*math.cos(angle)
    point1 =((Width/2) +x,(Height/2) +y)      
    point3 = ((Width/2) -x,(Height/2) -y)
    
    angle = 180-angle
    x = radius*math.sin(angle)
    y = radius*math.cos(angle)
    
    point2 = ((Width/2) -x,(Height/2)+y)
    point4 =((Width/2) +x,(Height/2) -y)
    

    return(point1,point2,point3,point4)
    
def main():
    global angle
    tk.bind("<Left>",left_keydown)
    tk.bind("<Right>",right_keydown)
    angle = math.asin((length/2) / (length + length/2))
    angle = math.degrees(angle)

       
        
    tk.mainloop()

setup()

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, cHeight, cWidth, angle):
        self.width = 0
        self.angle = angle
