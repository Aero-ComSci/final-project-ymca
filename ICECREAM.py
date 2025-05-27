menu = ['1','2','3','4','5','6','7','8','9','10']
cost = 0

def order(cost):
    true = True
    amtChicken = 0
    amtBeef = 0
    amtTofu = 0
    amtSmallDrink = 0
    amtMedDrink = 0
    amtBigDrink = 0
    amtSmallFries = 0
    amtMedFries = 0
    amtBigFries = 0
    amtKetchup = 0
    while true == True:
        WhatYouWant = input("What would you like? (Chicken(1), Beef(2), Tofu(3), Small Drink(4), Medium Drink(5), Large Drink(6), Small Fries(7), Medium Fries(8), Large Fries(9), Ketchup Packets(10))")
        
        if str(WhatYouWant) == menu[0]:
            Chicken = input("How many Chicken sandwiches would you like?")
            if Chicken.isdigit() and int(Chicken) > 0:
                cost += int(Chicken)*5.25
                amtChicken += int(Chicken)
                more = input("Would you like to order more? (yes/no)")
                if more == "yes":
                    print("Please select your next item.")
                elif more == "no":
                    break
                else:
                    print("Please enter if you want to order more")
                    cost = 0
            else:
                print("Please enter a positive number. Restarting order.")
                cost = 0

        if str(WhatYouWant) == menu[1]:
            Beef = input("How many beef sandwiches would you like?")
            if Beef.isdigit() and int(Beef) > 0:
                cost += int(Beef)*6.25
                amtBeef += int(Beef)
                more = input("Would you like to order more? (yes/no)")
                if more == "yes":
                    print("Please select your next item.")
                elif more == "no":
                    break
                else:
                    print("Please enter if you want to order more")
                    cost = 0
            else:
                print("Please enter a positive number. Restarting order.")
                cost = 0

        if str(WhatYouWant) == menu[2]:
            Tofu = input("How many Tofu sandwiches would you like?")
            if Tofu.isdigit() and int(Tofu) > 0:
                cost += int(Tofu)*5.75
                amtTofu += int(Tofu)
                more = input("Would you like to order more? (yes/no)")
                if more == "yes":
                    print("Please select your next item.")
                elif more == "no":
                    break
                else:
                    print("Please enter if you want to order more")
                    cost = 0
            else:
                print("Please enter a positive number. Restarting order.")
                cost = 0

        if str(WhatYouWant) == menu[3]:
            SmallDrink = input("How many small drinks would you like?")
            if SmallDrink.isdigit() and int(SmallDrink) > 0:
                cost += int(SmallDrink)*1
                amtSmallDrink += int(SmallDrink)
                more = input("Would you like to order more? (yes/no)")
                if more == "yes":
                    print("Please select your next item.")
                elif more == "no":
                    break
                else:
                    print("Please enter if you want to order more")
                    cost = 0
            else:
                print("Please enter a positive number. Restarting order.")
                cost = 0

        if str(WhatYouWant) == menu[4]:
            MedDrink = input("How many medium drinks would you like?")
            if MedDrink.isdigit() and int(MedDrink) > 0:
                cost += int(MedDrink)*1.75
                amtMedDrink += int(MedDrink)
                more = input("Would you like to order more? (yes/no)")
                if more == "yes":
                    print("Please select your next item.")
                elif more == "no":
                    break
                else:
                    print("Please enter if you want to order more")
                    cost = 0
            else:
                print("Please enter a positive number. Restarting order.")
                cost = 0

        if str(WhatYouWant) == menu[5]:
            BigDrink = input("How many big drinks would you like?")
            if BigDrink.isdigit() and int(BigDrink) > 0:
                cost += int(BigDrink)*2.25
                amtBigDrink += int(BigDrink)
                more = input("Would you like to order more? (yes/no)")
                if more == "yes":
                    print("Please select your next item.")
                elif more == "no":
                    break
                else:
                    print("Please enter if you want to order more")
                    cost = 0
            else:
                print("Please enter a positive number. Restarting order.")
                cost = 0

        if str(WhatYouWant) == menu[6]:
            SmallFries = input("How many small fries would you like?")
            if SmallFries.isdigit() and int(SmallFries) > 0:
                cost += int(SmallFries)*1
                amtSmallFries += int(SmallFries)
                more = input("Would you like to order more? (yes/no)")
                if more == "yes":
                    print("Please select your next item.")
                elif more == "no":
                    break
                else:
                    print("Please enter if you want to order more")
                    cost = 0
            else:
                print("Please enter a positive number. Restarting order.")
                cost = 0

        if str(WhatYouWant) == menu[7]:
            MediumFries = input("How many medium fries would you like?")
            if MediumFries.isdigit() and int(MediumFries) > 0:
                cost += int(MediumFries)*1.50
                amtMedFries += int(MediumFries)
                more = input("Would you like to order more? (yes/no)")
                if more == "yes":
                    print("Please select your next item.")
                elif more == "no":
                    break
                else:
                    print("Please enter if you want to order more")
                    cost = 0
            else:
                print("Please enter a positive number. Restarting order.")
                cost = 0

        if str(WhatYouWant) == menu[8]:
            BigFries = input("How many big fries would you like?")
            if BigFries.isdigit() and int(BigFries) > 0:
                cost += int(BigFries)*2
                amtBigFries += int(BigFries)
                more = input("Would you like to order more? (yes/no)")
                if more == "yes":
                    print("Please select your next item.")
                elif more == "no":
                    break
                else:
                    print("Please enter if you want to order more")
                    cost = 0
            else:
                print("Please enter a positive number. Restarting order.")
                cost = 0

        if str(WhatYouWant) == menu[9]:
            Ketchup = input("How many ketchup packets would you like?")
            if Ketchup.isdigit() and int(Ketchup) > 0:
                cost += int(Ketchup)*0.25
                amtKetchup += int(Ketchup)
                more = input("Would you like to order more? (yes/no)")
                if more == "yes":
                    print("Please select your next item.")
                elif more == "no":
                    break
                else:
                    print("Please enter if you want to order more")
                    cost = 0
            else:
                print("Please enter a positive number. Restarting order.")
                cost = 0

    print("You have ordered: \n " + str(amtChicken) + " #1's \n" +str(amtBeef) + " #2's \n" +str(amtTofu) + " #3's \n" +str(amtSmallDrink) + " #4's \n" +str(amtMedDrink) + " #5's \n" +str(amtBigDrink) + " #6's \n" +str(amtSmallFries) + " #7's \n" +str(amtMedFries) + " #8's \n" +str(amtBigFries) + " #9's \n" +str(amtKetchup) + " #10's")
    print("Your total cost is: " + str(round(cost, 2)) + "$")

order(0)