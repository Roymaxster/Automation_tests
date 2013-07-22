'''
Created on Jul 16, 2013
@author: Maksim Roienko
@company: BinTime
'''
from src.UserCreate import UserCreate

class orderForm(object):
    def __init__(self, driver):
        self.driver = driver
        
    def newuser(self):
        self.driver.find_element_by_xpath(".//*[@id='content']//form/button").click()
        return UserCreate(self.driver)

