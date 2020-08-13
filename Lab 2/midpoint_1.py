import math
import matplotlib.pyplot as plt

pointListX = []
pointListY = []

def drawLineMidPoint(x1,y1,x2,y2):
    x,y = x1, y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    print(f'x = {x}, y = {y}') 
    plt.plot(x, y, 'bo')
    pointListX.append(x)
    pointListY.append(y) 

    if dx > dy:
        p = dy - (dx / 2)
        for k in range(0, dx):            
            if p > 0:
                y = y + 1 if y < y2 else y - 1
                p = p + dy - dx
            else:                
                y = y
                p = p + dy 
            x = x + 1 if x < x2 else x - 1 
            print(f'x = {x}, y = {y}') 
            plt.plot(x, y, 'bo')          
            pointListX.append(x)
            pointListY.append(y) 
    else:
        p = dx - (dy / 2)
        for k in range(0, dy):            
            if p > 0:
                x = x + 1 if x < x2 else x - 1
                p = p + dx - dy
            else: 
                p = p + dx
            y = y + 1 if y < y2 else y - 1
            print(f'x = {x}, y = {y}') 
            plt.plot(x, y, 'bo')          
            pointListX.append(x)
            pointListY.append(y) 

def main():
    #drawLineMidPoint(4,8,9,12)
    #drawLineMidPoint(20,10,30,18)
    drawLineMidPoint(20,18,30,10)

    plt.plot(pointListX, pointListY)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Line draw using Midpoint Line Algorithm')
    plt.show()


if __name__ == "__main__":
    main()




    