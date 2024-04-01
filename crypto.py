import lxml.html
import requests
import asyncio
import aiohttp
import httpx
from bs4 import BeautifulSoup


#tree.xpath'de class ismini xpath olarak kopyaladım. (Bu link sürekli değiştiği için)
#ama python'da değişen class isimlerini nasıl yapacağımı henüz çözemedim
#tree yapısı kullanılacak büyük ihtimal

async def fetch_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.text()
            tree = lxml.html.fromstring(content)

            crypto = tree.xpath('/html/body/div[2]/div[6]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/span[1]/span[1]')

            if crypto:
                print(crypto[0].text_content())
            else:
                print("Crypto element not found.")

url = "https://tr.tradingview.com/chart/yyTaeE4j/?symbol=CRYPTO%3ABTCUSD"
asyncio.run(fetch_page(url))
