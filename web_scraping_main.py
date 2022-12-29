import requests
import functions
from bs4 import BeautifulSoup

# Step 1: Find the URL that you want to scrape.
URL = "https://imlo.uz/letter/A"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# Step 2: Inspecting the Page.
# This step is performed in a web browser.

# Step 3: Find the data you want to extract.
# This step is performed in a web browser.

# Step 4: Write the code.
# This step is performed in a functions.py modul.

# Step 5: Run the code and extract the data.
data = functions.convert_soup_to_csv(soup)  # Step 5.1
print(data)  # Step 5.2

# Step 6: Store the data in the required format.
#path_csv_file = "csv_files/data_1.csv"  # Step 6.1
#functions.save_data_to_csv(data, path_csv_file)  Step 6.2
