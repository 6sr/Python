from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

def getDescription(url):
    options = Options()
    options.headless = True

    # url = "https://www.youtube.com/channel/UCCTtSp0T63xo2wQ4z9x3ORQ/about"    
    try:
        driver = webdriver.Chrome('C:/chromedriver_win32/chromedriver.exe', chrome_options=options)
        driver.get(url)
        res = driver.execute_script("return document.documentElement.outerHTML")
        soup = BeautifulSoup(res, "lxml")

        route = soup.find("ytd-app")
        Ad = route.find("div",{'id':'content'})
        Ad = Ad.find("ytd-page-manager")
        Ad = Ad.find("ytd-browse",{'class':'style-scope ytd-page-manager'})
        Ad = Ad.find("ytd-two-column-browse-results-renderer")

        Ad = Ad.find("ytd-section-list-renderer")
        Ad = route.find("div",{'id':'contents'})
        Ad = Ad.find("ytd-item-section-renderer")
        Ad = route.find("div",{'id':'contents'})
        Ad = Ad.find("ytd-channel-about-metadata-renderer")
        Ad = route.find("div",{'id':'left-column'})
        Ad = route.find("div",{'id':'description-container'})
        Ad = route.find("yt-formatted-string",{'id':'description'})
    except:
        print("Check internet connection")
        return ""
    return str(Ad)

url = "https://www.youtube.com/channel/UCCTtSp0T63xo2wQ4z9x3ORQ/about"    
description = getDescription(url)
print("LOL")
print(description)

