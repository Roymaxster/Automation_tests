'''
Created on Jul 16, 2013
@author: Maksim Roienko
@company: BinTime
'''
from src.orderForm import orderForm
from selenium.webdriver.support.ui import Select


class ShopppingCart(object):

    def __init__(self, driver):
        self.driver = driver

    def firstProductCart(self):
        return self.driver.find_element_by_xpath(".//*[@id='cartForm']/table/tbody/tr/th/strong/a").text

    def ideal(self, bank):
        self.driver.find_element_by_id("ideal").click()
        Select(self.driver.find_element_by_id("parentId-ideal")).select_by_visible_text(bank)

    def paypal(self):
        self.driver.find_element_by_id("paypal").click()

    def ogone(self, card):
        '''
        ogone(card)
        select payment method and select credit card (visa, mastercard, etc.)
        card = visible text
        How to use: ogone("Visa")
        '''
        self.driver.find_element_by_id("ogonestd").click()
        Select(self.driver.find_element_by_id("parentId-ogonestd")).select_by_visible_text(card)

    def overboeking(self):
        self.driver.find_element_by_id("overboeking").click()

    def rembours(self):
        self.driver.find_element_by_id("rmbrs").click()

    def mistercash(self):
        self.driver.find_element_by_id("mistercash").ckick()

    def afhalen(self):
        self.driver.find_element_by_id("pin").click()

    def verder_met_bestellen(self):
        self.driver.find_element_by_xpath(".//*[@id='paymentForm']/fieldset/button").click()
        return orderForm(self.driver)
