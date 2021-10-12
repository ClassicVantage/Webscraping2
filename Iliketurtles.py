
from selenium import webdriver
frob bs4 import BeautifulSoup
import time
import csv
import requests

isbrowser=webdriver.Chrome("./chromedriver")

data=[]
starturl="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
headers=["name", "Distance", "mass", "radius"]

def scrapemodedata(hyperlink):
    page=requests.get(hyperlink)
    soup=beautifulSoup(page.content,"html.parcer")
    temlist=[]
    for trtag in soup.find_all("tr",attrs={"class":"fact_row"}):
        tdtag=trtag.find_all("td")
        for tdtags in tdtag:
            try:
                temlist.append(tdtags.find_all("div",attrs={"class":"value"})[0].contents[0])
            except:temlist.append("")
        data.append(temlist)
def scrape():
    
    for i in range(0,428):
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for ultag in soup.find_all("ul",attrs={"class": "onelanet"}) :
            li_tage=ultag.find_all("li")
            temlist=[]
            for index,li_tag in enumerate(li_tage):
                if index==0:
                    temlist.append(li_tage.find_all("A")[0].contents[0])
                else:
                    try:
                        temlist.append(li_tage.contents[0])
                    except:
                        temlist.append("")
            hyperlinklitag=li_tage[0]
            temlist.append("https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"+hyperlinklitag.find_all("a",href=True)[0]["href"])
            planetdata.append(temlist)
        browser.find_element_by_xpath('//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a').clicK()
    
       
scrape()