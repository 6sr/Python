from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
options = Options()
options.headless = True
driver = webdriver.Chrome('C:/chromedriver_win32/chromedriver.exe', chrome_options=options)

def getRelated(url):
    channelList = []

    # url = "https://www.youtube.com/channel/UCCTtSp0T63xo2wQ4z9x3ORQ/about"
    # url = "https://www.youtube.com/channel/UCuXE1qQ4pqFhflKeQgcqlrg/about"
    # url = input()
    try:
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


def getDescription(url):

    # url = "https://www.youtube.com/channel/UCCTtSp0T63xo2wQ4z9x3ORQ/about"    
    try:
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

def printChannel(url,i,channels):
    if len(channels) > 10 or i > 10:
        print("Reached")
        for k in channels:
            print(k)
    print(url,end = "  ")
    channels.append(url)
#    print(getDescription(url))
    list = getRelated(url)
    for j in list:
        if channels.count(str(j)) == 0:
            printChannel(str(j),i + 1,channels)

url = "https://www.youtube.com/channel/UCCTtSp0T63xo2wQ4z9x3ORQ/about"
i = 0
channels = []
printChannel(url,i,channels)
input("Continue : ")
