class Pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 5
        self.hunger = 0

    def feed(self):
        if (self.hunger == 0):
            print(self.name + ' is full')
        elif (len(log) > 2 and log[-2] == 1 and log[-1] == 1):
            print(self.name + ' cannot eat aymore')
            self.happiness -= 2
        else:
            self.hunger -= 1
            print("You've fed your pet. It's hunger level is " + str(self.hunger) + "/5")

    def play(self):
        if (self.hunger) == 5:
            print(self.name + ' is too hungry to play')
        elif (self.happiness == 10):
            print('Your pet is already super happy!')
        else:
            self.happiness +=1
            self.hunger += 1
            print("You've played with your pet. It's happiness level is " + str(self.happiness) + "/10")

    def stats(self):
        print(self.name + "'s happiness is " + str(self.happiness) + " and hunger is " + str(self.hunger))

print('Enter your Tamagotchi name:')
x = input()
pet = Pet(x)

log = []
def logger(number):
    log.append(number)

game_running = True
print('Hapiness 0-10 where 10 is super happy')
print('Hunger 0-5 where 5 is starving. Pet can\'t play if starving')
while (game_running == True):

    print('\n')
    print('Press 1 to feed you pet')
    print('Press 2 to play with your pet')
    print('Press 3 to view the stats of your pet')
    print('Press 4 to quit')
    print('What would you like to do?')
    choice = input()
    if (choice == "1"):
        pet.feed()
        logger(1)
    if (choice == "2"):
        pet.play()
        logger(2)
    if (choice == "3"):
        pet.stats()
        logger(3)
    if (choice == "4"):
        game_running = False
    if (choice != "1" and choice != "2" and choice != "3" and choice != "4"):
        print('Invalid input')

print('Game over')


