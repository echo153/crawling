from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

url = 'https://front.wemakeprice.com/best'  # 요청
service = webdriver.chrome.service.Service('../chromedriver')
driver = webdriver.Chrome(service=service)

driver.get(url)
sleep(5)

soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(soup)

item_list = soup.select('.box_listwrap')
items = soup.find_all('div', class_='list_conts_wrap')

for item in items:
    product = item.find('p', class_='text').text
    rank = item.find('span', class_='num').text
    price = item.find('em', class_='num').text

    print(f'{rank} 순위 : {product}, {price} KRW')

driver.close()
