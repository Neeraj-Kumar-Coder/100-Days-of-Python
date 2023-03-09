import requests
from bs4 import BeautifulSoup

URL = "https://www.w3schools.com/howto/howto_website_static.asp"

response = requests.get(url=URL)
print(f"Time to get the request = {response.elapsed}")

# Web Scraping
soup = BeautifulSoup(response.text, "html.parser")
h2s = soup.find_all("h2")

for h2 in h2s:
    print(h2.text)
