import yfinance as yf
from datetime import datetime
from forex.models import CurrencyPairs, DailyRates

HIST_RATE_PERIOD = "1mo"


def save_historical_rates():
    currencylist = list(CurrencyPairs.objects.all().values_list("symbol", flat=True))

    # Download all historical tickers from yfinance
    data = yf.download(currencylist, period=HIST_RATE_PERIOD)
    # TRANSFORM MULTI-LEVEL INDEX INTO A SINGLE-INDEX SET OF COLUMNS.
    data = data.stack(level=1).rename_axis(["Date", "Symbol"]).reset_index(level=1)
    data = data.reset_index(level="Date")

    # Save historical records into DailyRates table
    df_records = data.to_dict("records")
    model_instances = [
        DailyRates(
            currency_pairs=CurrencyPairs.objects.get(symbol=record["Symbol"]),
            date=record["Date"],
            high=record["High"],
            low=record["Low"],
            close=record["Close"],
            last_updated=datetime.now(),
        )
        for record in df_records
    ]

    DailyRates.objects.bulk_create(model_instances, ignore_conflicts=True)


def save_daily_rates():
    currencylist = list(CurrencyPairs.objects.all().values_list("symbol", flat=True))

    # Download all historical tickers from yfinance
    data = yf.download(currencylist, period="1d")
    # Transform multi-level index into single-index
    data = data.stack(level=1).rename_axis(["Date", "Symbol"]).reset_index(level=1)
    data = data.reset_index(level="Date")

    # Save daily rate records into DailyRates table
    df_records = data.to_dict("records")
    model_instances = [
        DailyRates(
            currency_pairs=CurrencyPairs.objects.get(symbol=record["Symbol"]),
            date=record["Date"],
            high=record["High"],
            low=record["Low"],
            close=record["Close"],
            last_updated=datetime.now(),
        )
        for record in df_records
    ]

    DailyRates.objects.bulk_create(model_instances, ignore_conflicts=True)


def get_daily_rates():
    currencylist = list(CurrencyPairs.objects.all().values_list("symbol", flat=True))

    # Download all historical tickers from yfinance
    data = yf.download(currencylist, period="1d")
    # Transform multi-level index into single-index
    data = data.stack(level=1).rename_axis(["Date", "Symbol"]).reset_index(level=1)
    print(data)
    return data.reset_index(level="Date")
