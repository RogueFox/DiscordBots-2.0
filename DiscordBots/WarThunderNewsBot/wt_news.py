from lxml import html
import requests

page = requests.get('https://warthunder.com/en/news')
tree = html.fromstring(page.content)

articleNames = tree.xpath('//div[contains(@class, "news-item__anons")]/a[@href]')

webLinks = []
for href in articleNames:
    webLinks.append(href.attrib['href'])
print(webLinks)

postedArticles = open('posted_articles.txt', 'r+')
linkList = postedArticles.read().splitlines()
print(linkList)

postedList = []

for link in webLinks:
    doNotPrint = False
    for post in linkList:
        if(link == post):
            doNotPrint = True
            break
    if(not doNotPrint):
        #post code here
        print(link)
        #add to posted list
        postedList.append(link)

toBeSaved = ""

for link in postedList:
    toBeSaved += (link + "\n")

postedArticles.write(postedArticles.read() + toBeSaved)
postedArticles.close()