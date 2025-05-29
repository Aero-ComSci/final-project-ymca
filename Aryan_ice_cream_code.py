def ice_cream():
    cost = 0
    number_of_icecreams = input("How many icecreams would you like to order (enter a number)? ")
    if number_of_icecreams.isdigit():
        for i in range(int(number_of_icecreams)):
            order = input("Icecream #" + str(i+1) + " - Choose type (chocolate $1.75, vanilla $1.25, strawberry $1.50): ")
            if order == "chocolate" or order == "choco":
                print("You selected chocolate for $1.75")
                cost += 1.75
            elif order == "vanilla" or order == "vanilla $1.25":
                print("You selected vanilla for $1.25")
                cost += 1.25
            elif order == "strawberry" or order == "strawberry $1.50":
                print("You selected strawberry for $1.50")
                cost += 1.50
            else:
                print("That was not an option")
                ice_cream()
    else:
        print("Invalid input")
        ice_cream()
    return cost

def cone_or_cup():
    cost = 0
    answer = input("Would you like a cone or cup?: ")
    if answer == "cone":
        cone_list = ["Chocolate cone", "Regular cone", "Waffle cone"]
        print(cone_list)
        selected_cone = input("Select a cone from the options above: ")
        if selected_cone == cone_list[0]:
            print("You selected a chocolate cone.")
            cost += 1.00
        elif selected_cone == cone_list[1]:
            print("You selected a regular cone.")
            cost += 0.50
        elif selected_cone == cone_list[2]:
            print("You selected a waffle cone.")
            cost += 0.75 
        else:
            print("Invalid input")
            cone_or_cup()
    elif answer == "cup":
        print("You did ordered a cup.")
        cost += 0.50
    else:
        print("Invalid response, please answer with yes or no")
        cone_or_cup()
    return cost

def toppings():
    cost = 0
    scoops_of_sprinkles = input("Select how many scoops of sprinkles you want: ")
    if scoops_of_sprinkles.isdigit():
        cost += float(scoops_of_sprinkles)*cost
    else:
        print("Invalid input")
        toppings()
    return cost


total_cost = 0
icecream_cost = ice_cream()
cone_or_cup_cost = cone_or_cup()
toppings_cost = toppings()


total_cost = icecream_cost + cone_or_cup_cost + toppings_cost

if icecream_cost > 0 and cone_or_cup_cost > 0 and toppings_cost > 0:
    total_cost -= 1

print("Your cost is: $" + str(total_cost))