import requests
from bs4 import BeautifulSoup
import csv

URL = "https://realpython.github.io/fake-jobs/"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

jobs=[]

table =  soup.find('div', attrs = {'id':'ResultsContainer'})


for row in table.find_all('div',
                      attrs = {'class':'column is-half'}):
    job = {}
    job['img'] = row.img['src']
    job['url'] = row.a['href']
    jobs.append(job)

filename = 'fake_jobs.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['img', 'url'])
    w.writeheader()
    for job in jobs:
        w.writerow(job)

print("Data Scraped Successfully")
print("Total jobs:", len(jobs))        
