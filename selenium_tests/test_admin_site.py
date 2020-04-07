"""
Selenium test module for Django administration site
"""
import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class TestAdminSite(unittest.TestCase):
    """
    TestCase class for Django administration site
    """
    USER = 'instructor'
    PWD = 'maverick1a'

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Edge('C:\\Users\\JordonTrujillo\\Documents\\temp\\web-application-' +
                                    'development-isqa-3900\\edgedriver_win64\\msedgedriver.exe')
        cls.driver.maximize_window()
        cls.driver.get('http://127.0.0.1:8000/admin')

    def test_login(self):
        """
        Test administration login
        :return: returns nothing
        """
        elem = self.driver.find_element_by_id('id_username')
        elem.send_keys(self.USER)
        elem = self.driver.find_element_by_id('id_password')
        elem.send_keys(self.PWD)
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)

        self.assertTrue(self.driver.find_element_by_id('user-tools'))

    def test_logout(self):
        """
        Test administration logout
        :return: returns nothing
        """
        self.driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/a[3]').click()
        time.sleep(4)

        self.assertTrue(self.driver.find_element_by_id('content'))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
