from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Create a ChromeDriverManager object
chrome_driver_manager = ChromeDriverManager()

# Install the latest ChromeDriver
chrome_driver_manager.install()

# Create a ChromeDriver object
driver = webdriver.Chrome()

# Open a web page
driver.get("https://google.com")

# Find the search bar element
search_bar = driver.find_element_by_name("q")

# Enter a search term
search_bar.send_keys("Selenium")

# Submit the search form
search_bar.submit()

# Wait for the page to load
driver.wait_for_page_load()

# Print the page title
print(driver.title)

# Close the driver
driver.quit()
