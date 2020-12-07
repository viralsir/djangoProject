from unittest import TestCase
import os
import pathlib
from selenium import webdriver

def file_uri(filename):
    return pathlib.path(os.path.abspath(filename)).as_uri()

driver= webdriver.Chrome()

# driver.get("http://127.0.0.1:8000/flights/counter")
# print(driver.title)
# print(driver.page_source)
#
# increase=driver.find_element_by_id("increase")
#
# increase.click()
# increase.click()
# increase.click()
# increase.click()
#
# for i in range(100):
#     increase.click()
#
# decrease=driver.find_element_by_id("decrease")
#
# decrease.click()
# decrease.click()

class webpagetest(unittest.TestCase):

    def setup(self):




