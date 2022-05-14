import talib
import yfinance as yf
    
# get ohlc data and scan it 
def candlestick_scan():
    data = yf.download("PINS", start="2022-05-10", end="2022-05-13", interval="5m")
    print(data)

    # signals breakout long with 100 and short with -100
    num = talib.CDLMARUBOZU(data['Open'], data['High'], data['Low'], data['Close'])
    print(num)
    print(num[num != 0])

candlestick_scan()