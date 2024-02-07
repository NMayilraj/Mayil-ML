import requests
from bs4 import BeautifulSoup

# URL of the HTML page
url = "https://brokercheck.finra.org/search/genericsearch/firmgrid"
response = requests.get(url)
print(response)
if response.status_code == 200:
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the specific HTML element using its class name
    target_element = soup.find("span", class_ = "sm:text-sm font-semibold text-base")

    # Extract the text content of the element
    if target_element:
        extracted_text = target_element.get_text(strip=True)
        print(extracted_text)

        # Export the extracted text to a text file
        with open('output.txt', 'w', encoding='utf-8') as file:
            file.write(extracted_text)

        print(f"Successfully extracted and exported the content to 'output.txt'.")
    else:
        print("Target element not found.")
else:
    print(f"Failed to retrieve the HTML content. Status code: {response.status_code}")

