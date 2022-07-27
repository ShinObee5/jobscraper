import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time

from tabulate import tabulate

URL = "https://in.indeed.com/jobs?q=Job%20Portal&start=10&vjk=e9f2a2b350096e8f&advn=5777929391423421"
#conducting a request of the stated URL above:
page = requests.get(URL)
#specifying a desired format of “page” using the html parser - this allows python to read the various components of the page, rather than treating it as one long string.
soup = BeautifulSoup(page.text,'html.parser')
#printing soup in a more structured tree format that makes for easier reading
#print(soup.prettify())


 
def extract_job_title_from_result(soup): 
    jobs_list = []
    cname_list = []
    sal = []
    loc_list = []
    jsumm = []
    results = []
    
    resultslist = soup.find('ul',class_="jobsearch-ResultsList css-0")
    for e in resultslist.findAll('li'):
        for a in e.findAll('a',class_="jcs-JobTitle"):
            jobs_list.append(a.get_text())
        for div in e.findAll('div',class_="company_location"):
            cname = div.find('span',class_="companyName").get_text()
            loc = div.find('div',class_="companyLocation").get_text()
            cname_list.append(cname)
            loc_list.append(loc)
        #results.append(e)

        
    print(jobs_list)
    print(cname_list)
    print(loc_list)
    dict = {'jtitle': jobs_list, 'company': cname_list,'location':loc_list}
    df=pd.DataFrame(dict)
  
   
extract_job_title_from_result(soup)

