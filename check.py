import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(options=chrome_options)

    def tearDown(self):
        self.driver.quit()

    def test_search_in_python_org(self):
        browser = self.driver
        browser.get("http://www.python.org")
        self.assertIn("Python", browser.title)
        elem = browser.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in browser.page_source


if __name__ == "__main__":
    unittest.main()
