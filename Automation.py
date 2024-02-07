from selenium import webdriver

# Create a new Chrome WebDriver instance
driver = webdriver.Chrome()

# Navigate to the web page that contains the element whose ID you want to find
driver.get("https://dev.xml-edge.com/login")

# Find the element with the specified ID
element = driver.find_element(by=id)

# Get the ID of the element
element_id = element.get_attribute("id")

# Print the ID of the element
print(element_id)

# Close the Chrome browser
# driver.quit()