#web scraping
'''
pip install requests
pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Lets use the requests get method to fetch the data from url

response = requests.get(url)
# lets check the status
status = response.status_code
print(status) # 200 means the fetching was successful

import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # gives the whole page on the website
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0] # the result is a list, we are taking out data from it
for td in table.find('tr').find_all('td'):
    print(td.text)
'''

#Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
import requests
from bs4 import BeautifulSoup
import json
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
#extraction of the main content from the website
content =soup.find('div', class_='content') or soup
data={}

#getting all headings and their following lists and paragraphs
for tag in content.find_all(['h2', 'h3', 'p', 'li']):
    text = tag.get_text(strip=True)
    if not text:
        continue
    if ':' in text and len(text) < 250:
        key, value = text.split(':', 1)
        data[key.stip()] = value.strip()
    else:
        #for paragraphs without colon , store by heading
        data[text[:50]] = text

#saving data as a json file
with open('bu_facts_stats.json', 'w', encoding= 'utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii = False)

print('Done! Data saved to bu_facts_stats.json')
print(json.dumps(data,indent=2)[:1000])

#Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file
#Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.