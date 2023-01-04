def make_pizza(size, *topings):
    '''Summarinze the pizza we are about to make.'''
    print(f'\nMaking a {size}-inch pizza with the following toppings')
    for topping in topings:
        print(f"-{topping}")


def make_cheese(size, *toping):
    print(f"\nPreparing a {size} the cheese with the following toppings")
    for toping in toping:
        print(f"-{toping}")
