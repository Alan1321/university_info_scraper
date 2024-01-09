from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from io import StringIO


def scrape_all(url, course):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find the tag with name="course"
    target_tag = soup.find(name='a', attrs={'name': f'{course}'})

    # Print the text content of the found tag
    if target_tag:
        return target_tag.text
    else:
        print("Tag not found.")