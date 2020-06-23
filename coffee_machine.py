# Write your code here

class CoffeeMachine:
    print("********** Welcome to Starbucks Coffee *********")
    print("Your one stop shop for great cup of coffee :)")
    print("We offer 3 different types of coffee")
    print("Our menu List:")
    print("Type                 Cost")
    print("Espresso .............$4 ")
    print("Latte    .............$7 ")
    print("Cappuccino ...........$6 ")
    print("Enjoy your Coffee :)")
    
    def __init__(self, water=400, milk=540, coffee=120, cups=9, money=550):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

    def interact(self, state):
        self.state = state

        if self.state == 'remaining':
            print("The coffee machine has:")
            print(str(self.water) + " of water")
            print(str(self.milk) + " of milk")
            print(str(self.coffee) + " of coffee beans")
            print(str(self.cups) + " of disposable cups")
            print(str(self.money) + " of money")

        elif self.state == 'buy':
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino")
            choice = input()
            if choice == "1":
                if (self.water >= 250) and (self.coffee >= 16) and (self.cups >= 1):
                    print('I have enough resources, making you a coffee!')
                    self.water -= 250
                    self.coffee -= 16
                    self.money += 4
                    self.cups -= 1
                else:
                    if self.water < 250:
                        print('Sorry, not enough water!')
                    if self.coffee < 16:
                        print('Sorry, not enough coffee!')
                    if self.cups < 1:
                        print('Sorry, not enough cups!')

            elif choice == "2":
                if (self.water >= 350) and (self.milk >= 75) and (self.coffee >= 20) and (self.cups >= 1):
                    print('I have enough resources, making you a coffee!')
                    self.water -= 350
                    self.milk -= 75
                    self.coffee -= 20
                    self.money += 7
                    self.cups -= 1
                else:
                    if self.water < 350:
                        print('Sorry, not enough water!')
                    if self.milk < 75:
                        print('Sorry, not enough milk!')
                    if self.coffee < 20:
                        print('Sorry, not enough coffee!')
                    if self.cups < 1:
                        print('Sorry, not enough cups!')

            elif choice == "3":
                if (self.water >= 200) and (self.milk >= 100) and (self.coffee >= 12) and (self.cups >= 1):
                    print('I have enough resources, making you a coffee!')
                    self.water -= 200
                    self.milk -= 100
                    self.coffee -= 12
                    self.money += 6
                    self.cups -= 1
                else:
                    if self.water < 200:
                        print('Sorry, not enough water!')
                    if self.milk < 100:
                        print('Sorry, not enough milk!')
                    if self.coffee < 12:
                        print('Sorry, not enough coffee!')
                    if self.cups < 1:
                        print('Sorry, not enough cups!')

        elif self.state == 'fill':
            print("Write how many ml of water do you want to add:")
            added_water = int(input())
            self.water += added_water
            print("Write how many ml of milk do you want to add:")
            added_milk = int(input())
            self.milk += added_milk
            print("Write how many grams of coffee beans do you want to add:")
            added_coffee = int(input())
            self.coffee += added_coffee
            print("Write how many disposable cups of coffee do you want to add:")
            added_cups = int(input())
            self.cups += added_cups

        elif self.state == 'take':
            print(f"i gave you {self.money}")
            self.money = 0

        elif self.state == 'exit':
            exit()


coffee = CoffeeMachine()

while True:
    print("\nWrite action(buy, fill, take, remaining, exit):")
    action = input()
    coffee.interact(action)
