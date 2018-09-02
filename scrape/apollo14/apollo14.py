#!/usr/bin/env python3
import os
import requests
from bs4 import BeautifulSoup
import json

"""
Apollo 14 Lunar Flight Journals:

https://www.hq.nasa.gov/alsj/main.html

Apollo 14 Lunar Surface Journals:

https://www.hq.nasa.gov/alsj/a14/a14.html
"""


def apollo14_lfj_scrape_index():
    """
    Scrape the index of the Apollo 14 Lunar Flight Journal.
    Get each link to a "Day X" page.
    Request the contents of each "Day X" page.
    Save it to a file for later processing.
    """
    scrape_dir = 'data'

    lfj_base_link = 'https://web.archive.org/web/20171225232133/https://history.nasa.gov/afj/ap14fj/'

    lfj_base_page = 'index.html'

    headers = {'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}

    # Make a soup from the page HTML
    r = requests.get(lfj_base_link, headers = headers)
    html_doc = r.text
    soup = BeautifulSoup(html_doc,"lxml")

    # Extract each link to a "Day X" page
    log_links = []
    
    a_s = soup.find_all('a')

    for a_ in a_s:
        link_text = a_.get_text()
        if 'Day ' in link_text:
            page_name = a_.attrs['href']
            link_name = lfj_base_link + page_name
            log_links.append(link_name)

    # Follow those links!!!
    # Save each page to disk
    if not os.path.exists(scrape_dir):
        os.mkdir(scrape_dir)

    for i,link in enumerate(log_links):

        dest = os.path.join(scrape_dir, os.path.basename(link))

        if not os.path.exists(dest):

            print("Scraping...")
            print("    Link: %s"%(link))
            print("    Target file: %s"%(dest))

            r = requests.get(link, headers=headers)
            html_doc = r.content.decode('utf-8')
            soup = BeautifulSoup(html_doc,"lxml")

            with open(dest,'w') as f:
                f.write(soup.text)

            print("Success!\n")

        else:

            print("Skipping %s, file already exists..."%(dest))


def apollo14_lfj_extract_dialogue():
    """
    Use the saved "Day X" pages on disk to exract dialogue.
    """
    pass


if __name__=="__main__":
    apollo14_lfj_scrape_index()

