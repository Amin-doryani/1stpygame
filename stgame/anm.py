class Anm:
    def __init__(self, w,h,x,y,speed,heart,spd):
        
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.speed = speed
        self.heart = heart
        self.spd = spd
        

    
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
    #heart
    def getheart(self):
        return self.heart
    def setheart(self,heart):
        self.heart =heart
    #spd
    def getspd(self):
        return self.spd
    def setspd(self,spd):
        self.spd =spd
    
    def chnagepos(self):
        i = self.getx()
        speed = self.getspeed()
        if speed > 0:
            if (i>=1):
                self.setx((i+self.spd))
            if i>=1100:
                self.setspeed(speed * (-1))
        if speed < 0:
            if (i<=1200):
                self.setx((i-self.spd))
            if i <= 10:
                self.setspeed(speed * (-1))
            
