from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import csv

numChannels = 0
options = Options()
options.headless = True
driver = webdriver.Chrome('C:/chromedriver_win32/chromedriver.exe', chrome_options=options)

def BuildURL(url):
    try:
        driver.get(url)
        res = driver.execute_script("return document.documentElement.outerHTML")
        soup = BeautifulSoup(res, "lxml")

        Ad = soup.find("ytd-app")
        Ad = Ad.find("div",{'id':'content'})
        Ad = Ad.find("ytd-page-manager")
        return Ad
    except:
        print("Check internet connection while building URL")
        return None


def getRelated(url,Ad):
    channelList = []

    # url = "https://www.youtube.com/channel/UCCTtSp0T63xo2wQ4z9x3ORQ/about"
    # url = "https://www.youtube.com/channel/UCuXE1qQ4pqFhflKeQgcqlrg/about"
    # url = input()

    try:
        # BuildURL

        relatedChannels = Ad.find("ytd-browse",{'class':'style-scope ytd-page-manager'})
        relatedChannels = relatedChannels.find("ytd-two-column-browse-results-renderer")
        relatedChannels = relatedChannels.find("div",{"id":"secondary"})
        relatedChannels = relatedChannels.find("ytd-browse-secondary-contents-renderer")
        relatedChannels = relatedChannels.find("div",{"id":"contents"})
    except:
        print("Check internet connection while related")
        return None

    linkFlag = 1
    while True:
        try:
            currChannels = relatedChannels.contents[linkFlag].find("div",{"id":"items"})
            currChannels = currChannels.findAll("ytd-mini-channel-renderer")
            # print("LOL")
            for i in currChannels:
                i = str(i)      # i is ytd-min-channel-renderer tag
                i = re.findall('href="(\S+)"',i)
                # i collects the channel sublink from href of <a> tag in ytd-min-channel-renderer tag
                channelLink = "https://www.youtube.com" + i[0] + "/about" # channelLink is the whole link to channel
                channelList = channelList + [channelLink]
            linkFlag = linkFlag + 1
            # print(linkFlag)
        except:
            break
    return channelList


def getDescription(url,Ad):
    # url = "https://www.youtube.com/channel/UCCTtSp0T63xo2wQ4z9x3ORQ/about"    
    try:
        #BuildURL

        description = Ad.find("ytd-browse",{'class':'style-scope ytd-page-manager'})
        description = description.find("ytd-two-column-browse-results-renderer")
        description = description.find("ytd-section-list-renderer")
        description = description.find("div",{'id':'contents'})
        description = description.find("ytd-item-section-renderer")
        description = description.find("div",{'id':'contents'})
        description = description.find("ytd-channel-about-metadata-renderer")
        description = description.find("div",{'id':'left-column'})
        description = description.find("div",{'id':'description-container'})
        description = description.find("yt-formatted-string",{'id':'description'})
        return str(Ad)
    except:
        print("Check internet connection while description")
        return None

def getCountry(url,Ad):
    try:
        country = Ad.find("ytd-browse",{'class':'style-scope ytd-page-manager'})
        country = country.find("ytd-two-column-browse-results-renderer")
        country = country.find("ytd-section-list-renderer")
        country = country.find("div",{'id':'contents'})
        country = country.find("ytd-item-section-renderer")
        country = country.find("div",{'id':'contents'})
        country = country.find("ytd-channel-about-metadata-renderer")
        country = country.find("div",{'id':'left-column'})
        country = country.find("div",{'id':'details-container'})
        country = country.find("table",{'class':'style-scope ytd-channel-about-metadata-renderer'})
        country = country.find("tbody",{'class':'style-scope ytd-channel-about-metadata-renderer'})
        country = country.findAll("tr",{'class':'style-scope ytd-channel-about-metadata-renderer'})
        country = country[1].findAll("td",{'class':'style-scope ytd-channel-about-metadata-renderer'})
        country = country[0].find("yt-formatted-string",{'class':'style-scope ytd-channel-about-metadata-renderer'}).contents
        return str(country[0])
    except:
        return ""

def getSubscribers(url,Ad):
    try:
        subs = Ad.findAll("ytd-browse",{'class':'style-scope ytd-page-manager'})
        subs = subs[0].find("div",{'id':'header'})
        subs = subs.find("ytd-c4-tabbed-header-renderer")
        subs = subs.find("app-header-layout")
        subs = subs.find("div",{'id':'wrapper'})
        subs = subs.find("app-header",{'id':"header"})
        subs = subs.find("div",{'id':'contentContainer'})
        subs = subs.find("div",{'id':'channel-container'})
        subs = subs.find("div",{'id':'channel-header'})
        subs = subs.find("div",{'id':'channel-header-container'})
        subs = subs.find("div",{'id':'inner-header-container'})
        subs = subs.find("yt-formatted-string",{'id':'subscriber-count'}).contents
        subs = subs[0].split(' ')
        subs = subs[0].split(',')
        ans = ""
        for i in subs:
            ans = ans + str(i)
        return int(ans)
    except:
        return 0

def getName(url,Ad):
    try:
        name = Ad.findAll("ytd-browse",{'class':'style-scope ytd-page-manager'})
        name = name[0].find("div",{'id':'header'})
        name = name.find("ytd-c4-tabbed-header-renderer")
        name = name.find("app-header-layout")
        name = name.find("div",{'id':'wrapper'})
        name = name.find("app-header",{'id':"header"})
        name = name.find("div",{'id':'contentContainer'})
        name = name.find("div",{'id':'channel-container'})
        name = name.find("div",{'id':'channel-header'})
        name = name.find("div",{'id':'channel-header-container'})
        name = name.find("div",{'id':'inner-header-container'})
        name = name.find("h1",{'id':'channel-title-container'})
        name = name.find("span",{'id':'channel-title'}).contents
        return str(name[0])
    except:
        return " "

# check for mail an numbr regular expressions
def getRow(url,Ad):
    row = []
    name = str(getName(url,Ad))
    link = str(url)
    subs = int(getSubscribers(url,Ad))
    description = str(getDescription(url,Ad))
    mail = " "
    number = " "
    try:
        mail = re.findall('\S+@\S+',description)
        mail = str(mail[0])
    except:
        mail = " "
    try:
        number = re.findall("[0-9]\S+",description)
        i = 0
        for i in number:
            if len(i) >= 10:
                break
        number = str(i)
    except:
        number = " "

    # forming current row
    row.append(name)
    row.append(link)
    row.append(subs)
    row.append(mail)
    row.append(number)
    return row

def isPresent(channels,url):
    for i in channels:
        if i[1] == url:
            return False
    return True

def printChannel(url,channels):
    Ad = BuildURL(url)
    if Ad == None:
        print("Ad")
        return None
    if getCountry(url,Ad) != "India":
        print("Coun")
        return None
    if len(channels) >= numChannels:
        print("Reached")
        return None
    
    channels.append(getRow(url,Ad))     # adding url to list
    list = getRelated(url,Ad)       # getting related channels
    if list == None:
        print("Related")
        return None
    for j in list:
        if isPresent(channels,str(j)):        # Checking repitition
            printChannel(str(j),channels)

def buildCSV(list):
    csvList = open("urlList.csv",'a',encoding='utf-8')
    for i in list:
        writer = csv.writer(csvList,delimiter=' ',lineterminator='\r')
        writer.writerow(i)
    csvList.close()




numChannels = int(input("Enter number of channels you want to get : "))
url = str(input("Enter URL : "))
#url = "https://www.youtube.com/channel/UCCTtSp0T63xo2wQ4z9x3ORQ/about"
# https://www.youtube.com/channel/UCFda_3iggsKi_scQFbTIJPw/about        Numchannels = 5 - error why?
# https://www.youtube.com/channel/UCBnnsrvmuQ7tFdTL511dzBQ/about        Numchannels = 5 - no error

channels = []
printChannel(url,channels)
i = int(input("Continue to build csv press 1 : "))
if i == 1:
    buildCSV(channels)

for k in channels:
    print(k)
