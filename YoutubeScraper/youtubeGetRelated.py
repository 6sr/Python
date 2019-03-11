from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

def getRelated(url):
    channelList = []
    options = Options()
    options.headless = True

    # url = "https://www.youtube.com/channel/UCCTtSp0T63xo2wQ4z9x3ORQ/about"
    # url = "https://www.youtube.com/channel/UCuXE1qQ4pqFhflKeQgcqlrg/about"
    # url = input()
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

        relatedChannels = Ad.find("div",{"id":"secondary"})
        relatedChannels = relatedChannels.find("ytd-browse-secondary-contents-renderer")
        relatedChannels = relatedChannels.find("div",{"id":"contents"})
    except:
        print("Check internet connection")
        return ""

    linkFlag = 1
    while True:
        try:
            currChannels = relatedChannels.contents[linkFlag].find("div",{"id":"items"})
            currChannels = currChannels.findAll("ytd-mini-channel-renderer")
            print("LOL")
            for i in currChannels:
                i = str(i)      # i is ytd-min-channel-renderer tag
                i = re.findall('href="(\S+)"',i)
                # i collects the channel sublink from href of <a> tag in ytd-min-channel-renderer tag
                channelLink = "https://www.youtube.com" + i[0] + "/about" # channelLink is the whole link to channel
                channelList = channelList + [channelLink]
            linkFlag = linkFlag + 1
            print(linkFlag)
        except:
            break
    return channelList

url = "https://www.youtube.com/channel/UCCTtSp0T63xo2wQ4z9x3ORQ/about"
list = getRelated(url)
for i in list:
    print(i)
