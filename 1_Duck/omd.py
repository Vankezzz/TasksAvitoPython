from Animals import *
from Items import *

resultsOfsteps = []


def step1(animal):
    print(
        f'{animal.name} wants to go out for buying the nunchucks \n'
        f'Should take for walking:\n'
        f'1. Umbrella\n'
        f'2. Doggy\n'
        f'3. Ventuz\n'
    )
    option = ''
    options = {
        '1': Umbrella,
        '2': Doggy,
        '3': Ventuz
    }
    while option not in options:
        option = input('Выберите: {}/{}/{}\nYour answer is '.format(*options))
    animal.items = options[option]
    print(f'good, I hope {options[option].__name__} will be needed to me')
    return None


def step2(animal):
    print(
        f'It rains outside, but you are Duck. Mama always said life was like a box of chocolates. You never '
        f'know what you are gonna get \n'
        f'A few moments later you see a deep tunnel, you will go into it?\n'
        f'1. Of course\n'
        f'2. Brrrrr...I think to pass by'
    )
    option = ''
    options = {
        '1': True,
        '2': False,
    }
    while option not in options:
        option = input('Выберите: {}/{}\nYour answer is '.format(*options))
    print('Every man dies, but not every man really lives.')
    return options[option]


def step3(animal, resultofsteps):
    option = ''
    varphrase = ''
    options = {
        '1': True,
        '2': False,
    }
    if resultofsteps[1]:
        print(
            f'{animal.name} has been wandering for a long time. He stopped and lit a cigar, after that he said '
            f'"After all, tomorrow is another day!" \n'
            f'Suddenly three eggs have appeared in front of him. It were the famous Egbert, Yoko, and Shelly\n'
            f'Are you going to fight?\n'
            f'1. The first rule of Fight Club is: You do not talk about Fight Club. The second rule is fight to the'
            f'end\n'
            f'2. Do, or do not. There is no “try”'
        )
        if animal.items[0] == Doggy:
            options['3'] = None
            varphrase = 'I will back, leather bastards\n'
            print('3. You may use doggy to leave fastly\n')
    else:
        print(
            f'{animal.name} has been going for a long time under the rain. '
            f'Suddenly he saw a bottomless river. Whats fucked up?! What are you going to do?\n '
            f'1. You are going to swim across\n'
            f'2. I think to return'
        )
        if animal.items[0] == Umbrella:
            options['3'] = None
            varphrase = 'I believe I can fly'
            print('3. You may use Umbrella for flying over the river\n')

    while option not in options:
        option = input('Your answer is ')
    if options[option] is None:
        print(varphrase)
    else:
        print('Once the wise cucumber told me "Follow your heart"')
    return options[option]


if __name__ == '__main__':
    duck = Duck('Sam', 34)
    duck.display_info()
    print("*****************************Step1*******************************")
    resultsOfsteps.append(step1(duck))
    print("*****************************Step2*******************************")
    resultsOfsteps.append(step2(duck))
    print("*****************************Step3*******************************")
    resultsOfsteps.append(step3(duck, resultsOfsteps))
    print("Story will be continued in soon, but now I gonna leave")


