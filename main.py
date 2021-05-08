from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
from random import * 
import random as rand
from PIL import Image, ImageTk


def choicemade(choicePlayer):
    global comScore, playScore, scoreText, imageList, computerImage, playerImage,bestOfNum, keepPlaying
    choiceComputer= rand.randint(0,2)

    computerImage=imageList[choiceComputer]
    root.computerImage=ImageTk.PhotoImage(Image.open(computerImage))
    computer.configure(image=root.computerImage)

    playerImage=imageList[choicePlayer]
    root.playerImage=ImageTk.PhotoImage(Image.open(playerImage))
    player.configure(image=root.playerImage)
    

    if (choicePlayer == choiceComputer-1 or  (choiceComputer==0 and choicePlayer==2)):
        comScore+=1
    elif (choicePlayer-1 == choiceComputer or  (choiceComputer==2 and choicePlayer==0)):
        playScore+=1
    scoreText.set(str(comScore)+" - "+str(playScore))
    if comScore== bestOfNum :
        #print("computer won "+str(comScore)+" - "+str(playScore))
        box= messagebox.askquestion("Computer Won!","\t      "+str(comScore)+" - "+str(playScore)+"\nWould you like to keep playing?",icon="question")
        if box!="yes":         
            keepPlaying=FALSE  
        root.destroy()         
        
    elif playScore== bestOfNum:        
        #print("player Won "+str(comScore)+" - "+str(playScore))
        box= messagebox.askquestion("Player Won!","\t      "+str(comScore)+" - "+str(playScore)+"\nWould you like to keep playing?",icon="question")
        if box!="yes":      
            keepPlaying=FALSE
        root.destroy()
           
  
def startgame():

    startButton.destroy()
    bestOfButton.destroy()
    rpsButton.destroy()
    sprButton.destroy()
    
        

    global computerImage, playerImage, rockImage, paperImage, scissorsImage, scoreText
    
    #computer= Button(root,bd=0,height=120,width=110,bg="#c1c1c1",image=computerImage,compound= BOTTOM,text="The Computer \nPicked: ")
    computer.grid(row=1, column=0)
    computer["state"]=DISABLED
    computer["font"]= gameFont

    
    scoreText.set("Click a Button\nto \nStart Playing")
    scoreImage= PhotoImage(file= r'images/empty.png')
    score= Button(root, bd=0, height=120, width=110,disabledforeground ="#c1c1c1", bg="#426973",textvariable=scoreText,image=scoreImage, compound= BOTTOM )
    score.grid(row=1,column=1)
    score["state"]=DISABLED
    score["font"]= gameFont
    
    
    player.grid(row=1, column=2)
    player["state"]=DISABLED
    player["font"]= gameFont

    #rockImage= rockImage.subsample(8,8)
    rock = Button(root,bd=0,height=80,width=112, bg="#426973", activebackground ="#ECEAEF",image=root.rockImage,command=lambda : choicemade(0))
    rock.grid(padx=2,pady=3,row=2,column=0)

    
    paper = Button(root,bd=0,height=80,width=112, bg="#426973", activebackground ="#ECEAEF",image=root.paperImage,command=lambda : choicemade(1))
    paper.grid(padx=2,pady=3,row=2,column=1)

    
    scissors= Button(root,bd=0,height=80,width=112, bg="#426973", activebackground ="#ECEAEF",image=root.scissorsImage,command=lambda : choicemade(2))
    scissors.grid(padx=2,pady=3,row=2,column=2)
    

def bestOfWhat():
    global bestOfNum
    bestOfNum= bestOfNum+2 if bestOfNum < 7 else 1
    bestOfText.set("Best Of "+str(bestOfNum))

def OnClose():
    global keepPlaying
    keepPlaying=FALSE 
    root.destroy()

"""-------------------------------main-------------------------------"""
imageList=['images/rock.png','images/paper.png','images/scissors.png','images/empty.png']
keepPlaying= TRUE

while keepPlaying==TRUE : 
    root = tk.Tk()
    root.title("Rock Paper Scissors")
    root.iconbitmap(r'images/scissors.ico')
    root.configure(bg="#fff")
    bestOfNum=3
    playScore=0
    comScore=0
    
    root.protocol('WM_DELETE_WINDOW', OnClose)



    #declaring the image variables (tip: they cannot be declared in a function)
    try:
        computerImage=imageList[3]
        root.computerImage=ImageTk.PhotoImage(Image.open(computerImage))

        playerImage=imageList[3]
        root.playerImage=ImageTk.PhotoImage(Image.open(playerImage))

        rpsImage = "images/rps.png"
        root.rpsImage=ImageTk.PhotoImage(Image.open(rpsImage))
        sprImage = "images/spr.png"
        root.sprImage=ImageTk.PhotoImage(Image.open(sprImage))

        rockImage=imageList[0]
        paperImage=imageList[1]
        scissorsImage=imageList[2]
        root.rockImage=ImageTk.PhotoImage(Image.open(rockImage))
        root.paperImage=ImageTk.PhotoImage(Image.open(paperImage))
        root.scissorsImage=ImageTk.PhotoImage(Image.open(scissorsImage)) 
    except:
        print("rouh")

    scoreText= tk.StringVar()

    #declaring buttons 
    computer= Button(root,bd=0,height=120,width=110,disabledforeground ="#c1c1c1",bg="#426973",image=root.computerImage,compound= BOTTOM,text="The Computer \nPicked: ")
    player= Button(root,bd=0,height=120,width=110, disabledforeground ="#c1c1c1", bg="#426973",image=root.playerImage,compound= BOTTOM,text="The Player \nPicked: ")

    #declaring the fonts 
    textFont =font.Font(family="Times",size=20,weight="bold",slant="italic")
    gameFont =font.Font(family="Times",weight="bold",slant="italic")

    bestOfText= tk.StringVar()
    bestOfText.set("Best Of 3\n Click To Change")
    bestOfButton= Button(root,activebackground ="#6097A5", activeforeground ="#c1c1c1", textvariable= bestOfText,height=5,width=20,bd=0,fg="#c1c1c1",bg="#426973",command= bestOfWhat)
    bestOfButton.grid(row=1,column=0)
    bestOfButton["font"]=textFont

    startButton= Button(root,activebackground ="#6097A5", activeforeground ="#c1c1c1", text="Click To Start",height=5,width=20,bd=0,fg="#c1c1c1",bg="#426973",command= startgame)
    startButton.grid(row=2,column=1)
    startButton["font"]=textFont
    
    rpsButton= Button(root,image=root.sprImage,text=" ",height=150,width=120,bd=0,fg="#c1c1c1",bg="#fff",disabledforeground="#fff")
    rpsButton.grid(row=1,column=1)
    rpsButton["font"]=textFont
    rpsButton["state"]=DISABLED

    sprButton= Button(root,image=root.rpsImage,text=" ",height=150,width=120,bd=0,fg="#c1c1c1",bg="#fff",disabledforeground="#fff")
    sprButton.grid(row=2,column=0)
    sprButton["font"]=textFont
    sprButton["state"]=DISABLED

    root.mainloop()