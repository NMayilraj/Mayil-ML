from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up Chrome options (headless mode to run without opening a browser window)
chrome_options = Options()
chrome_options.add_argument("--headless")

# Specify the path to your ChromeDriver executable
chrome_driver_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

# URL of the HTML page
url = "https://brokercheck.finra.org/search/genericsearch/firmgrid"


# Start the Chrome browser
with webdriver.Chrome(service=ChromeService(chrome_driver_path), options=chrome_options) as driver:
    # Navigate to the URL
    driver.get(url)

    # Find the specific HTML element using its class name
    target_element = driver.find_element(By.CSS_SELECTOR, "span.sm:text-sm.font-semibold.text-base")
    print(target_element)

    # Extract the text content of the element
    if target_element:
        extracted_text = target_element.text
        print(extracted_text)

        # Export the extracted text to a text file
        with open('C:\\Users\\Mayilraj\\Downloads\\EDGAR_Form_D_XML_Technical_Specification\\output.txt', 'w', encoding='utf-8') as file:
            file.write(extracted_text)

        print(f"Successfully extracted and exported the content to 'output.txt'.")
    else:
        print("Target element not found.")
