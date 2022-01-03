import random

operator = random.randint(1, 4)

first_number = random.randint(1, 20)

second_number = random.randint(1, 50)

scores = 0

chance = 5


def check_int(val: str) -> int:
    while not val.isnumeric():
        val = "ERREUR: Entrer un nombre: "
    return int(val)


def addition(number1: int, number2: int):
    global scores
    response = number1 + number2
    response_input = input("Calculer : " + str(number1) + " + " + str(number2) + " : ")
    rep = check_int(response_input)

    if rep == response:
        print("Bravo, bonne réponse !")
        print("Vous avez gagnez 10 points :)")
        scores += 10
        return

    print("Désolé, mauvaise réponse !")
    print("Vous avez perdu 2 points :(")
    scores -= 2


def substraction(number1: int, number2: int):
    global scores
    response = number1 - number2
    response_input = input("Calculer : " + str(number1) + " - " + str(number2) + " : ")
    rep = check_int(response_input)

    if rep == response:
        print("Bravo, bonne réponse !")
        print("Vous avez gagnez 12 points :)")
        scores += 12
        return
    print("Désolé, mauvaise réponse !")
    print("Vous avez perdu 3 points :(")
    scores -= 3


def multiplication(number1: int, number2: int):
    global scores
    response = number1 * number2
    response_input = input("Combien font : " + str(number1) + " x " + str(number2) + " : ")
    rep = check_int(response_input)

    if rep == response:
        print("Bravo, bonne réponse !")
        print("Vous avez gagnez 20 points :)")
        scores += 20
        return
    print("Désolé, mauvaise réponse !")
    print("Vous avez perdu 10 points :(")
    scores -= 10


def division(number1: int, number2: int):
    global scores
    response = number1 / number2
    response_input = input("Combien font : " + str(number1) + " / " + str(number2) + " : ")
    rep = check_int(response_input)

    if rep == response:
        print("Bravo, bonne réponse !")
        print("Vous avez gagnez 30 points :)")
        scores += 30
        return
    print("Désolé, mauvaise réponse !")
    print("Vous avez perdu 25 points :(")
    scores -= 25


def question(number1: int, number2: int, op: int):
    response = 0

    

