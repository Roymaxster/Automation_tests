'''
Created on Jul 16, 2013
@author: Maksim Roienko
@company: BinTime
'''
from src.ShoppingCart import ShopppingCart

class ProductPage(object):
    def __init__(self, driver):
        self.driver = driver
        
    def title(self):
        return self.driver.find_element_by_xpath("//*[@id='productContent']/div[1]/h1").text
    
    def button_buy(self):
        self.driver.find_element_by_xpath(".//*[@id='saleButton']/button").click()
        return ShopppingCart(self.driver)