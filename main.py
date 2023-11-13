from tkinter import *
import randGuessFunc
import configs
if __name__ == '__main__':

    window = Tk()
    window.geometry(configs.windowSize)
    window.title("угадай число")
    window.config(background=configs.bg)

    labelAsk = Label(window, #лейбл вверху
                     text="угадай число от 1 до 10",
                     font=(configs.font40),
                     bg=configs.bg)
    labelAsk.pack()

    entry = Entry(window, # инпут
                  font=(configs.font))
    entry.insert(0,"0")
    entry.pack()

    submit_button = Button(window,
                           text="Ввести",
                           font=(configs.font),
                           command= lambda: randGuessFunc.guess(entry,labelAnswer))
    submit_button.pack()

    labelAnswer = Label(window,text="",font=(configs.font),bg=configs.bg,)
    labelAnswer.pack()

    window.mainloop()



