from puel1 import *
from time import *
import threading

class pHB():
    
    def __init__(self):
        self.timer=10
        self.msgidx=[
        '0101',
        '0303',
        '0401',
        '0505',
        '0806',
        '1113',
        '1225',
        '1231']
        self.msg={}
        self.msg['1225']=[
        'ハッピークリスマス!',
        'ねぇねえ、プレゼント買った〜?']
        self.msg['0101']=[
        'お正月大好き〜',
        'ハッピーニューイヤー!',
        'ねぇねえ何して遊ぶ？']
        self.msg['1231']=[
        '今年も終わりだな〜',
        'おしょおがつー']
        self.msg['0303']=[
        'お雛様飾るの？']
        self.msg['0401']=[
        '春だね、あったかい']
        self.msg['0505']=[
        '鯉のぼり']
        self.msg['0806']=[
        'おぼーんぼんぼん']
        self.msg['1113']=[
        'プエルのたんじょうびー']
        self.msg['Hima']=[
        'いないのー？']
                
    def loop(self):
        for i in range(0,5):
            shuffle(self.msgidx)
            m=self.msg[self.msgidx[0]]
            shuffle(m)
            draw(m[0],None)
            sleep(5)

p=pHB()
p.loop()
            
        
