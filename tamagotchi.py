class Pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 5
        self.hunger = 0 
    # happiness/10 (wheere 10 is the highest), hunger/5 (where 5 is hungriest)

    def feed(self):
        if (self.hunger == 0):
            print(self.name + ' is full')
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

print('Enter your name:')
x = input()
pet = Pet(x)


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
    if (choice == "2"):
        pet.play()
    if (choice == "3"):
        pet.stats()
    if (choice == "4"):
        game_running = False
    
        


print('Game over')

#print 1 for feed, 2 for play
# keypress = input
# if keypress is 1 --> y.feed()
# if keypress is 2 --> y.play()


# user interface
# be able to set up a instance of the class 
# a function that creates a new pet
# a func that reads the properties of the pet 
# if statement for if hunger = 5 then can no longer play
# some UI that allows the user to input what they want to do 
# type/error checks 
# once user creates a pet then it tells them what the happiness/uunger numbers mean 

