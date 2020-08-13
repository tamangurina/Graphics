import math
import matplotlib.pyplot as plt

pointListX = []
pointListY = []

def drawLineBresenham(x1,y1,x2,y2):
    x,y = x1, y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    print('x = %s, y = %s' % (x, y))
    plt.plot(x, y, 'bo')
    pointListX.append(x)
    pointListY.append(y) 

    if dx > dy:
        p = 2*dy - dx
        for k in range(0, dx):            
            if p > 0:
                y = y + 1 if y < y2 else y - 1
                p = p + 2*dy - 2*dx
            else:     
                p = p + 2*dy 
            x = x + 1 if x < x2 else x - 1 
            print(f'x = {x}, y = {y}') 
            plt.plot(x, y, 'bo')          
            pointListX.append(x)
            pointListY.append(y)                    
    else:
        p = 2*dx - dy
        for k in range(0, dy):            
            if p > 0:
                x = x + 1 if x < x2 else x - 1
                p = p + 2*dx - 2*dy
            else:  
                p = p + 2*dx
            y = y + 1 if y < y2 else y - 1
            print(f'x = {x}, y = {y}')  
            plt.plot(x, y, 'bo')         
            pointListX.append(x)
            pointListY.append(y) 

def main():
    #drawLineBresenham(20,10,30,18)
    #drawLineBresenham(10,5,16,15)
    drawLineBresenham(20,18,30,10)

    plt.plot(pointListX, pointListY)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Line draw using BLA')
    plt.show()


if __name__ == "__main__":
    main()




    