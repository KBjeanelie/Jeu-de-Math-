import random

operator = random.randint(1, 4)

first_number = random.randint(1, 20)

second_number = random.randint(1, 10)

scores = 0

chance = 5


def check_int(val: str) -> float:
    while not val.isnumeric():
        val = "ERREUR: Entrer un nombre: "
    return float(val)


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

    i = 0
    while i < chance:
        if op == 1:
            addition(number1, number2)
        elif op == 2:
            substraction(number1, number2)
        elif op == 3:
            multiplication(number1, number2)
        else:
            division(number1, number2)

        op = random.randint(1, 4)
        number1 = random.randint(1, 20)
        number2 = random.randint(1, 10)
        i += 1
    
    print("--------------------------------------------------------------------------------")
    print("Votre Score est de : ", scores)
    print("--------------------------------------------------------------------------------")


def main():
    question(first_number, second_number, operator)


#######################################################################################################
#                                    STARTING PROGRAMME                                               #
#######################################################################################################

main()
