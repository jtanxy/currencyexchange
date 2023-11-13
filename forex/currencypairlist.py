import yahooquery as yq
import pandas as pd
import json
import bs4
import requests
from requests.models import PreparedRequest
from forex.models import CurrencyPairs


COLUMNS = ["symbol", "name"]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "DNT": "1",
    "Connection": "close",
}


# Function to get all a list of all currencies
def get_currencies():
    data = yq.get_currencies()
    x = json.dumps(data)
    df = pd.read_json(x, orient="columns")
    # print(df['symbol'])
    return df


# get lookup url for available symbols
def get_symbol_lookup_webpage(symbol):
    print("Given symbol :\n", symbol)
    url = "https://finance.yahoo.com/lookup/currency?"
    params = {"s": symbol, "t": "A", "b": "0", "c": "200"}
    req = PreparedRequest()
    req.prepare_url(url, params)
    print("Print req url: ", req.url)
    response = requests.get(req.url, verify=False, headers=headers)
    return bs4.BeautifulSoup(response.text, "html.parser")


# scrape through the webpage to get the symbol of all currency pairs
def scrape(webpage):
    try:
        rows = webpage.find("table").find_all("tr")
        cy_data = []
        for row in rows:
            cells = row.find_all("td")[0:2]
            cy_data.append([cell.text for cell in cells])
        return cy_data
    except Exception:
        pass


# retrieve the symbols and save in CurrencyPairs table
def save_currency_pairs():
    currency = get_currencies()
    cy_pairs = pd.DataFrame()
    for i in range(len(currency)):
        symbol = currency.loc[i, "symbol"]
        page = get_symbol_lookup_webpage(symbol)
        data = scrape(page)
        if data is not None:
            list1 = [x for x in data if x != []]
            df = pd.DataFrame(list1)
            cy_pairs = pd.concat([cy_pairs, pd.DataFrame(df)], ignore_index=True)
    cy_pairs.columns = COLUMNS
    cy_pairs[["source_ccy", "target_ccy"]] = cy_pairs["name"].str.split(
        "/", expand=True
    )
    cy_pairs = cy_pairs[cy_pairs["target_ccy"].notna()]
    print(cy_pairs)
    df_records = cy_pairs.to_dict("records")

    model_instances = [
        CurrencyPairs(
            symbol=record["symbol"],
            source_currency=record["source_ccy"],
            target_currency=record["target_ccy"],
        )
        for record in df_records
    ]

    CurrencyPairs.objects.bulk_create(model_instances, ignore_conflicts=True)
