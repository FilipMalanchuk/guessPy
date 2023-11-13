import random
def randNum(num):
    number = random.randint(1,100)
    if num == number:
        print("угадал , я загадал "+ str(number))
    else:
        print("не угадал, я загадал "+ str(number));


if __name__ == '__main__':
    numb = int(input("угадай число от 1 до 100: "))
    randNum(numb)



