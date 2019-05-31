#!//usr/bin/env python

# Part 4: Class Report
# Using the classes to write a new module
# that will generate random products and print a summary
# Module includes: generate_products and inventory_report

import random
from acme import Product
from collections import defaultdict
from functools import reduce

products = []
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(n=30):
    count = n
    while(count > 0):
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0, 2.5)
        name = f'{random.choice(ADJECTIVES)} {random.choice(NOUNS)}'
        info = Product(name, price, weight, flammability)
        products.append(info)
        count -= 1
    return products


def inventory_report(names_list):
    # list all the names made
    names = [names_list[i].name for i in range(len(names_list))]
    # using defaultdict to count unique names (products)
    inventory_names = defaultdict(int)
    for name in names:
        inventory_names[name] += 1

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique Products : ', len(inventory_names))

    price = []
    weight = []
    flammability = []
    for dict in products:
        price.append(dict.price)
        weight.append(dict.weight)
        flammability.append(dict.flammability)

    def mean(names_list):
        mean = reduce(lambda x, y: x+y, names_list)/len(names_list)
        return mean

    print('Average Price:', mean(price))
    print('Average Weight:', mean(weight))
    print('Average Price:', mean(flammability))

if __name__ == '__main__':
    inventory_report(generate_products())

