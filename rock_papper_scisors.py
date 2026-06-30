from tkinter import*
import random
winner=""


def button_pressed(number):
    global winner
    global c_score
    global p_score
    global rps
    computer_choice=random.randint(1,3)
    if number==1:
      if computer_choice==1:
        winner="drew"
      if computer_choice==2:
        winner="lost"
      if computer_choice==3:
        winner="won"

    if number==2:
      if computer_choice==1:
        winner="won"
      if computer_choice==2:
        winner="drew"
      if computer_choice==3:
        winner="lost"

    if number==3:
      if computer_choice==1:
        winner="lost"
      if computer_choice==2:
        winner="win"
      if computer_choice==3:
        winner="lost"


    if winner=="won":
      p_score=p_score+1
    if winner=="lost":
      c_score=c_score+1
    computer_score.config(text="Computer Score= "+str(c_score))
    player_score.config(text="Player Score= "+str(+p_score))
    conclusion.config(text="You "+winner)

    if computer_choice==1:
      rps.config(text=("The computer picked rock"))
    if computer_choice==2:
      rps.config(text="The computer picked papper")
    if computer_choice==3:
      rps.config(text="The computer picked scisors")
    





p_score=0
c_score=0
window=Tk()
window.title("rock papper scisors")
window.config(background="white")
window.geometry("400x400")
rock=Button(window,text="rock",background="yellow",font=("Airal",20),bd=5,command=lambda:button_pressed(1))
rock.place(x=25,y=180)
papper=Button(window,text="papper",background="red",font=("Airal",20),bd=5,command=lambda:button_pressed(2))
papper.place(x=125,y=180)
scisiors=Button(window,text="scissors",background="blue",font=("Airal",20),bd=5,command=lambda:button_pressed(3))
scisiors.place(x=250,y=180)
title=Label(window,text="Rock Papper scisors",font=("Ariel",20))
title.place(x=75,y=10)
options=Label(window,text="Options:",font=("Ariel",15))
options.place(x=1,y=130)
score_display=Label(window,text="Score:",font=("Ariel",15))
score_display.place(x=1,y=260)
player_score=Label(window,text="Player Score= "+str(+p_score),font=("Ariel",15))
player_score.place(x=40,y=310)
computer_score=Label(window,text="Computer Score= "+str(c_score),font=("Ariel",15))
computer_score.place(x=40,y=340)
conclusion=Label(window,text="You "+winner,font=("Ariel",15))
conclusion.place(x=300,y=370)
rps=Label(window,text="")
rps.place(x=200,y=100)
window.mainloop()