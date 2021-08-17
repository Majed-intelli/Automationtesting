import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    # def test_search_in_python_org(self):
    #     driver = self.driver
    #     driver.get("http://www.python.org")
    #     self.assertIn("Python", driver.title)
    #     elem = driver.find_element_by_name("q")
    #     elem.send_keys("pycon")
    #     elem.send_keys(Keys.RETURN)
    #     assert "No results found." not in driver.page_source

    def test_lgonintoodoo14(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8069/web/login")
        self.assertIn("Odoo", driver.title)
        username = driver.find_element_by_id("login")
        username.clear
        username.send_keys("admin")
        passwd = driver.find_element_by_id("password")
        passwd.clear
        passwd.send_keys("admin")
        loginbutton = driver.find_element_by_xpath("/html/body/div[1]/main/div/div/div/form/div[3]/button")
        loginbutton.click()
        # employees = driver.find_element_by_
        # employees.click()
        time.sleep(5)
        print(loginbutton.text)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        time.sleep(10)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()