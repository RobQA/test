from Utils import Utils
from selenium.webdriver.support.wait import WebDriverWait


class Logout:

    @staticmethod
    def logout():
        driver = Utils.driver
        driver.find_element_by_class_name('scp-profile-dropdown-button').click()
        driver.find_element_by_class_name('glyphicon-log-out').click()



