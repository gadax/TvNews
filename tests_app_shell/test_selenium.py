from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager


webdriver_service = service.Service(ChromeDriverManager().install())
webdriver_service.start()

chrome_options = Options()
# chrome_options = Options(ChromeDriverManager().install())
chrome_options.add_argument("--headless")
driver = webdriver.Remote(webdriver_service.service_url, options = chrome_options)

def test_default_value_one():
	driver.get("http://localhost:8080/")

	elem = driver.find_element(By.ID, "oneValue")
	assert 1 == int(elem.get_attribute("value"))

	driver.close()

test_default_value_one()