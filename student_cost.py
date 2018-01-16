""" # Problem Summary
    You work at a pizza restaurant, which is starting to accept orders online. You need to
    provide a python function that will accept arbitrary orders, and compute the correct
    price for the order.

    A single pizza order is formed as a list of toppings. For example
       A pizza with no toppings (other than cheese and sauce is: [] (an empty list)
       A pizza with pepperoni and a double order of olives is : ["pepperoni", "olives", "olives"]
    *An arbitrary number of pizzas may be ordered, including no pizzas as all*

    Drinks come in as a named order (i.e. a keyword argument 'drinks'). If drinks are ordered,
    they are specified as a list of sizes ("small", "medium", "large", "tub").

    Wings come in as a named order as well (keyword argument 'wings'). If wings are ordered,
    they are specified as a list of integers (10, 20, 40, 100).

    A coupon may be specified as the keyword argument 'coupon'. It is will be a single
    floating point number between 0 and 1. This indicates the fraction of the *pre-tax*
    price that is to be subtracted.

    A 6.25% tax is applied to every order. The tax is computed on the total cost of the
    order *before a coupon is applied*

    Round the price to the nearest cent, using the built-in function round.
      round(x, 2) will round x to two decimal places.


    The prices are as follows:

    Plain Pizza
    -----------
    $13.00

    Toppings
    -------
    pepperoni : $1.00
    mushroom : $0.50
    olive : $0.50
    anchovy : $2.00
    ham : $1.50

    Drinks
    ------
    small : $2.00
    medium : $3.00
    large : $3.50
    tub : $3.75

    Wings
    -----
    10 : $5.00
    20 : $9.00
    40 : $17.50
    100 : $48.00


    # Examples
    The following is an order for a plain pizza, a ham and anchovy pizza, two "tub"-sized
    drinks, with a 10%-off coupon:

    >>>cost_calculator([], ["ham", "anchovy"], drinks=["tub", "tub"], coupon=0.1)
    35.61

    This order consists only of a small drink.
    >>>cost_calculator(drinks=["small"])
    2.12

    # Details
    Assume that the front-end of the website will never pass your function erroneous
    orders. That is, you will never receive orders for items that do not exist nor
    items that contain typos.

    Consider defining individual functions responsible for computing
    the cost of the pizzas, drinks, and wings, respectively. Have `cost_calculator`
    invoke these.

    Our `cost_calculator` signature is empty. Part of the assignment is to come up with the
    correct function signature!
"""


def cost_pizzas(pizza):
    result = 0.0
    for topping in pizza:
        if topping == "pepperoni":
            result += 1.0
        elif topping == "mushroom":
            result += 0.5
        elif topping == "olive":
            result += 0.5
        elif topping == "anchovy":
            result += 2.0
        else:
            result += 1.5
    return result


def cost_drinks(drinks):
    result = 0.0
    for drink in drinks:
        if drink == "small":
            result += 2.0
        elif drink == "medium":
            result += 3.0
        elif drink == "large":
            result += 3.5
        else:
            result += 3.75
    return result


def cost_wings(wings):
    result = 0.0
    for wing in wings:
        if wing == 10:
            result += 5.0
        elif wing == 20:
            result += 9.0
        elif wing == 40:
            result += 17.5
        else:
            result += 48.0
    return result


def cost_calculator(*args, drinks=[], wings=[], coupon=0):
    pizza_cost = 0
    for arg in args:
        pizza_cost += 13.0 + cost_pizzas(arg)
        print(pizza_cost)
    drinks_cost = cost_drinks(drinks)
    print(drinks_cost)
    wings_cost = cost_wings(wings)
    print(wings_cost)
    after_coupon = (pizza_cost + drinks_cost + wings_cost) * coupon
    #print ("Cost", (1.0625 * (pizza_cost + drinks_cost)) * (1.0 - coupon))
    return round(1.0625 * (pizza_cost + drinks_cost + wings_cost) - after_coupon, 2)

print(cost_calculator([], coupon=0.05))