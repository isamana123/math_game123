import random

correct_g = 0
incorrect_g = 0

while True:
    user_input = input(' Type in (add) or (sub) to begin)  type "end" to end the game : ').lower()

    if user_input == 'add':
        number1: int = random.randrange(1, 100)
        number2: int = random.randrange(1, 100)
        add_answer = number1 + number2
        print(number1, ' + ', number2)
        add_question = input('What is the sum of these two numbers? ')
        if int(add_question) == add_answer:
            print('That is correct!')
            correct_g += 1
            pass

        else:
            print('Incorrect. whomp whomp:(')
            incorrect_g += 1
            pass

    elif user_input == 'sub':
        number3: int = random.randrange(1, 100)
        number4: int = random.randrange(1, 100)
        sub_answer = number3 - number4
        print(number3, ' - ', number4)
        sub_question = input('What is the sum of these two numbers? ')
        if int(sub_question) == sub_answer:
            print('That is correct!')
            pass

        else:
            print('Incorrect. whomp whomp:(')
            incorrect_g += 1
            pass


    elif user_input == 'end':
        print('You got ', correct_g, ' questions right!')
        print('You got ', incorrect_g, ' questions wrong.')
        print('Thank you for playing! By Isaac Manaena, play again soon!')
        break

    else:
        print('I do not understand.')
        pass



