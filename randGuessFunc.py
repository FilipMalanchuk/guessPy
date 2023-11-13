import random
def randNum(num,label):
    number = random.randint(1,10)
    print(number)
    if num == number:
        answer(1,label)
    else:
        answer(0,label)
def guess(entry,label):
    answer = entry.get()
    #добавить проверку на пустую
    randNum(int(answer),label)

def answer(ans,label):
    if ans == 1:
        changeLabel("угадал",label)
    else:
        changeLabel("не угадал",label)

def changeLabel(ans,label):
    label.config(text=ans)