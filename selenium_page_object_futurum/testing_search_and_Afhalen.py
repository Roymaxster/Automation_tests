'''
Created on Jul 16, 2013
@author: Maksim Roienko
@company: BinTime
'''

import unittest
from selenium import webdriver
import time
from src.MainPage import MainPage


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.futurumshop.nl")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()

    def testSearch(self):
        main = MainPage(self.driver)
        product = main.search("Futurumshop Coolmax Cycling Socks Wit")
        assert "Futurumshop Coolmax Cycling Socks Wit" in product.title()
        cart = product.button_buy()
        assert "Futurumshop Coolmax Cycling Socks Wit" in cart.firstProductCart()
        cart.ogone("Visa")
        order = cart.verder_met_bestellen()
        newuser = order.newuser()
        newuser.gender()
        newuser.naam("test name")
        newuser.bedrijfsnaam("test")
        newuser.straat("test str")
        newuser.huisnummer("test house")
        newuser.postcode("12345")
        newuser.plaats("test bintime")
        newuser.telefoon("1234567890")
        newuser.email("test10@bintime.com")
        order_last = newuser.go_to_cart()
        order_last.make_order()
        time.sleep(5)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSearch']
    unittest.main()
