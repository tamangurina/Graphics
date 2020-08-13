from graphics import *
import time
import math

#DDA Line Drawing Algorithm
def drawLineDDA(x1, y1, x2, y2):    

    # creating the window
    winX = 400
    winY = 400
    win = GraphWin('DDA Line', winX, winY)

    # measure the distance
    x,y = x1, y1
    dx = x2 - x1
    dy = y2 - y1

    # calculate the steps
    if abs(dx) > abs(dy):
        stepSize = dx
    else:
        stepSize = dy   

    # calculate the increment for x & y
    xinc = dx / abs(stepSize)
    yinc = dy / abs(stepSize)

    stepSize = abs(stepSize)

    # Line drawing based on point
    #PutPixle(win, x, y)
    for i in range(stepSize):
        x += x_inc
        y += y_inc

        putPixel(win, round(x), round(y))  
        
    win.getMouse()
    win.close()

#Plot pixel
def putPixel(win, x, y):    
    pt = Point(x, y)
    pt.draw(win)


def main():
    drawLineDDA(120,120,330,328)


if __name__ == "__main__":
    main()