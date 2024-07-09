#Switch-Case -> Match case
x = int(input(
'''
Press 1 to Order Pizza
Press 2 to Order Burger
Press 3 to Order Dessert
'''
))

match x:
    case 1:
        print("Pizza Ordered Successfully")
        print("*******case 1 ended********")
    case 2:print("Burger Ordered Successfully")
    case 3:print("Dessert Ordered Successfully")
    #default case
    case _:print("Invalid")
