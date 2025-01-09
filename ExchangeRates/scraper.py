import aiohttp
from bs4 import BeautifulSoup
import asyncio
import re

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
pattern = re.compile(r'\d{2}\.\d{2}\.\d{4}')

async def make_req():
    async with aiohttp.ClientSession() as session:
        responce = await session.get('https://www.cbr.ru/currency_base/daily/')
        html = await responce.text()
        return html

async def make_req_using_date(datetime):
    async with aiohttp.ClientSession() as session:
        responce = await session.get(f'https://www.cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To={datetime}')
        html = await responce.text()
        return html

async def parse_date_from_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    date = soup.find('h2', class_='h3').text.strip()
    date = pattern.findall(date)[0]
    return date

async def parse_exchange_rate(html):
    exchange_list = []
    new_list = []
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find_all('table', class_='data')
    for tr in table:
        tr = tr.find_all('tr')
        if tr:
            for text in tr:
                list_ = [text.text.strip()]
                exchange_list.append(list_)
    exchange_list.pop(0)
    i = 0
    while i < len(exchange_list):
        new_string = ''.join(exchange_list[i])
        new_string = new_string.split('\n')
        code = int(new_string[0])
        letter_code = new_string[1]
        amount = int(new_string[2])
        currency = new_string[3]
        rate = new_string[4].replace(',', '.')
        rate = float(rate)
        json_ = {
            'code': code,
            'letter_code': letter_code,
            'amount': amount,
            'currency': currency,
            'rate': rate,
        }
        new_list.append(json_)
        i += 1
    return new_list