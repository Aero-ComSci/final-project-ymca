menu = ['1','2','3']

    
def order():
    true = True
    cost = 0
    amtChoco = 0
    amtVan = 0
    amtStraw = 0
    amtSpr = 0
    while true == True:
        WhatYouWant = input("What flavor ice cream would you like? Chocolate (1), Vanilla (2), Strawberry (3)")
        
        if str(WhatYouWant) == menu[0]:
            Choco = input("How many chocolate ice creams would you like?")
            if Choco.isdigit() and int(Choco) > 0:
                cost += int(Choco)*1.75
                amtChoco += int(Choco)
                more = input("would you like to order more? (yes/no)")
                if more == "yes":
                    print("please select your next item")
                elif more == "no":
                    break
                else:
                    print("please select if you want more. Resetting your order.")
                    cost = 0
                    amtChoco = 0
                    amtVan = 0
                    amtStraw = 0
                    amtSpr = 0
                    continue
            else:
                    print("please select how many you want. Resetting your order.")
                    cost = 0
                    amtChoco = 0
                    amtVan = 0
                    amtStraw = 0
                    amtSpr = 0
                    continue
        elif str(WhatYouWant) == menu[1]:
            Van = input("How many vanilla ice creams would you like?")
            if Van.isdigit() and int(Van) > 0:
                cost += int(Van)*1.25
                amtVan += int(Van)
                more = input("would you like to order more? (yes/no)")
                if more == "yes":
                    print("please select your next item")
                elif more == "no":
                    break
                else:
                    print("please select how many you want. Resetting your order.")
                    cost = 0
                    amtChoco = 0
                    amtVan = 0
                    amtStraw = 0
                    amtSpr = 0
                    continue
            else:
                    print("please select if you want more. Resetting your order.")
                    cost = 0
                    amtChoco = 0
                    amtVan = 0
                    amtStraw = 0
                    amtSpr = 0
                    continue
        elif str(WhatYouWant) == menu[2]:
            Straw = input("How many strawberry ice creams would you like?")
            if Straw.isdigit() and int(Straw) > 0:
                cost += int(Straw)*2.0
                amtStraw += int(Straw)
                more = input("would you like to order more? (yes/no)")
                if more == "yes":
                    print("please select your next item")
                elif more == "no":
                    break
                else:
                    print("please select if you want more. Resetting your order.")
                    cost = 0
                    amtChoco = 0
                    amtVan = 0
                    amtStraw = 0
                    amtSpr = 0
                    continue
            else:
                    print("please select how many you want. Resetting your order.")
                    cost = 0
                    amtChoco = 0
                    amtVan = 0
                    amtStraw = 0
                    amtSpr = 0
                    continue
        else:
            print("Please select what you want. Restarting order.")
            cost = 0
            amtChoco = 0
            amtVan = 0
            amtStraw = 0
            amtSpr = 0
            continue
        tops = input("would you like a cup of rainbow sprinkles for 3$? yes/no")
        if tops == "yes":
            cost += 3
            amtSpr += 1
            x = input("would you like to order more? yes/no")
            if x == "no":
                break
            elif x != "yes" and x != "no":
                print("Please select if you want to order more. Restarting order")
                cost = 0
                amtChoco = 0
                amtVan = 0
                amtStraw = 0
                amtSpr = 0
                continue
        elif tops != "no":
            cost = 0
            print("Please select if you want sprinkles. Restarting order")
            cost = 0
            amtChoco = 0
            amtVan = 0
            amtStraw = 0
            amtSpr = 0
            continue
    
        
    print("You have ordered:" + " " + str(amtChoco) + " chocolate icecreams" + "\n" + str(amtVan) + " Vanilla icecreams" + "\n" + str(amtStraw) + " Strawberry icecreams" + "\n" + str(amtSpr) + " cups of sprinkles")
    print("Your total cost is: " + str(round(cost, 2)) + "$")

order()
