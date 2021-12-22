water = 400
milk = 540
beans = 120
dcups = 9
money = 550

while True:
    ans = input("Write action (buy, fill, take, remaining, exit): ")
    if ans == "remaining":
        print(f'''
The coffee machine has:
{water} of water
{milk} of milk
{beans} of coffee beans
{dcups} of disposable cups
${money} of money
''')
    elif ans == "buy":
        tcoff = str(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: "))
        if tcoff == "back" or tcoff == "4":
            pass
        if tcoff == "espresso" or tcoff == "1":
            if water >= 250 and beans >= 16:
                print("I have enough resources, making you a coffee!")
                money += 4
                water -= 250
                beans -= 16
                dcups -= 1
            elif water < 250:
                print("Sorry, not enough water!\n")
            elif beans < 16:
                print("Sorry, not enough beans!\n")
            elif dcups < 1:
                print("Sorry, not enough cups\n")
        elif tcoff == "latte" or tcoff == "2":
            if water >= 350 and beans >= 20 and milk >= 75:
                money += 7
                water -= 350
                milk -= 75
                beans -= 20
                dcups -= 1
            elif water < 350:
                print("Sorry, not enough water!\n")
            elif beans < 20:
                print("Sorry, not enough beans!\n")
            elif dcups < 1:
                print("Sorry, not enough cups\n")
            elif milk < 75:
                print("Sorry, not enough milk\n")
        elif tcoff == "cappuccino" or tcoff == "3":
            if water >= 200 and beans >= 12 and milk >= 100:
                money += 6
                water -= 200
                milk -= 100
                beans -= 12
                dcups -= 1
            elif water < 200:
                print("Sorry, not enough water!\n")
            elif beans < 12:
                print("Sorry, not enough beans!\n")
            elif dcups < 1:
                print("Sorry, not enough cups\n")
            elif milk < 100:
                print("Sorry, not enough milk\n")
        elif tcoff == "0":
            pass
        else:
            pass
    elif ans == "take":
        print()
        print(f"I gave you ${money}")
        money -= money
    elif ans == "fill":
        water += int(input("Write how many ml of water do you want to add: "))
        milk += int(input("Write how many ml of milk do you want to add: "))
        beans += int(input("Write how many grams of coffee beans do you want to add: "))
        dcups += int(input("Write how many disposable cups of coffee do you want to add:"))
        print()
    elif ans == "exit":
        break