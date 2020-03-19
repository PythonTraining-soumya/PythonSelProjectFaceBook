from selenium.webdriver.common.by import By


class HomePage:

    # create a constructor to get the knowledge of the driver
    def __init__(self, driver):
        self.driver = driver
    shop = (By.LINK_TEXT, "Shop")   # shop is a class variable
    # the first value will be the type of locator , second value will be the value of the locator
    # assign the two values in a tuple data type

    def shopIcon(self):
        return self.driver.find_element(*HomePage.shop)
        # as driver ids the instance variable it is called using self.driver
        # as the shop is a class variable if you want to call it use class name.class variable
        # and put * in front of the class name so that it will read the variable as a tuple and will deserialize it
        # if you want to call a variable declared in  the function(instance variable)then use self .variable name

