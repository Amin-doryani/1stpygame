class Player:
    def __init__(self, w,h,x,y,speed,t):
        
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.speed = speed
        self.t = t

    
    #W
    def getw(self):
        return self.w
    def setw(self,w):
        self.w = w
    #H
    def geth(self):
        return self.h
    def seth(self,h):
        self.h = h
    #X
    def getx(self):
        return self.x
    def setx(self,x):
        self.x = x
    
    #Y
    def gety(self):
        return self.y
    def sety(self,y):
        self.y = y
    #speed
    def getspeed(self):
        return self.speed
    def setspeed(self,speed):
        self.speed =speed
    #T
    def gett(self):
        return self.t
    def sett(self,t):
        self.t = t
