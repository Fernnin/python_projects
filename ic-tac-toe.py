from tkinter import *
import random

def game():
    def next_turn(row, column):
        global player

        if buttons[row][column]['text'] == "" and check_winner() is False:

            if player == players[0]:

                buttons[row][column]['text'] = "X"
                buttons[row][column].config(bg="#FFFFCC")

                if check_winner() is False:
                    player = players[1]
                    label.config(text=(players[1]+"'s turn"))

                elif check_winner() is True:
                    buttons[row][column].config(bg="yellow")
                    show_winner(players[0], players[1])

                elif check_winner() == "Tie":
                    TIE()

            else:

                buttons[row][column]['text'] = "O"
                buttons[row][column].config(bg="#FFCCCC")

                if check_winner() is False:
                    player = players[0]
                    label.config(text=(players[0]+"'s turn"))

                elif check_winner() is True:
                    buttons[row][column].config(bg="yellow")
                    show_winner(players[1],players[0])

                elif check_winner() == "Tie":
                    TIE()

    def check_winner():

        for row in range(3):
            if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
                return True

        for column in range(3):
            if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
                return True

        if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
            return True

        elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
            return True

        elif empty_spaces() is False:

            for row in range(3):
                for column in range(3):
                    buttons[row][column].config(bg="yellow")
            return "Tie"

        else:
            return False


    def empty_spaces():

        spaces = 9

        for row in range(3):
            for column in range(3):
                if buttons[row][column]['text'] != "":
                    spaces -= 1

        if spaces == 0:
            return False
        else:
            return True

    def new_game():

        global player

        player = random.choice(players)

        label.config(text=player+"'s turn")

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(text="",bg="#F0F0F0")
    
    def show_winner(a,b):
        global result                
        result = Tk()
        result.config(bg="light green")
        label = Label(result,text="🥳🥳🥳🥳"+a+" WON that match🥳🥳🥳🥳 \n\n"+"🤣🤣🤣🤣"+b+" is the LOOSER🤣🤣🤣🤣", font=('consolas', 40), backgroun="light green")
        label.pack(side="top")
        result.after(3000,lambda:result.destroy())
        result.mainloop()
    def TIE():
        global result                
        result = Tk()
        result.config(bg="light green")
        label = Label(result,text="It's a Tie\n🙄🙄🙄🙄🙄🙄🙄🙄🙄🙄🙄🙄", font=('consolas', 40), backgroun="light green")
        label.pack(side="top")
        result.after(3000,lambda:result.destroy())
        result.mainloop()


    window = Tk()
    window.title("Tic-Tac-Toe")
    players =[str(a1.get()), str(b1.get())]
    global player
    player = random.choice(players)
    buttons = [[0,0,0],
            [0,0,0],
            [0,0,0]]

    label = Label(window,text=player + "'s turn", font=('consolas',40))
    label.pack(side="top")

    reset_button = Button(window,text="restart", font=('consolas',20), command=new_game)
    reset_button.pack(side="bottom")

    frame = Frame(window)
    frame.pack()

    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                        command= lambda row=row, column=column: next_turn(row,column))
            buttons[row][column].grid(row=row,column=column)

    window.mainloop()

Login = Tk()
Login.title("tic-tac-toe")
Login.geometry("500x400")
Login.config(bg="sky blue")
heading=Label(text="---TIC TAC TOE---", font=('consolas',40))
heading.pack(side="top")
a=Label(text="Player 1:", font=("consolas", 20), background="sky blue")
a.place (relx=0.15, rely=0.5, anchor=CENTER)
a1= Entry(Login, width=20, font=20)
a1.place (relx=0.524, rely=0.5, anchor=CENTER)
b1=Entry(Login, width=20, font=20)
b1.place (relx=0.52, rely=0.6, anchor=CENTER)
b=Label(text="Player 2:", font=("consolas", 20), background="sky blue")
b.place (relx=0.15, rely=0.6, anchor=CENTER)
click = Button(text="START THE GAME", font=('consolas',15), command=game)
click.pack(side="bottom")
Login.after(20000,lambda:Login.destroy())
Login.mainloop()