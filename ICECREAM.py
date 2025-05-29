menu = ['1','2','3']
cost = 0
amtChoco = 0
amtVan = 0
amtStraw = 0
def toppings()
    tops = input("would you like rainbow sprinkles for 3$? yes/no")
        if tops == "yes"
            cost += 3
            x = input("would you like to order more? yes/no")
            if x == "no"
                break
            elif x != "yes" and x != "no"
                print("Please select if you want to order more. Restarting order")
                cost = 0
                amtChoco = 0
                amtVan = 0
                amtStraw = 0
        elif tops != "no"
            cost = 0
            print("Please select if you want sprinkles. Restarting order")
            cost = 0
            amtChoco = 0
            amtVan = 0
            amtStraw = 0
            continue
def order(cost):
    true = True
    while true == True:
        WhatYouWant = input("What flavor ice cream would you like? Chocolate (1), Vanilla (2), Strawberry (3)")
        
        if str(WhatYouWant) == menu[0]:
            Choco = input("How many chocolate ice creams would you like?")
            if choco.isdigit():
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
        elif str(WhatYouWant) == menu[0]:
            Choco = input("How many chocolate ice creams would you like?")
            if choco.isdigit():
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
        elif str(WhatYouWant) == menu[0]:
            Choco = input("How many chocolate ice creams would you like?")
            if choco.isdigit():
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
    
        
    
    print("Your total cost is: " + str(round(cost, 2)) + "$")

order(0)
