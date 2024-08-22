class Anm:
    def __init__(self, w,h,x,y,speed):
        
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.speed = speed
        

    
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
    
    def chnagepos(self):
        i = self.getx()
        speed = self.getspeed()
        if speed > 0:
            if (i>=1):
                self.setx((i+0.1))
            if i>=1100:
                self.setspeed(speed * (-1))
        if speed < 0:
            if (i<=1200):
                self.setx((i-0.1))
            if i <= 10:
                self.setspeed(speed * (-1))
            