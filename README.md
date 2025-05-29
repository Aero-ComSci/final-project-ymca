![pngtree-awning-store-storefront-striped-stripe-png-image_4904557](https://github.com/user-attachments/assets/60d7e6fb-c17c-4024-bc2f-245a49458228)


# ˜”*°•Ice Cream Shop•°*”˜
We have 2 codes: the main is ICECREAM and the Aryan_ice_cream_code is an additional one cause we had time!

### Who are our customers?
```
This program is our take on the online ordering frenzy of 2025. Now, you can order ice cream online! Our audience does not have a specific range of ages or demographics: everyone can enjoy ice cream! This program is designed for the tech-savvy person who would love a cold, refreshing dessert anytime. They can customize every aspect of their dessert, from size to flavor to toppings. Our program will also apply discounts and deals automatically for the customer's comfort. 
```

### What does the program do?

```
The program serves essentially as an online menu, where the customer can pick and choose what ice cream they want, what toppings, and how many they want as well. It will ask a series of questions regarding their order, where they respond based on what food or toppings they would like. At the end, the program prints the user's order, as well as their total and any discounts they may have.
```

### Screen Recording Video:
https://github.com/user-attachments/assets/b25485dc-dc02-402e-8bfe-dbab56c52cf4

### Function example
```
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
  ```
