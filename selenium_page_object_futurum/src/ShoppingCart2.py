
class ShoppingCart2(object):
    def __init__(self, driver):
        self.driver = driver

    def make_order(self):
        self.driver.find_element_by_xpath(".//*[@id='payment_select']/button[2]").click()
