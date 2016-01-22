############################################################################################

#TITLE:  THE BIG CATCH

#PURPOSE:  EAT AS MANY FISH AS YOU CAN WHILE CONTROLLING THE SHARK BUT DON'T EAT THE PURPLE ONES

#DATE LAST MODIFIED: 08/06/2014

#PROGRAMMER:  SAMATAR ABUKAR

############################################################################################


from tkinter import *
from time import *
from math import *
from random import *

#CREATES CANVAS
root = Tk()
screen = Canvas( root, width = 1100, height = 800)
screen.pack()
Sea = PhotoImage(file = "SEA.gif")
gamescreen = PhotoImage(file = "game screen.gif")
#CREATE SEA BACKGROUND
screen.create_image(600,400, image = Sea)
#SHOW GAME INFO SCREEN AT BEGINNING
screen.create_image(550,355, image = gamescreen)


def SetInitialValues():
    
    #SET GLOBAL VARIABLE SO I CAN USE THEM ANY TIME DURING THE PROGRAM WITHOUT HAVING TO REDEFINE THEM
    global SharkImageFile, SeaImageFile, GreenFish, YellowFish, RedFish, PurpleFish, FishArray, xShark, yShark, xMouse, yMouse, SharkSpeed, gamescreen
    global FishSpeed, Quit, GameOn, LivesLeft, score, Ylanes, FishLanes, xpos, LivesDisplay, xpoison, poisonlanes, poisonspeed, ypoison
    
    #IMPORT THE IMAGE FILES
    SeaImageFile = PhotoImage(file = "SEA.gif")
    SharkImageFile = PhotoImage(file = "shark copy.gif")
    GreenFish = PhotoImage(file = "greenfish copy.gif")
    YellowFish = PhotoImage(file = "yellowfish copy.gif")
    RedFish = PhotoImage(file = "redfish copy.gif")
    PurpleFish = PhotoImage(file = "purplefish.gif")
    gamescreen = PhotoImage(file = "game screen.gif")
    FishArray = [GreenFish, YellowFish, RedFish]

    #STARTING POSITION FOR SHARK
    xShark = 180
    yShark = 400

    #STARTING POSITION FOR MOUSE
    xMouse = 600
    yMouse = 400

    #GIVE ALL SET VALUES
    numFish = 8
    SharkSpeed = 10
    FishSpeed = 10
    poisonspeed = 6
    LivesLeft = 20
    score = 0
    scoreDisplay = 0
    LivesDisplay = 0


    #ARRAY FOR THE POSITION OF THE REGULAR FISH AND POISON FISH
    xpos = []
    xpoison=[]

    #ARRAY FOR LANES OF REGULAR FISH AND POISON FISH
    Ylanes=[200,400,600]
    ypoison = [300,500]
    poisonlanes = ["",""]
    FishLanes = ["","",""]

    
    Quit = False
    GameOn = True

    
#GIVES LOCATION OF MOUSE
def getMouseLocation( event ):
    global yMouse

    yMouse = event.y

#FINDS OUT WHICH KEY HAS BEEN PRESSED AND QUITS IF IT IS THE "Q" KEY
def getKeyPressed( event ):
    global Quit, GameOn

    if event.keysym == "q" or event.keysym == "Q":
        Quit = True
        GameOn = False

    else:
        print ("You pushed the " + event.key + "key, but nothing happens")
    


#DRAWS THE SHARK
def DrawShark():
    global SharkImageFile, SharkImage 

    SharkImage = screen.create_image( xShark, yShark, image=SharkImageFile )


#UPDATES THE SHARK POSITION DEPENDING ON WHERE THE MOUSE HAS BEEN PLACED
def UpdateSharkPosition():
    global yDirection, yMouse, SharkSpeed, yShark
    

    yShark += (yMouse - yShark)/ SharkSpeed


#DRAWS THE FISH
def DrawFish():
    global FishLanes, Ylanes, xpos, randfish

    import random

    for i in range(0,3):
        xpos.append(randint(1200,1600))

    for i in range(0,3):
        FishLanes[i] = screen.create_image(xpos[i],Ylanes[i],image= FishArray[i% len(FishArray)])


#UPDATES THE FISH POSITION BY SUBTRACTING THE SPEED SO THE FISH MOVE TO THE LEFT
def UpdateFishPosition():
    global FishSpeed, xpos
    
    for i in range(0,3):
        xpos[i] -= FishSpeed


#DRAWS POISON FISH
def DrawPoisonFish():
    global ypoision, poisonlanes, xpoison

    for i in range(0,2):
        xpoison.append(randint(1700,2200))#APPENDS THEM OFF THE CANVAS AT A RANDOM POINT IN THIS INTERVAL TO MAKE GAME HARDER


    for i in range(0,2):
        poisonlanes[i] = screen.create_image(xpoison[i],ypoison[i], image = PurpleFish)


#UPDATES THE POISON FISH POSITION 
def UpdatePoisonFish():
    global poisonspeed, xpoison

    import random

    for i in range(0,2):
        xpoison[i]-= poisonspeed


#DELETES POISON FISH AFTER DRAWING THE NEW ONE SO IT LOOKS LIKE THEY MOVE        
def DeletePoisonFish():
    
    for i in range(0,2):
        screen.delete(poisonlanes[i])
    
        
#WHEN POISON FISH COMES INTO CONTACT WITH SHARK'S MOUTH IT WILL DISAPPEAR AND BE TAKEN OFF SCREEN
def PoisonEatenByShark():
    global yShark,xShark,LivesLeft,xpoison

    import random

    for i in range (0,2):
        if xpoison[i] <=xShark+140 and xpoison[i]>=xShark and yShark>ypoison[i] -80 and yShark<ypoison[i]:
            xpoison[i] = randint(1700,2200)
            LivesLeft -= 1#IF YOU EAT A POISON FISH LIVES DECREASES BY ONE  

        elif xpoison[i] <= -100:
            xpoison[i] = randint(1700,2200)#IF YOU LEAVE THE FISH AND IT GOES OFF THE CANVAS NOTHING CHANGES



#WHEN REGULAR FISH COME INTO CONTACT WITH SHARK'S MOUTH THEY WILL DISAPPEAR AND BE TAKEN OFF THE SCREEN
def FishEatenByShark():
    global yShark,xShark,score,LivesLeft,xpos

    import random

    for i in range (0,3):
        if xpos[i] <=xShark+140 and xpos[i]>=xShark and yShark>Ylanes[i] -110 and yShark<Ylanes[i]-30:
            xpos[i] = randint(1200,1600)
            score = score+(i+1)#IF FISH IS EATEN SCORE INCREASES DEPENDING ON WHICH LANE YOU HAVE EATEN FROM

        elif xpos[i] <= -100:
            xpos[i] = randint(1200,1600)
            LivesLeft -= 1#IF YOU MISS A FISH LIVES DECREASES BY ONE


#AFTER PLAYER REACHES SCORE OF 100 THE FISH SPEED UP MAKING THE GAME HARDER
def FishSpeedUp():
    global FishSpeed

    if score >= 70:
        FishSpeed = 12

    elif score >=120:
        FishSpeed = 15

#DELETES THE SHARK AFTER THE NEW ONE HAS BEEN DRAWN MAKING IT LOOK LIKE IT'S MOVING
def DeleteShark():
    global  Sharkimage
    

    screen.delete(SharkImage)

#DELETE OLD FISH AFTER NEW ONES ARE DRAWN
def DeleteFish():
    
    for i in range(0,3):
        screen.delete(FishLanes[i])

#PRINTS THE SCORE IN THE TOP OF THE GAME CANVAS 
def ShowScore():
    global scoreDisplay
    Message = "Your score is: " + str(score)
    
    scoreDisplay = screen.create_text( 600, 50, text = Message, font = "Times 30", fill="white")

#PRINTS LIVES IN THE TOP OF GAME CANVAS
def ShowLives():
    global LivesDisplay
    Message = "Lives Remaining: " + str(LivesLeft)
    
    LivesDisplay = screen.create_text( 200, 50, text = Message, font = "Times 30", fill="white" )

#WHEN LIVESLEFT IS EQUAL TO 0 THE GAME ENDS AND IT GOES TO THE ENDGAME FUNCTION
def NoLives():
    global GameOn, GameOverMessage
    
    if LivesLeft == 0:
        GameOn = False

        EndGame()

#SHOWS A BLUE SCREEN AND DEPENDING ON IF THE PLAYER QUIT OR LOST PRINTS AN APPOPRIATE STATEMENT SHOWING LIVES AS WELL
def EndGame():
    global score

    
    if Quit == True:
        GameOverMessage = ("You quit: GAME OVER")
        
    elif LivesLeft == 0:
        GameOverMessage = ("Nice Try! GAME OVER")

    screen.create_rectangle(0,0,1100,800, fill = "dodgerblue")
    scoreDisplay = screen.create_text( 550, 450, text = "Your score was " , font = "Times 40",  fill="navy")
    screen.create_text(550, 350, text = GameOverMessage, font = "Times 60",  fill = "navy")
    screen.create_text(550,550, text = str(score), font = "Times 80", fill = "navy")

#DELETES OLD SCORE EVERYTIME THE SCORE INCREASES TO NOT OVERLAP NUMBERS
def DeleteScore():
    global scoreDisplay

    screen.delete(scoreDisplay)

#DELETES OLD LIVES EVERYTIME THE LIVES DECREASES TO NOT OVERLAP NUMBERS
def DeleteLives():
    global LivesDisplay

    screen.delete(LivesDisplay)

#MAIN LOOP FOR RUNNING GAME
def runGame():
    SetInitialValues()

    sleep(4)

    while GameOn == True:
        
         DrawShark()
         DrawFish()
         DrawPoisonFish()
         
         UpdateSharkPosition()
         UpdateFishPosition()
         UpdatePoisonFish()
         ShowScore()

         FishSpeedUp()
         PoisonEatenByShark()
         FishEatenByShark()
         ShowLives()

         screen.update()
         sleep(0.01)

         DeleteShark()
         DeleteFish()
         DeletePoisonFish()
         DeleteScore()
         DeleteLives()
         NoLives()

    EndGame()


root.after( 1000, runGame )


#BINDS THE PROCEDURE getMouseLocation TO ALL MOUSE-MOTION EVENTS
#THAT IS, WHENEVER THE USER MOVES THE MOUSE, getMouseLocation() GETS CALLED
screen.bind("<Motion>", getMouseLocation )


#BINDS THE USER'S KEY-STROKES TO THE PROCEDURE getKeyPressed(), DEFINED ABOVE.
screen.bind("<Key>", getKeyPressed)


#CREATES THE SCREEN AND SETS THE EVENT LISTENER
screen.pack()
screen.focus_set()


#STARTS THE PROGRAM
root.mainloop()
