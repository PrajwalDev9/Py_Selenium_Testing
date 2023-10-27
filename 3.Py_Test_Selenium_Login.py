from selenium import webdriver
import pytest

class TestSample():

    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Completed")


    def test_login(self,test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.find_element_by_id("username").send_keys("Admin")
        driver.find_element_by_id("password").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        x=driver.title
        assert x == "OrangeHRM"

