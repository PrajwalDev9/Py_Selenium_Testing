from selenium import webdriver
import unittest
import HtmlTestRunner

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_automationstepbystep(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation")
        self.driver.find_element_by_name("btnK").click()

    def test_search(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Test Search")
        self.driver.find_element_by_name("btnK1").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if _name_ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\Users\prajwal_kumbhar\PycharmProjects\pythonselenium\venv')
