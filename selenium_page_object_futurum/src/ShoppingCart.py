'''
Created on Jul 16, 2013
@author: Maksim Roienko
@company: BinTime
'''
from src.orderForm import orderForm

class ShopppingCart(object):

    def __init__(self, driver):
        self.driver = driver
        
    def firstProductCart(self):
        return self.driver.find_element_by_xpath(".//*[@id='cartForm']/table/tbody/tr/th/strong/a").text
    
    def afhalen(self):
        self.driver.find_element_by_id("pin").click()
        
    def verder_met_bestellen(self):
        self.driver.find_element_by_xpath(".//*[@id='paymentForm']/fieldset/button").click()
        return orderForm(self.driver)