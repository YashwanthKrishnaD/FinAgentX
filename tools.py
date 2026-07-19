import yfinance as yf
import pandas as pd


# ---------------- STOCK INFO ---------------- #

def get_stock_data(symbol):

    stock = yf.Ticker(symbol)

    info = stock.info

    data = {}

    data["symbol"] = symbol.upper()
    data["company"] = info.get("longName", "N/A")
    data["sector"] = info.get("sector", "N/A")
    data["industry"] = info.get("industry", "N/A")
    data["country"] = info.get("country", "N/A")
    data["website"] = info.get("website", "N/A")

    data["currentPrice"] = info.get("currentPrice", info.get("regularMarketPrice"))
    data["previousClose"] = info.get("previousClose")
    data["open"] = info.get("open")
    data["dayHigh"] = info.get("dayHigh")
    data["dayLow"] = info.get("dayLow")

    data["fiftyTwoWeekHigh"] = info.get("fiftyTwoWeekHigh")
    data["fiftyTwoWeekLow"] = info.get("fiftyTwoWeekLow")

    data["marketCap"] = info.get("marketCap")
    data["enterpriseValue"] = info.get("enterpriseValue")

    data["pe"] = info.get("trailingPE")
    data["forwardPE"] = info.get("forwardPE")
    data["peg"] = info.get("pegRatio")

    data["eps"] = info.get("trailingEps")
    data["forwardEPS"] = info.get("forwardEps")

    data["beta"] = info.get("beta")

    data["dividendYield"] = info.get("dividendYield")

    data["profitMargins"] = info.get("profitMargins")
    data["operatingMargins"] = info.get("operatingMargins")

    data["revenueGrowth"] = info.get("revenueGrowth")
    data["earningsGrowth"] = info.get("earningsGrowth")

    data["roe"] = info.get("returnOnEquity")
    data["roa"] = info.get("returnOnAssets")

    data["debtToEquity"] = info.get("debtToEquity")

    data["currentRatio"] = info.get("currentRatio")
    data["quickRatio"] = info.get("quickRatio")

    data["employees"] = info.get("fullTimeEmployees")

    return data


# ---------------- PRICE HISTORY ---------------- #

def history(symbol):

    stock = yf.Ticker(symbol)

    hist = stock.history(period="1y")

    return hist


# ---------------- FINANCIALS ---------------- #

def financials(symbol):

    stock = yf.Ticker(symbol)

    return stock.financials


# ---------------- BALANCE SHEET ---------------- #

def balance_sheet(symbol):

    stock = yf.Ticker(symbol)

    return stock.balance_sheet


# ---------------- CASHFLOW ---------------- #

def cashflow(symbol):

    stock = yf.Ticker(symbol)

    return stock.cashflow


# ---------------- NEWS ---------------- #

def news(symbol):

    stock = yf.Ticker(symbol)

    try:
        return stock.news
    except:
        return []


# ---------------- BUFFETT SCORE ---------------- #

def buffett_score(data):

    score = 0

    pe = data.get("pe")
    eps = data.get("eps")
    roe = data.get("roe")
    debt = data.get("debtToEquity")
    growth = data.get("revenueGrowth")
    margin = data.get("profitMargins")
    beta = data.get("beta")

    if pe and pe < 20:
        score += 15
    elif pe and pe < 30:
        score += 10

    if eps and eps > 5:
        score += 15

    if roe and roe > 0.15:
        score += 15

    if debt and debt < 50:
        score += 15

    if growth and growth > 0.10:
        score += 15

    if margin and margin > 0.15:
        score += 15

    if beta and beta < 1.2:
        score += 10

    return min(score,100)


# ---------------- RISK SCORE ---------------- #

def risk_score(data):

    risk = 0

    pe = data.get("pe")
    beta = data.get("beta")
    debt = data.get("debtToEquity")
    growth = data.get("revenueGrowth")
    margin = data.get("profitMargins")

    if pe and pe > 40:
        risk += 2

    if beta and beta > 1.5:
        risk += 2

    if debt and debt > 100:
        risk += 2

    if growth and growth < 0:
        risk += 2

    if margin and margin < 0.05:
        risk += 2

    if risk <= 2:
        level = "Low"

    elif risk <= 5:
        level = "Medium"

    else:
        level = "High"

    return risk, level