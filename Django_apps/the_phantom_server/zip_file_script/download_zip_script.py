import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin


url = "https://www.rrc.texas.gov/resource-center/research/data-sets-available-for-download/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    tables = soup.find_all("table")
    for table in tables:
        if "Digital Map Data" in table.get_text():
            cells = table.find_all("td", {"data-label": "Download"})
            for cell in cells:
                link = cell.find_next_sibling("td").find("a")
                if link:
                    file_url = link.get("href")
                    full_file_url = urljoin(url, file_url)
                    file_name = full_file_url.split("/")[-1]
                    print(f"Downloading {file_name} from {full_file_url}...")
                    file_response = requests.get(full_file_url)
                    with open(file_name, "wb") as file:
                        file.write(file_response.content)
                    print(f"{file_name} downloaded successfully.")

else:
    print("Failed to fetch the page")
