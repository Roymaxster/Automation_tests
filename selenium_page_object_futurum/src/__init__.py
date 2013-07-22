'''
Created on Jul 16, 2013
@author: test
'''

import unittest
from selenium import webdriver
import time
from src import MainPage


class Test(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.futurumshop.nl")
        self.driver.implicitly_wait(10)


    def tearDown(self):
        self.driver.close()


    def testSearch(self):
        time.sleep(10)
        main = MainPage(self.driver)
        result = main.search("Futurumshop Coolmax Cycling Socks Wit")
        assert "Futurumshop Coolmax Cycling Socks Wit" in result.title()
        cart = result.button_buy()
        assert "Futurumshop Coolmax Cycling Socks Wit" in cart.firstProductCart()
        cart.afhalen()
        cart.verder_met_bestellen()
        time.sleep(10)
        
              


if __name__ == "__main__":
    unittest.main()