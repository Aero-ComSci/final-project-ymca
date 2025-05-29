menu = ['1','2','3']
cost = 0
amtChoco = 0
amtVan = 0
amtStraw = 0
    
def order(cost, amtChoco, amtVan, amtStraw):
    true = True
    while true == True:
        WhatYouWant = input("What flavor ice cream would you like? Chocolate (1), Vanilla (2), Strawberry (3)")
        
        if str(WhatYouWant) == menu[0]:
            Choco = input("How many chocolate ice creams would you like?")
            if Choco.isdigit():
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
        elif str(WhatYouWant) == menu[1]:
            Van = input("How many chocolate ice creams would you like?")
            if Van.isdigit():
                cost += int(Van)*1.25
                amtVan += int(Van)
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
        elif str(WhatYouWant) == menu[2]:
            Straw = input("How many chocolate ice creams would you like?")
            if Straw.isdigit():
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
        else:
            print("Please select what you want. Restarting order.")
            cost = 0
            amtChoco = 0
            amtVan = 0
            amtStraw = 0
            cost(0,0,0,0)
        tops = input("would you like rainbow sprinkles for 3$? yes/no")
        if tops == "yes":
            cost += 3
            x = input("would you like to order more? yes/no")
            if x == "no":
                break
            elif x != "yes" and x != "no":
                print("Please select if you want to order more. Restarting order")
                cost = 0
                amtChoco = 0
                amtVan = 0
                amtStraw = 0
        elif tops != "no":
            cost = 0
            print("Please select if you want sprinkles. Restarting order")
            cost = 0
            amtChoco = 0
            amtVan = 0
            amtStraw = 0
            continue
    
        
    
    print("Your total cost is: " + str(round(cost, 2)) + "$")

order(0, 0 ,0 ,0)
