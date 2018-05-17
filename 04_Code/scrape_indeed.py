import time
from splinter import Browser
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import pymongo
from pprint import pprint
import datetime


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    max_results_per_city = 100
    city_search = ['New York', 'San Francisco']
    job_search = "data analyst"  

    url = 'https://www.indeed.com/jobs?q=data+analyst&l=San+Francisco%2C+CA'
    url2 = 'https://www.indeed.com/jobs?q=data+analyst&l=New+York%2C+NY'

    browser.visit(url)
    time.sleep(2)
    positions_SF = []
    positions_NY = []
    for i in range(0, 10):
        time.sleep(5)
        html = browser.html
        soup_SF = BeautifulSoup(html, "html.parser")
        positions_SF.append(scrape_city(soup_SF, "San Francisco"))
        browser.click_link_by_partial_text('Next')
    
    # browser.visit(url2)
    # time.sleep(2)
    # for x in range(0, 10):
    #     time.sleep(2)
    #     html = browser.html
    #     soup_NY = BeautifulSoup(html, "html.parser")
    #     positions_NY.append(scrape_city(soup_NY, "New York"))
    #     browser.click_link_by_partial_text('Next')

    return positions_SF
    
    
def scrape_city(soup, city):
    # Extract position information
    ls_titles = extract_job_title_from_result(soup)
    ls_companies = extract_company_from_result(soup)
    ls_locations = extract_location_from_result(soup)
    ls_summary = extract_summary_from_result(soup)
    ls_links = extract_link_from_result(soup)
    
    # print(f"Titles {len(ls_titles)}")
    # print(f"Companies {len(ls_companies)}")
    # print(f"Locations {len(ls_locations)}")
    # print(f"Summary {len(ls_summary)}")
    # print(f"Links {len(ls_links)}")

    positions = []
    d = {}
    idx = 0
    while idx < len(ls_titles):
        d["title"] = ls_titles[idx]
        d["company"] = ls_companies[idx]
        d["location"] = ls_locations[idx]
        d["summary"] = ls_summary[idx]
        d["link"] = ls_links[idx]
        d["Scrape datetime"] = datetime.datetime.utcnow()
        d["city"] = city
        positions.append(d)
        d = {}
        idx += 1
    return positions

def extract_job_title_from_result(soup):
    jobs = []
    results = soup.find_all(name="div", attrs={"class": "row"})
    for result in results:
        for a in result.find_all(name="a", attrs={"data-tn-element": "jobTitle"}):
            jobs.append(a["title"])
    return jobs


def extract_company_from_result(soup):
    companies = []
    for div in soup.find_all(name="div", attrs={"class": "row"}):
        company = div.find_all(name="span", attrs={"class": "company"})
        if len(company) > 0:
            for b in company:
                companies.append(b.text.strip())
        else:
            sec_try = div.find_all(name="span", attrs={
                                   "class": "result-link-source"})
            for span in sec_try:
                companies.append(span.text.strip())
    return companies


def extract_location_from_result(soup):
    locations = []
    spans = soup.findAll('span', attrs={'class': 'location'})
    for span in spans:
        locations.append(span.text)
    return(locations)


def extract_summary_from_result(soup):
    summaries = []
    spans = soup.findAll('span', attrs={'class': 'summary'})
    for span in spans:
        summaries.append(span.text.strip())
    return(summaries)


def extract_link_from_result(soup):
    links = []
    results = soup.find_all(name="div", attrs={"class": "row"})
    for result in results:
        for a in result.find_all(name="a", attrs={"class": "jobtitle"}, href=True):
            links.append("https://www.indeed.com"+a["href"])

    results = soup.find_all(name="h2", attrs={"class": "jobtitle"})
    for result in results:
        for a in result.find_all(name="a", href=True):
            links.append("https://www.indeed.com"+a["href"])
    return links
