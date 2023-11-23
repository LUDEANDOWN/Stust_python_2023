
#創建了鴨子類別,有它的名子,性別,年齡,還有座標XYZ(我只考慮水平移動(公尺))來算他的走路,游泳,飛行的速度,時間(秒)
class Duck():
    def __init__(self,name,gender,age,coordinateX,coordinateY,coordinateZ,time):
        self.name=name
        self.gender=gender
        self.age=age
        self.coordinateX=coordinateX
        self.coordinateY=coordinateY
        self.coordinateZ=coordinateZ
        self.time=time

    def talk(self): #創建talk 來讓鴨子自我介紹
        print("Hi I'm duck "+self.name )

    def vote(self): #來說明鴨子是否能飛和游泳了
        if self.age<1:
            print("I can't fly and swim yet")
        else:
            print("I can fly and swim")

    def fly(self):#飛行判斷
        if self.age<1:#如果他年紀小於1就不能飛
            print("I can't fly yet")
        elif self.coordinateZ>=1:#如果coordinateZ大於等於1就可以飛
            print("Duck "+self.name+" 的飛行速度為 "+str(abs(self.coordinateY-self.coordinateX)/self.time) + " m/s")
        else:#其他就不能飛,飛行高度不夠
            print("I can't fly now because "+str(self.coordinateZ)+" less than 1")

    def walk(self):#走路判斷
        if self.coordinateZ==0:#如果coordinateZ等於0就可以走路
            print("Duck "+self.name+" 的走路速度為 "+str(abs(self.coordinateY-self.coordinateX)/self.time) + " m/s")
        else:#其他就不能走,因為不是平地0
            print("I can't walk now because "+str(self.coordinateZ)+" not equal to 0 ")
    def swim(self):#游泳判斷
        if self.age<1:#如果他年紀小於1就不能游泳
            print("I can't swim yet")
        elif self.coordinateZ<0:#如果coordinateZ小於0就可以游泳
            print("Duck "+self.name+" 的游泳速度為 "+str(abs(self.coordinateY-self.coordinateX)/self.time) + " m/s")
        else:#其他就不能游泳,因為沒有水
            print("I can't swim now because "+str(self.coordinateZ)+" greater to 0")

duck=Duck("DD","Male",2,6,1,0,2)

duck.talk()
duck.vote()
duck.fly()
duck.walk()
duck.swim()
