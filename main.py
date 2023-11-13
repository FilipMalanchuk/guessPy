import random
from tkinter import *


def randNum(num):
    number = random.randint(1,10)
    print(number)
    if num == number:
        answer(1)
    else:
        answer(0)
def guess():
    answer = entry.get()
    #добавить проверку на пустую
    randNum(int(answer))
def answer(ans):
    if ans == 1:
        labelAnswer.config(text = "угадал")
    else:
        labelAnswer.config(text = "не угадал")


if __name__ == '__main__':

    window = Tk()
    window.geometry("800x400")
    window.title("угадай число")
    window.config(background="#d1f2a2")

    labelAsk = Label(window, #лейбл вверху
                     text="угадай число от 1 до 10",
                     font=('arial',40,'bold'),
                     bg="#d1f2a2")
    labelAsk.pack()

    entry = Entry(window, # инпут
                  font=('arial',28,'bold'))
    entry.pack()

    submit_button = Button(window,text="Ввести",font=('arial',28,'bold'), command=guess)
    submit_button.pack()

    labelAnswer = Label(window,text="",font=('arial',28,'bold'),bg="#d1f2a2")
    labelAnswer.pack()

    window.mainloop()



