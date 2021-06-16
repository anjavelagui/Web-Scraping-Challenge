#Import dependencies and setup
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd
import os
from splinter import Browser
import time

# initializing browser
def init_browser():
    executable_path = {"executable_path": ChromeDriverManager().install()}
    browser = Browser("chrome", **executable_path, headless=False)

mars_info ={}

def scrape():
    browser = init_browser()
    #---Visit Mars News Web site---
    browser.visit("https://mars.nasa.gov/news/")
    time.sleep(1)

    #----Scrape web site into BS----
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    #---finding articles titles---
    results_art = soup.find_all('div', class_="content_title")
    latest_news = results_art[0].text
    #---Getting the paragraph----
    para_cont = soup.find_all('div', class_="article_teaser_body")
    latest_para = para_cont[0].text
    



