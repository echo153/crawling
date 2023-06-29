import json

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import requests

url = 'https://www.youtube.com/@deemd/videos'
service = webdriver.chrome.service.Service('../chromedriver')
driver = webdriver.Chrome(service=service)

driver.get(url)
sleep(3)

soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(soup)

# titles_list = soup.select('#primary #content h3 #video-title')
# print(titles_list)

content_list = soup.select('#primary #content #details #meta')
# print(content_list[0])

views_dict = list()
for content in content_list:
    # print(content)
    title = content.find(attrs={"id": "video-title-link"}).text
    views = content.find('span', class_='inline-metadata-item style-scope ytd-video-meta-block').text
    # print(f'{title} : {views}')

    temp = dict()
    temp['title'] = title
    temp['views'] = views
    views_dict.append(temp)

result_dict = dict()
result_dict['@deemd'] = views_dict

result_json = json.dumps(result_dict, ensure_ascii=False)
print(result_json)
