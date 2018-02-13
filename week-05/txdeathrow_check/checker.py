from data_helper import get_html
from bs4 import BeautifulSoup
txt = get_html()
soup = BeautifulSoup(txt, 'lxml')
rows = soup.select('tr')

def get_and_parse_inmate_rows():
    
    return rows[1:]

def count_inmates():
    
    return len(rows[1:])
