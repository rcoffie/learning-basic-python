def make_cheese(size, *toppings):
    print(f'\nPreparing cheese with the {size} of toppings')
    for topping in toppings:
        print(f" -{topping}")