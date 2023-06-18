from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless")

def test_default_value_one():
	driver = webdriver.Chrome(options = chrome_options)
	driver.get("http://localhost:8080/")

	elem = driver.find_element(By.ID, "oneValue")
	assert 1 == elem.get_attribute("value")

	driver.close()


test_default_value_one()