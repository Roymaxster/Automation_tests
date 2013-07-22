'''
Created on Jul 16, 2013
@author: Maksim Roienko
@company: BinTime
'''
from src.ProductPage import ProductPage

class MainPage(object):
    def __init__(self, driver):
        self.driver = driver
    
    def search(self, param1):
        self.driver.find_element_by_id("fc_search").send_keys(param1)
        self.driver.find_element_by_id("searchBarButton").click()
        return ProductPage(self.driver)