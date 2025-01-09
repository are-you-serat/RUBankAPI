from fastapi import FastAPI, HTTPException
from scraper import make_req, make_req_using_date, parse_exchange_rate, parse_date_from_page

app = FastAPI()
source_url = 'https://www.cbr.ru/currency_base/daily/'

@app.get('/get_exchange_rates', summary='Получить текущий курс валют')
async def get_exchange_rates():
    result = await make_req()
    exchange_rates = await parse_exchange_rate(result)
    return {'exchange_rates': exchange_rates}

@app.get('/get_rate_by_code/{code}', summary='Получить курс валюты по коду', description=f'Узнать о доступных числовых кодах можно на {source_url} в столбце "Цифр. код"')
async def get_rate_by_code(code: int):
    result = await make_req()
    result_json = await parse_exchange_rate(result)
    for rate in result_json:
        if rate['code'] == code:
            return {'rate' : rate}
    raise HTTPException(status_code=404, detail='Курс валюты с таким кодом не найден')

@app.get('/get_rate_by_letter_code/{letter_code}', summary='Получить курс валюты по буквенному коду', description=f'Узнать о доступных буквенных кодах можно на {source_url} в столбце "Букв. код"')
async def get_rate_by_letter_code(letter_code: str):
    result = await make_req()
    result_json = await parse_exchange_rate(result)
    for rate in result_json:
        if rate['letter_code'] == letter_code:
            return {'rate' : rate}
    raise HTTPException(status_code=404, detail='Курс валюты с таким буквенным кодом не найден')

@app.get('/get_rate_by_date/{date}', summary='Получить курс валюты за указанную дату', description=f'Для получения курса за дату необходимо указать ее в формате dd.mm.yyyy')
async def get_rate_by_date(date: str):
    result = await make_req_using_date(date)
    parsed_date = await parse_date_from_page(result)
    exchange_rates = await parse_exchange_rate(result)
    if date == parsed_date:
        return {'exchange_rates': exchange_rates}
    else:
        raise HTTPException(status_code=404, detail='Курс валюты за указанную дату не найден')