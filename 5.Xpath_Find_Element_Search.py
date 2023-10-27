from selenium import webdriver
import time


# Create a ChromeDriver object
driver = webdriver.Chrome()

# Open a web page
driver.get("https://google.com")

# Wait for the page to load
time.sleep(5)

# Find the search bar element using XPath
search_bar = driver.find_element_by_xpath('//*[@name="q"]')

# Enter a search term
search_bar.send_keys("Selenium")

# Submit the search form
search_bar.submit()

# Wait for the search results to load
time.sleep(5)

# Find the first search result element using XPath
first_search_result = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/a/h3')

# Click on the first search result
first_search_result.click()

# Wait for the search result page to load
time.sleep(5)

# Find the title of the search result page using XPath
search_result_title = driver.find_element_by_xpath('//*[@id="main"]/c-wiz/div/div/div/div/h3').text

# Print the title of the search result page
print(search_result_title)

# Close the driver
driver.quit()
