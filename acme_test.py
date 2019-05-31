#!/usr/bin/env python

# Part 5: Measure Twice, Test Once
# Add min 2 more test methods to AcmeProductTests
# Write a new test class with at least 2 test methods:
# test_default_num_products & test_legal_names

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Testing default product price as 10"""
        prod = Product('Testing Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Testing default product weight at 10"""
        prod = Product('Testing Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability(self):
        """Testing stealability()"""
        prod = Product('Testing Product')
        self.assertEqual(prod.stealability(), 'Kinda stealable.')

    def test_explode(self):
        """Testing explode()"""
        prod = Product('Testing Product')
        self.assertEqual(prod.explode(), '...boom!')


class AcmeReportTests(unittest.TestCase):
    """ Testing generate_products returning 30 results"""
    def test_default_num_products(self):
        prods = generate_products()
        self.assertEqual(len(prods), 30)

    def test_legal_names(self):
        """ Testing if the names are in the correct format """
        # valid lists of adjectives and nouns
        adjectives = set(['Awesome', 'Shiny', 'Impressive', 'Portable',
                         'Improved'])
        nouns = set(['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???'])
        # generate product names from report
        products = generate_products()
        # split into adjectives and nouns
        bad_adjectives = [prod.name.split()[0] for prod in products
                          if prod.name.split()[0] not in adjectives]
        bad_nouns = [prod.name.split()[1] for prod in products
                     if prod.name.split()[1] not in nouns]
        self.assertEqual(len(bad_adjectives), 0)
        self.assertEqual(len(bad_nouns), 0)


if __name__ == '__main__':
    unittest.main() 
# PEP8 Errors: 1 - Same whitespace stuff

