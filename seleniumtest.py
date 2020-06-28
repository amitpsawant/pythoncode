from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://automatetheboringstuff.com/")

elem = driver.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a:nth-child(1)')
elem.click()

