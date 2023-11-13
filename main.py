from tkinter import *
import randGuessFunc
import configs



def enterPress(event):
    randGuessFunc.guess(entry,labelAnswer)
if __name__ == '__main__':

    window = Tk()
    window.geometry(configs.windowSize)
    window.title("угадай число")
    window.config(background=configs.bg)

    labelAsk = Label(window, #лейбл вверху
                     text="угадай число от 1 до 10",
                     font=(configs.font40),
                     bg=configs.bg,
                     bd=10)
    labelAsk.pack()

   
    # input
    entry = Entry(window,
                  font=(configs.font),
                  bd=10,
                  foreground="#40167a")

    entry.insert(0,"0")
    entry.pack(padx=20,pady=20)

    submit_button = Button(window,
                           text="Ввести",
                           font=(configs.font),
                           command= lambda: randGuessFunc.guess(entry,labelAnswer),
                           bd=10)
    submit_button.pack()

    #леймб для ответа угадал или нет
    labelAnswer = Label(window,
                        text="",
                        font=(configs.font),
                        bg=configs.bg,
                        bd=10)
    labelAnswer.pack()

    #keybinds
    window.bind("<Return>", enterPress)


    window.mainloop()



