import yfinance as yf

msft = yf.Ticker("MSFT")

#Added ticker info

print(msft.info)
print(msft.info['regularMarketPrice'])