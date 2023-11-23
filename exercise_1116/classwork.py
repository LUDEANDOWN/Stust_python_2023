import math


class MyShape: 
    def __init__(self,square_side,length,width,radius):
        self.square_side=square_side
        self.length=length
        self.width=width
        self.radius=radius

    def getSquareArea(self):
        print("正方形面積=" + str(self.square_side*self.square_side)) #打印正方形面積函式

    def getRectangleArea(self):
        print("長方形面積="+str(self.length*self.width))#打印長方形面積函式

    def getTriangleArea(self):
        print("三角形面積="+ str((self.length*self.width)/2))#打印三角形面積函式

    def getCircleArea(self):
        print("圓形面積="+str(self.radius*self.radius*math.pi))#打印圓形面積函式


SP=MyShape(2,4,6,8)

SP.getSquareArea()
SP.getRectangleArea()
SP.getTriangleArea()
SP.getCircleArea()  