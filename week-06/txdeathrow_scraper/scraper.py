from bs4 import BeautifulSoup
import data_helper
from format_helper import calc_years_diff
from format_helper import make_absolute_url
from format_helper import txdate_to_iso


def get_inmate_data():
   
    inmaterows = get_and_parse_inmate_rows()
    the_data = []
    for row in inmaterows:
        d = wrangle_inmate_data_from_tag(row)
        the_data.append(d)
    return the_data



def get_and_parse_inmate_rows():
    
    import requests
    resp = requests.get('https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/dr_offenders_on_dr.html')
    soup = BeautifulSoup(resp.text, 'lxml')
    rows = soup.select('tr')[1:]
    return rows

def wrangle_inmate_data_from_tag(rowtag):

    import requests
    resp = requests.get('https://wgetsnaps.github.io/tdcj-state-tx-us-2018/death_row/dr_offenders_on_dr.html')
    soup = BeautifulSoup(resp.text, 'lxml')
    rows = soup.select('tr')[1:]
    for rowtag in rows:
        d = {}
        cols = rowtag.select('td')
        d['tdcj_id'] = cols[0].text
        d['url'] = 
        d['last_name'] = cols[2].text
        d['first_name'] = cols[3].text
        d['birth_date'] = cols[4].text
        d['gender'] = cols[5].text
        d['race'] = cols[6].text
        d['date_received']
        d['date_offense']
        d['age_at_offence']
        d['years_before_death_row']
   
    return d