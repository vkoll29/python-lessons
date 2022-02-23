from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('https://www.twitter.com')
assert "Twitter" in driver.title

# el = driver.find_element_by_name('q')
# el.clear()
# el.send_keys('pycon')
# el.send_keys(Keys.RETURN)
# assert "No Results Found" not in driver.page_source
# driver.close()
