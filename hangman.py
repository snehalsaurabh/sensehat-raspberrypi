#import sense_hat
#from time sleep, time
# from random import radiant
# 
# sense = sense_hat.SenseHat()
# sense.clear()
# 
# col_color=(0,255,0)
# bg_color=(0,0,0)
# bird_color=(200,200,0)
# bird_y=2
# bird_lives=3
# columns= [ (7,3,3)]
# column_speed_base=1
# debug_mode= False
# 
# up_key=sense_hat.DIRECTION_UP
# pressed = sense_hat.ACTION.PRESSED
# 
#

from guess import *

setup()

def restart(x,y):
    if(x>-30 and x<30 ) and (y>-169 and y<-147):
        del guessedletter[:]
        resetvariables()
        hangman.clear()
        guessedturtle.goto(-45,90)
        guessedturtle.clear()
        drawgallow()
        hiddenword.clear()
        instructions.clear()
        instructions.write('please guess a key to guess a letter', False, 'center',('Arial','13'))
        screen.tracer(1)
        

screen.onkey(guessq,'q')
screen.onkey(guessw,'w')
screen.onkey(guesse,'e')
screen.onkey(guessr,'r')
screen.onkey(guesst,'t')
screen.onkey(guessy,'y')
screen.onkey(guessu,'u')
screen.onkey(guessi,'i')
screen.onkey(guesso,'o')
screen.onkey(guessp,'p')
screen.onkey(guessa,'a')
screen.onkey(guesss,'s')
screen.onkey(guessd,'d')
screen.onkey(guessf,'f')
screen.onkey(guessg,'g')
screen.onkey(guessh,'h')
screen.onkey(guessj,'j')
screen.onkey(guessk,'k')
screen.onkey(guessl,'l')
screen.onkey(guessm,'m')
screen.onkey(guessn,'n')
screen.onkey(guessb,'b')
screen.onkey(guessv,'v')
screen.onkey(guessz,'z')
screen.onkey(guessc,'c')
screen.onkey(guessx,'x')
screen.onclick(restart)
screen.listen()