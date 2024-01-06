import requests
from bs4 import BeautifulSoup as bs
import time

start_time = time.time()

pages = []


for page_number in range(1, 4):
    url = 'https://www.centralcharts.com/en/price-list-ranking/ALL/desc/ts_29-us-nyse-stocks--qc_2-daily-change?p=' + str(page_number)
    pages.append(url)

values_list = []

for page in pages:
    webpage = requests.get(page)
    soup = bs(webpage.text, 'html.parser')

    stock_table = soup.find('table', class_='tabMini tabQuotes')
    tr_tag_list = stock_table.find_all('tr')

    for each_tr_tag in tr_tag_list[1:]:
        td_tag_list = each_tr_tag.find_all('td')

        row_values = []
        for each_td_tag in td_tag_list[0:7]:
            new_value = each_td_tag.text.strip()
            row_values.append(new_value)
        
        if int(row_values[6].replace(',', '')) >= 500000:
            values_list.append([row_values[0], row_values[2], row_values[6]])

for row in values_list:
    print(row[0], "Daily Price Change(%): " + row[1], "Volume: " + row[2])

print('---%s seconds ---' % (time.time() - start_time))
