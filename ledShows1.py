#GPIO multi LED shows PWM way softly
import RPi.GPIO as GPIO
from time import sleep

class Taki: #a abstract light object that move by vec per doTurn, bounce at posMin, posMax
    def __init__(self, ratio, vec, pos, posMin, posMax):
        self.ratio = ratio
        self.vec = vec
        self.pos = pos
        self.posMin = posMin
        self.posMax = posMax
        
    def doTurn(self):
        self.pos += self.vec
        if self.pos >= self.posMax and self.vec > 0 :
            self.vec *= -1
        if self.pos <= self.posMin and self.vec < 0:
            self.vec *= -1

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#gpio pin# for led order list
ledOrd = [14, 15, 18, 23, 24, 25, 1, 12]

#init Light led
pwmObjs = []
for pin in ledOrd:
    GPIO.setup(pin, GPIO.OUT)
    #Param Ch, Frequency
    PwmObj = GPIO.PWM(pin, 1000)
    PwmObj.ChangeDutyCycle(0) # %on of 1 clock
    #make pwmObj list
    pwmObjs.append(PwmObj)
    
#init Taki objects
takis = [Taki(2, 1, -3, 0, 7),
         Taki(20, 1, -3, 0, 7),
         Taki(65, 1, -2, 0, 7),
         Taki(85, 1, -1, 0, 7),
         Taki(100, 1, -0, 0, 7),
         #Taki(2, -1, 11, 0, 7),
         #Taki(20, -1, 10, 0, 7),
         #Taki(65, -1, 9, 0, 7),
         #Taki(85, -1, 8, 0, 7),
         #Taki(100, -1, 7, 0, 7)
         ]
    
#print(pwmObjs)

# x frame per sec for sleep *a
frr = 0.1

# 1 frame transition step *b
frtr = 5

# transition step rate = *a / *b = ex) 0.01sec
trs = frr / frtr

#Animation Frame base
frame = [[],[]]

#clear Frame Base
for i in range(0,len(ledOrd)):
    frame[0].append(0)
    frame[1].append(0)
#print(frame)

#main loop
try:
    #for bl in range(20):
    while True:

        ##Render takis to frame[1], takis set to next turn
        #clear current Base
        for i in range(0,len(ledOrd)):
            frame[1][i] = 0
        #render
        for taki in takis:
            if 0 <= taki.pos < len(ledOrd) and taki.ratio >= frame[1][taki.pos] :
                frame[1][taki.pos] = taki.ratio
            taki.doTurn()
        #print(frame)

        #show currnet by led all
        for frst in range(0, frtr+1):
            for frame01 in range(0, len(ledOrd)):
                diffa = frame[1][frame01] - frame[0][frame01] #frame between value
                difdiv = diffa / frtr #frame between value by step
                brightness = frame[0][frame01] + difdiv * frst #step brightness 
                pwmObjs[frame01].start(int(brightness))
                #print( "%3d " % (int(brightness)), end = " " ) #debug
            #print("") #debug
            sleep(trs)

        #flip to save current to past
        frame[0],frame[1] = frame[1],frame[0]

except Excepion:
    print(Exception)
    pass
for pwmObj in pwmObjs:
    pwmObj.stop()
GPIO.cleanup()

exit()
