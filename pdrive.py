from puel1 import *

p=puel()
p.createHeart('poko','echo',2017,12,19,1,'cha')
#p.setBD(None,None,None)
print(p.BD)
#p.setBD(2013,12,21)
#print(p.BD)
#p.setName(‘name’)
#p.createDigest(“pass”)
#print(p.Digest)
print(p.ID)
p.stat[statSleep]+=1
for i in range(0,10):
    p.touch(partHip,1)
p.touch(partBody,0)
p.touch(partHoppe,1)
p.touch(partHead,1)
p.touch(partLHand,1)
p.touch(partRHand,1)
p.oyasumi()
print(p.DayHist)
p.showstatus()
