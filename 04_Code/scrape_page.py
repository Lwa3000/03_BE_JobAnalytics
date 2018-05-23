# Dependencies
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
import numpy as np

def scrape(*args):
    max_results_city = 10
    step = 10
    job_search = "data+analyst"
    if args:
        cities = set(args)
    else:
        cities = {"New York", "San Francisco"}

    city_search = [city.replace(" ", "+") for city in cities]
    city_search.sort()
    
    city_list = [city for city in cities] * max_results_city
    city_list.sort()
   
    url_list = get_url_list(city_search, job_search, max_results_city, step)

    results = scrape_links(url_list)
    results["search_city"] = city_list
    
    jobs_df = get_dataframe(results)
    # Save to new csv file
    output = os.path.join('..', '03_Data', 'Job_Data.csv')
    jobs_df.to_csv(output, header=True, index=True, index_label="Id", encoding="utf-8-sig")
    print("Done")
    data = jobs_df.to_dict(orient="records")
    return data

def get_url_list(city_search, job_search, max_results_city, step):
    url_list = []
    for city in city_search:
        for start in range(0, max_results_city, step):
            search_url = "http://www.indeed.com/jobs?q="+str(job_search)+"&l="+str(city)+"&start="+str(start)
            results_page = requests.get(search_url)
            #browser.visit(search_url)
            time.sleep(1)  #ensuring at least 1 second between page grabs
            #html = browser.html
            soup = BeautifulSoup(results_page.text, "lxml",)

            h2 = soup.find_all('h2', class_="jobtitle")
            for stuff in h2:
                href = stuff.find('a')['href']
                url = "http://www.indeed.com/"+str(href)
                url_list.append(url)
    return url_list


def scrape_links(url_list):
    job_company = []
    job_desc = []
    job_location = []
    job_title = []

    for url in url_list:
        job_page = requests.get(url,)
        time.sleep(1) 
        
        job_soup = BeautifulSoup(job_page.text, "lxml")
        
        title=company=location=job_summary="No information"
            
        title_object = job_soup.find("b", class_="jobtitle")
        if title_object is not None:
            title = title_object.text
        job_title.append(title)

        company_object = job_soup.find("span", class_="company")
        if company_object is not None:
            company = company_object.text
        job_company.append(company)

        location_object = job_soup.find("span", class_="location")
        if location_object is not None:
            location = location_object.text
        job_location.append(location)

        job_summary_object = job_soup.find("span", id="job_summary")
        if job_summary_object is not None:
            job_summary = job_summary_object.get_text()
            
        job_desc.append(job_summary)
        
    
    result = { "title":job_title,
               "description": job_desc, 
               "location": job_location,
               "company": job_company,
               "link" : url_list
             }

    return result

def get_dataframe(results):
    jobs_df = pd.DataFrame.from_dict(results)
    jobs_df = jobs_df.dropna(how='any')
    jobs_df = jobs_df[["title","company", "location","description", "search_city", "link"]]
    jobs_df.index = np.arange(1, len(jobs_df) + 1)
    return jobs_df