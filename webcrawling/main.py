import sys
sys.path.insert(0,'/chromedriver')
import pandas as pd
import requests
import urllib.request as ur
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from tqdm import tqdm
from web_crawling import web_scraping
from web_loading import web_loading

if __name__ == "__main__":
    
    url = 'https://search.naver.com/search.naver?where=blog&query=%ED%99%94%EC%88%9C+%EC%97%AC%ED%96%89&sm=tab_opt'

    chrome_options = webdriver.ChromeOptions() 
    chrome_options.add_argument('--headless') 
    chrome_options.add_argument('--no-sandbox') 
    chrome_options.add_argument('--disable-dev-shm-usage') 
    browser = webdriver.Chrome('chromedriver',chrome_options=chrome_options) 


    browser.maximize_window()
    browser.get(url)
    count=int(input('불러오고 싶은 블로그 갯수 : '))
    여행 = dict(zip(['Title', 'URL', 'Text'], [[], [], []]))
    N = (count-30)//30 + 1

    web_loading(N)
    web_scraping(count)