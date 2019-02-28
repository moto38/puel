#Note:The template file will be copied to a new file. When you change the code of the template file you can create new file with this base code. 
#Note:The template file will be copied to a new file. When you change the code of the template file you can create new file with this base code. 
import datetime
import hmac
from pConst import *

class heart():
    def __init__(self):
        self.init()
    
    def init(self):
        self.Name=None
        self.BD=0    #BirthDay
        self.ID=0
        self.Digest=0
        self.heartnerPoint=0
        self.heartnerName=None
        self.Char=0        #CharacterType
        self.Model=0        #Puel Model
        self.DayHist=[]    
        self.WeekHist=[]
        self.YearHist=[]
        self.stat=[0,0,0,0,0] #sleep,kaze,kigen,warau,game
        self.FriendList=[]    #ListOfFriends
    
    def createHeart(self,name,hname,y,m,d,model,passwd):
        self.setName(name)
        self.setHeartnerName(hname)        
        self.setModel(model)
        self.setBD(y,m,d)
        self.createID()
        self.createDigest(passwd)
        
    def setName(self,name):
        self.Name = name
    
    def setHeartnerName(self,name):
        self.heartnerName=name
        
    def setChar(self,char):
        self.Char=char
    
    def setModel(self,model):
        self.Model=model
        
    def setBD(self,bdy,bdm,bdd): 
        try:
            self.BD=datetime.date(bdy,bdm,bdd)
        except:
            dt=datetime.datetime.now()
            self.BD=datetime.date(dt.year,dt.month,dt.day)

        return self.BD
        
    def createDigest(self,passwd):
        k=bytes(self.Name , 'latin-1' )
        p=bytes(passwd , 'latin-1' )
        self.Digest=hmac.new(k,p).hexdigest()
    
    def createID(self):
        self.ID=hash(self.Name)

    def touch(self,part,how):
        self.DayHist.append([part,how])
        self.touchOP(part,how)
        
    def touchOP(self,part,how):
        '''touchOperation
        ねてた > むにゃむむむ
        三連続おなじ > うざい
        しり > やめて
        ほっぺ > キス
        うで > 握手
        おでこ > 眠くない
        '''
        pass

    def showstatus(self):
        print("Kigen:"+str(self.stat[statKigen]))