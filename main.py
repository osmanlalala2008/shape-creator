import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((800, 600))

radius = 100.0
rgb_values = 3
shape_color = []
bg_color = []
black_color = (0, 0, 0)
see_shape_properties = None
radius_Input = None

def bg_color_func():
    for value in range(rgb_values):
        bg_color.append(int(input("Enter a color value: ")))
    tuple(bg_color)

bg_color_input = input("Do you want to change the background color? ")

if bg_color_input == "yes":
    bg_color_func()
    DISPLAYSURF.fill(bg_color)

elif bg_color_input == "no":
    DISPLAYSURF.fill(black_color)

def color_edit():
    for value in range(rgb_values):
        shape_color.append(int(input("Enter a color value: ")))
    tuple(shape_color)
shape_input = input("Enter a name of a shape from the following: \ncircle\nrectangle\nsquare\nparallelogram\nyour choice: ")

if shape_input == "circle":
    circle_edit = input("Do you want to edit the circle's properties? ")

    if circle_edit == "yes":
        radius_Input = int(input("radius: "))
        width_input = int(input("width: "))
        color_edit()
        pygame.draw.circle(DISPLAYSURF, shape_color, (400, 300), radius_Input, width_input)
        see_shape_properties = input("Do you want to seee the shape's properties? ")

    if see_shape_properties == "yes":
        area = (22/7) * (radius_Input * radius_Input)
        print("area: ", area)
        circumference = 2 * (22/7) * radius_Input
        print("circumference: ", circumference)
        diameter = radius_Input * 2
        print("diameter: ", diameter)

    elif circle_edit == "no":
        pygame.draw.circle(DISPLAYSURF, (255, 255, 255), (400, 300), radius, 10)
        see_shape_properties = input("Do you want to seee the shape's properties? ")

        if see_shape_properties == "yes":
            area = (22/7) * (radius * radius)
            print("area: ", area)
            circumference = 2 * (22/7) * radius
            print("circumference: ", circumference)
            diameter = radius * 2
            print("diameter: ", diameter)

elif shape_input == "rectangle":
    rectangle_edit = input("Do you want to edit the rectangle's properties? ")

    if rectangle_edit == "yes":
        width = int(input("breadth: "))
        height = int(input("height: "))
        border_size = int(input("border_size: "))
        color_edit()
        pygame.draw.rect(DISPLAYSURF, shape_color, (400, 300, width, height), border_size)
        see_shape_properties = input("Do you want to seee the shape's properties? ")

        if see_shape_properties == "yes":
            area = width * height
            print("area: ", area)

    elif rectangle_edit == "no":
        width = 100
        height = 200
        pygame.draw.rect(DISPLAYSURF, (255, 255, 255), (400, 300, width, height), 10)
        see_shape_properties = input("Do you want to seee the shape's properties? ")

        if see_shape_properties == "yes":
            area = width * height
            print("area: ", area)

elif shape_input == "square":
    square_edit = input("Do you want to edit the square's properties? ")
    
    if square_edit == "yes":
        side = float(input("side lenght: "))
        width = int(input("width: "))

        while side != width:
            print("error: Invalid dimensions for square")
            print("try again......")
            side = float(input("side lenght: "))
            width = int(input("width: "))

        color_edit()
        pygame.draw.rect(DISPLAYSURF, shape_color, (400, 300, side, side), width)
        see_shape_properties = input("Do you want to seee the shape's properties? ")

        if see_shape_properties == "yes":
            area = side * width
            print("area: ", area)

    elif square_edit == "no":
        width = 150
        height = 150
        pygame.draw.rect(DISPLAYSURF, (255, 255, 255), (400, 300, width, height), 10)
        see_shape_properties = input("Do you want to seee the shape's properties? ")

        if see_shape_properties == "yes":
            area = width * height
            print("area: ", area)

elif shape_input == "parallelogram":
    parallelogram_edit = input("Do you want to edit the parallelogram's properties?")

    if parallelogram_edit == "no":
        pygame.draw.polygon(DISPLAYSURF, (255, 255, 255), ((100, 100), (600, 100), (700, 500), (200, 500)), 10)

    elif parallelogram_edit == "yes":
        color_edit()
        pygame.draw.polygon(DISPLAYSURF, shape_color ((100, 100), (600, 100), (700, 500), (200, 500)), 10)

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
