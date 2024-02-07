import requests
from bs4 import BeautifulSoup

def get_page_text(url):
    # Send a GET request to the URL
    response = requests.get(url)
    print(response.text)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'FormText')
        
        # Extract all text from the parsed HTML
        page_text = soup.get_text()
        
        return page_text
    else:
        # Print an error message if the request was not successful
        print(f"Failed to retrieve page. Status code: {response.status_code}")
        return None

# Example usage
url = "https://www.sec.gov/Archives/edgar/data/2008979/000200897924000002/xslFormDX01/primary_doc.xml"
text_content = get_page_text(url)

# Print the extracted text
print(text_content)
