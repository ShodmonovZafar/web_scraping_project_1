from bs4 import BeautifulSoup

def convert_soup_to_csv(soup):
    """Convert soup to csv.
    Args:
        soup: object(BeautifulSoup)
    Return:
        csv_data: str
    """
    div_tag_1 = soup.div
    print(type(div_tag_1.contents[4]))
    pass
    
def save_data_to_csv(data, path_csv_file):
    with open(path_csv_file, 'w') as f:
        f.write(data)