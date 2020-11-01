import os
import unittest

from tests.pages.main_page import MainPage
from tests.pages.address_page import AddressPage

from selenium.webdriver import DesiredCapabilities, Remote


class FirstTest(unittest.TestCase):
    ADDRESS = 'Россия, Москва, 2-я Бауманская улица, 5с1'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy() 
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        addr_page = AddressPage(self.driver)
        addr_page.open()

        addr_page.start_address(self.ADDRESS)

class AddRestaurantTest(unittest.TestCase):
    LOGIN = os.environ['ADMIN_LOGIN']
    PASSWORD = os.environ['ADMIN_PASSWORD']

    ADDRESS = 'Россия, Москва, 2-я Бауманская улица, 5с1'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy() 
        )

        addr_page = AddressPage(self.driver)
        addr_page.open()

        addr_page.start_address(self.ADDRESS)

        main_page = MainPage(self.driver)
        main_page.wait_open()

        main_page.auth(self.LOGIN, self.PASSWORD)

    def tearDown(self):
        self.driver.quit()

    def testUnvalidTitle(self):
        pass

    # def testUnvalidDescription(self):
    #     pass

    # def testUnvalidAddress(self):
    #     pass

    # def testUnvalidRadius(self):
    #     pass

    # def testUnvalidBigPhoto(self):
    #     pass

    # def testUnvalidPhotoFormat(self):
    #     pass

    # def testAddRestaurant(self):
    #     pass
