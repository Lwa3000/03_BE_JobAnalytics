# Dependencies
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd

max_results_per_city = 100
city_search = ['New York', 'San Francisco']
job_search = "data analyst"

url_list = [] # will hold list of urls for each job

for city in city_search:
    for start in range(0, max_results_per_city, 10):
        search_url = "http://www.indeed.com/jobs?q="+str(job_search)+"&l="+str(city)+"&start="+str(start)
        results_page = requests.get(search_url)
        time.sleep(1)  #ensuring at least 1 second between page grabs
        soup = BeautifulSoup(results_page.text, "html.parser")

        h2 = soup.find_all('h2', class_="jobtitle")
        for stuff in h2:
            href = stuff.find('a')['href']
            url = "http://www.indeed.com/"+str(href)
            url_list.append(url)

job_company = []
job_desc = []
job_location = []
job_title = []

for url in url_list:
    job_page = requests.get(url)
    job_soup = BeautifulSoup(job_page.text, "html.parser")
    
    title = job_soup.find("b", class_="jobtitle").text
    job_title.append(title)
    
    company = job_soup.find("span", class_="company").text
    job_company.append(company)
    
    location = job_soup.find("span", class_="location").text
    job_location.append(location)
    
    job_summary = job_soup.find("span", id="job_summary").get_text(strip=True)
    job_desc.append(job_summary)

example_df = pd.DataFrame({"title": job_title,
                           "company": job_company,
                           "location": job_location,
                           "description": job_desc})
print