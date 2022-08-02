import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time


URL = "https://in.indeed.com/jobs?q=Job%20Portal&start=40&vjk=b4a17c048930a42a"
#conducting a request of the stated URL above:
page = requests.get(URL)
#specifying a desired format of “page” using the html parser - this allows python to read the various components of the page, rather than treating it as one long string.
soup = BeautifulSoup(page.text,'html.parser')

          
def extract_job_title_from_result(soup): 
    jobs_list = []
    cname_list = []
    sal_list = []
    loc_list = []
    jsumm = []
    results = []
    i=0
    
    resultslist = soup.find('ul',class_="jobsearch-ResultsList css-0")
    for e in resultslist.findAll('li'):
        for a in e.findAll('a',class_="jcs-JobTitle"):
            jobs_list.append(a.get_text())
        for div in e.findAll('div',class_="company_location"):
            cname = div.find('span',class_="companyName").get_text()
            loc = div.find('div',class_="companyLocation").get_text()
            cname_list.append(cname)
            loc_list.append(loc)
            sal_list.append(0)

        for div in e.findAll('div',class_= "salary-snippet-container"):
            sal=div.get_text()
            sal_list[i]=sal
            i+=1
        
    
    dict = {'Job title': jobs_list, 'Company name': cname_list,'Location':loc_list,'Salary':sal_list}
    d=pd.DataFrame(dict)
    return(d)
  


def next_page():
    for i in soup.find_all('a', href = True):
        
      # check all link which  contains /jobs?q=Job+Portal&start
      
      if("/jobs?q=Job+Portal&start" in i['href']):
    
          
        # call get method to request next url
        nextpage = requests.get("http://in.indeed.com"+i['href'])
          
        # create soup for next url
        nextsoup = BeautifulSoup(nextpage.content, 'html.parser')
        
        print(extract_job_title_from_result(nextsoup))
        
        
        
   
df=extract_job_title_from_result(soup)
next_page()

