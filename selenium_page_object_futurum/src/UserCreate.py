'''
Created on Jul 19, 2013

@author: test
'''
from src.ShoppingCart2 import ShoppingCart2


class UserCreate(object):
    def __init__(self, driver):
        self.driver = driver

    def gender(self):
        self.driver.find_element_by_id("fc_sex_M").click()

    def naam(self, param):
        self.driver.find_element_by_id("fc_voornaam").send_keys(param)

    def bedrijfsnaam(self, param):
        self.driver.find_element_by_id("fc_company").send_keys(param)

    def straat(self, param):
        self.driver.find_element_by_id("fc_straat").send_keys(param)

    def huisnummer(self, param):
        self.driver.find_element_by_id("fc_huisnummer").send_keys(param)

    def postcode(self, param):
        self.driver.find_element_by_id("fc_postcode").send_keys(param)

    def plaats(self, param):
        self.driver.find_element_by_id("fc_plaats").send_keys(param)

    def land(self):
        self.driver.find_element_by_xpath(
            ".//*[@id='newUserForm']//fieldset[2]//select").click()

    def telefoon(self, param):
        self.driver.find_element_by_id("fc_telefoon").send_keys(param)

    def email(self, param):
        self.driver.find_element_by_id("fc_email").send_keys(param)

    def go_to_cart(self):
        self.driver.find_element_by_xpath(".//*[@id='newUserForm']/div/div[3]/button").click()
        return ShoppingCart2(self.driver)
