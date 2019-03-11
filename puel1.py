from pHeart import *
from pdisplay import *
from random import *
from datetime import *

class puel(heart):
    def __init__(self):
        self.init()
        #self.d=display()
        
    def touchOP(self,part,how):
        '''
        ねてた > むにゃむむむ
        三連続おなじ > うざい
        しり > やめて
        ほっぺ > キス
        うで > 握手
        おでこ > 眠くない
        '''
        if self.stat[statSleep] > 0 :
            self.sleepy()
        elif self.checkuzai(part):
            self.uzai()
        elif part == partHip:
            self.hip()
        elif part == partHoppe:
            self.Hoppe()
        elif part == partHead:
            self.Head()
        elif part == partLHand:
            self.LHand(how)
        elif part == partRHand:
            self.RHand(how)
        else:
            self.takaitakai()
    
    def RHand(self,how):
        if how != touchLong:
            self.stat[statKigen]+=1
            msg=['さみしいの？']
            shuffle(msg)
            draw(msg[0],None)
            
    def LHand(self,how):
        if how != touchLong:
            self.stat[statKigen]+=1            
            msg=['あくしゅ、うれしいー']
            shuffle(msg)
            draw(msg[0],None)

    def checkuzai(self,part):
        l=len(self.DayHist)
        if l<3:
            return False
        elif self.DayHist[l-1][0]==part and self.DayHist[l-2][0]==part:
            return True
        else:
            return False
    
    def Hoppe(self):
        self.stat[statKigen]+=1
        msg=['キスー？','えへへ','照れちゃうよ','愛情たっぷり〜']
        shuffle(msg)
        draw(msg[0],None)
   
    def takaitakai(self):
        self.stat[statKigen]+=1
        draw('わーいわーい、タカイタカーイ',None)
       
    def sleepy(self):
        self.stat[statSleep]-=1
        if self.stat[statSleep]> 0:
            draw('むにゃむむむ',None)
        else:
            draw('わかったよ、起きるよ',None)
    
    def oyasumi(self):
        msg=['ブヒブヒパジャマブヒブヒブッブー,おやすみー','むにゃむむむむ']
        shuffle(msg)
        self.stat[statSleep]=30
        draw(msg[0],None)
        
    def Head(self):
        msg=['まだ眠くないよー']
        shuffle(msg)
        if randint(0,10000)==5:
            self.oyasumi()
        else:
            draw(msg[0],None)
        
    def uzai(self):
        msg=['そんなにさわらないでよ',
        'そっとしておいてよ']
        self.stat[statKigen]-=1
        shuffle(msg)
        draw(msg[0],None)
        
    def hip(self):
        msg=['なんでー','やあだー']
        shuffle(msg)
        self.stat[statKigen]-=1
        draw(msg[0],None)
    
        
        
l
