import requests
from bs4 import BeautifulSoup
import csv
import re

base_url = "https://southpark.fandom.com"
index_url = base_url + "/wiki/Category:Scripts"

response = requests.get(index_url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all the episode scripts in the index page
script_links = [a["href"] for a in soup.find_all("a", href=True) if "/wiki/File:" in a["href"]]

# Iterate through each script link and extract the content
rows = []
import tqdm
for script_link in tqdm.tqdm(script_links):
    script_url = base_url + script_link
    response = requests.get(script_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the headerscontent table in the HTML
    table = soup.find_all('table', {'class': 'headerscontent'})[1]

    # Extract the content from the table and store it in a list of rows
    for tr in table.find_all('tr'):
        td = [td.text for td in tr.find_all('td')]
        if len(td) == 2 and td[0].strip() and td[1].strip(): # Check if both columns are occupied
            speaker = "Cartman" if "Eric" in td[0] or "Cartman" in td[0] else "[OTH]"
            sentences = td[1].strip()
            sentences =' '.join(word for word in re.split(r'\s*\[.*?\]\s*', sentences) if word) # Remove everything within square braces
            rows.append([speaker, sentences])

# Write the content of the list to a CSV file
filename = "all_scripts_filtered.csv"
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Speaker", "Sentences"])
    writer.writerows(rows)

print(f"All the scripts have been extracted, filtered, and saved to the file {filename}.")
