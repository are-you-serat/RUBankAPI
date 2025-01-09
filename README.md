# RUBankAPI
A modern API for accessing real-time and historical financial data from the Central Bank of Russia.

## Key Features  
- 📊 **Real-Time Exchange Rates**: Get up-to-date currency exchange data.  
- 🕰️ **Historical Data**: Access past rates for analysis.  
- ⚙️ **Customizable Queries**: Flexible filters for specific data needs.  
- 🚀 **Fast & Reliable**: Optimized for performance and scalability.  

## Getting Started  
1. Clone the repository.  
2. ```cd ExchangeRates```
3. ```pip install requirements.txt```
4. ```fastapi dev main.py```
5. Go to http://127.0.0.1:8000/docs for documentation.
6. Start using the API to power your financial applications!  

## Libraries used in the API
1. beautifulsoup4 - for cbr.ru parsing.
2. fastapi - for api development.
3. aiohttp - for asynchronous http requests.
