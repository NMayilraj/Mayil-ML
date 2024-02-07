import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"} 

# Here the user agent is for Edge browser on windows 10. You can find your browser user agent from the above given link. 
URL="https://www.sec.gov/Archives/edgar/data/2008979/000200897924000002/xslFormDX01/primary_doc.xml"

r = requests.get(URL, headers=headers) 
    # Send a GET request to the URL
response = requests.get(URL)
Field = response.text
print(Field)
    