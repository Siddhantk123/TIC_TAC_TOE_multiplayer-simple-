from tkinter import *

def callback(r,c):
    global players
    #now we will assign value to each box by configuring
    if players=='X' and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text='X', fg='blue',bg='white')
        states[r][c]='X'
        players='O'
    if players=='O' and states[r][c] == 0 and stop_game == False:
        b[r][c].configure(text='O', fg='orange',bg='black')
        states[r][c]='O'
        players='X'
    check_for_winner()
def check_for_winner():
    global stop_game
    for i in range(3):
        #for rows
        if states[i][0]== states[i][1]==states[i][2]!=0:
            b[i][0].configure(bg='green')
            b[i][1].configure(bg='green')
            b[i][2].configure(bg='green')
            stop_game=True
        #for columns    
        if states[0][i]== states[1][i]==states[2][i]!=0:
            b[0][i].configure(bg='green')
            b[1][i].configure(bg='green')
            b[2][i].configure(bg='green')
            stop_game=True  
    #for diagonal 1
    if states[0][0]== states[1][1]==states[2][2]!=0:
        b[0][0].configure(bg='green')
        b[1][1].configure(bg='green')
        b[2][2].configure(bg='green')
        stop_game=True
    #for diagonal 2
    if states[0][2]== states[1][1]==states[2][0]!=0:
        b[0][2].configure(bg='green')
        b[1][1].configure(bg='green')
        b[2][0].configure(bg='green')
        stop_game=True          




root=Tk()
root.title("Tic Tac Toe *Siddhant")
#this matrix is taken to form 3*3 matrix
b=[[0,0,0],
    [0,0,0],
    [0,0,0]]
#this matrix is formed to check the position of above matrix and assign value to above matrix,and chek the condition

states=[[0,0,0],
       [0,0,0],
       [0,0,0]]

for i in range(3):
    for j in range(3):
        b[i][j]=Button(font=("Arial",60),width=4,bg='powder blue',
        command= lambda r=i,c=j: callback(r,c))
        b[i][j].grid(row=i,column=j)
players='X'
stop_game=False
mainloop()                
        
