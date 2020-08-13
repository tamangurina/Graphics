import math
import matplotlib.pyplot as plt

pointListX = []
pointListY = []

def drawLineDDA(x1,y1,x2,y2):
    x,y = x1, y1
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) > abs(dy):
        stepSize = dx
    else:
        stepSize = dy
    xinc = dx / abs(stepSize)
    yinc = dy / abs(stepSize)
    stepSize = abs(stepSize)
    print(dx, stepSize, dy)

    print('x = %s, y = %s' % (x, y))
    plt.plot(x, y, 'bo')
    pointListX.append(x)
    pointListY.append(y)

    for i in range(stepSize):
        x += xinc
        y += yinc

        print('x = %s, y = %s' % (round(x),round(y)))        
        plt.plot(round(x), round(y), 'bo')
        pointListX.append(round(x))
        pointListY.append(round(y))

def main():
    #drawLineDDA(10,5,16,15)
    #drawLineDDA(20, 20, 30, 28)
    #drawLineDDA(0, 0, 4, 6)
    #drawLineDDA(20,10,30,18)
    drawLineDDA(10,15,20,10)

    plt.plot(pointListX, pointListY)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('line draw using DDA')
    plt.show()


if __name__ == "__main__":
    main()	
