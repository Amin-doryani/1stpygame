class Power:
    def __init__(self, w,h,x,y,lived):
        
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        
        self.lived = lived
       
        

    
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
    #lived
    def getlived(self):
        return self.lived
    def setlived(self,lived):
        self.lived = lived