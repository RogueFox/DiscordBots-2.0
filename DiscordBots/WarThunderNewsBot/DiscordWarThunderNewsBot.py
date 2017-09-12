import discord
from discord.ext import commands
from lxml import html
import requests

Client = discord.Client()
bot_prefix= "!"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    client.move_member(client,"bots")
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))

@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong!")

@client.command()
async def shutdown():
    await client.say("Disconnecting...")
    await client.close()

@client.command()
async def test():
    await client.say("Connected!")

@client.command()
async def postNews():
    await client.say("Obtaining latest news from War Thunder...")
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

    madeAPost = False
    for link in webLinks:
        doNotPrint = False
        for post in linkList:
            if (link == post):
                doNotPrint = True
                break
        if (not doNotPrint):
            # post code here
            madeAPost = True
            print(link)
            await client.say(link)
            # add to posted list
            postedList.append(link)

    if(not madeAPost):
        await client.say("No new updates from War Thunder...")

    toBeSaved = ""

    for link in postedList:
        toBeSaved += (link + "\n")

    postedArticles.write(postedArticles.read() + toBeSaved)
    postedArticles.close()

input("Press ENTER to start...")
client.run("MzUyOTI5NTg0MzY4NDUxNTg1.DJCCSg.E3JTWtKNCSsIZldR229KY5IIN2M")
input("Press ENTER to exit...")