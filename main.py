import matplotlib.pyplot as plt
import pandas as pd
import requests
from matplotlib.dates import DateFormatter, WeekdayLocator, DayLocator, MONDAY, date2num
from mpl_finance import candlestick_ohlc, candlestick2_ochl
import datetime
from datetime import date


def import_data(ticker, timeseries):
    url, name = None, None
    if timeseries == 'intraday':
        # intraday 指的是一天内的交易数据
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + ticker + '&interval=1min&apikey=' + '9JQS102QXL5THDIL' + '&outputsize=full&datatype=json'
        name = 'Time Series (1min)'
    if timeseries == 'daily':
        # daily指的是每一天的交易数据
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + ticker + '&apikey=' + '9JQS102QXL5THDIL' + '&outputsize=compact&datatype=json'
        name = 'Time Series (Daily)'

    r = requests.get(url, stream=True)
    with open("daily_AAPL.csv", "wb") as csv_file:
        for line in r.iter_lines():
            csv_file.write(line)




def pandas_candlestick_ohlc(dat, ticker, lag="day", label_date=None, x1=0, x2=0, apple=None):
    mondays = WeekdayLocator(MONDAY)
    all_days = DayLocator()

    transdat = dat.loc[:, ["Open", "High", "Low", "Close"]]
    if type(lag) == str:
        if lag == "day":
            plotdat = transdat
            w = 1
        elif lag in ["week", "month", "year"]:
            if lag == "week":
                transdat["week"] = pd.to_datetime(transdat.index).map(lambda x: x.isocalendar()[1])  # 定义每一周
                w = 7
            elif lag == "month":
                transdat["month"] = pd.to_datetime(transdat.index).map(lambda x: x.month)  # 定义一个月
                w = 30
            elif lag == "year":
                w = 365
            transdat["year"] = pd.to_datetime(transdat.index).map(lambda x: x.isocalendar()[0])  # 定义一年
            grouped = transdat.groupby(list({"year", lag}))
            plotdat = pd.DataFrame({"Open": [], "High": [], "Low": [], "Close": []})
            for name, group in grouped:
                plotdat = plotdat.append(pd.DataFrame({"Open": group.iloc[0, 0],
                                                       "High": max(group.High),
                                                       "Low": min(group.Low),
                                                       "Close": group.iloc[-1, 3]},
                                                      index=[group.index[0]]))
    else:
        raise ValueError('Valid inputs to argument "lag" include the strings "day", "week", "month", "year"')

    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2)
    weekFormatter = DateFormatter('%b %d, %Y')
    ax.xaxis.set_major_locator(mondays)
    ax.xaxis.set_minor_locator(all_days)
    ax.xaxis.set_major_formatter(weekFormatter)
    ax.grid(True)

    candlestick_ohlc(ax, list(
        zip(list(date2num(plotdat.index.tolist())), plotdat["Open"].tolist(), plotdat["High"].tolist(),
            plotdat["Low"].tolist(), plotdat["Close"].tolist())),
                     colorup="red", colordown="green", width=w * .4)

    if label_date is not None:
        dt = date2num(datetime.datetime.strptime(label_date, '%Y-%m-%d').date())
        ax.annotate(str(apple.loc[label_date, 'High']), xy=(dt - 2, x1))
        ax.annotate(str(apple.loc[label_date, 'Low']), xy=(dt - 2, x2))

    ax.xaxis_date()
    ax.autoscale_view()
    plt.title(ticker)
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

    plt.show()


def main():
    apple = import_data('AAPL', 'daily')  # 'GOOGL'/'GOOG'; 'MSFT'
    cols = apple.columns
    apple[cols] = apple[cols].apply(pd.to_numeric, errors='coerce')  # 将每一列转化成数字变量
    apple.index = pd.to_datetime(apple.index, format='%Y-%m-%d')  # 将索引转化成时间变量
    plt.figure(figsize=(10, 5))  # 改变图片大小
    apple["Close"].plot(grid=True)
    plt.title('Close Price of AAPL')
    plt.show()

    mondays = WeekdayLocator(MONDAY)  # 用于横坐标设定，每个显示的横坐标都是周一
    alldays = DayLocator()  # 横坐标的最小单位为一天

    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2)
    weekFormatter = DateFormatter('%b %d, %Y')  # 设置坐标显示的日期格式Jun 5, 2018
    ax.xaxis.set_major_locator(mondays)
    ax.xaxis.set_minor_locator(alldays)
    ax.xaxis.set_major_formatter(weekFormatter)
    ax.grid(True)
    candlestick_ohlc(ax, list(zip(list(date2num(apple.index.tolist())), apple["Open"].tolist(), apple["High"].tolist(),
                                  apple["Low"].tolist(), apple["Close"].tolist())),
                     colorup="red", colordown="green", width=1 * .4)

    ax.xaxis_date()
    ax.autoscale_view()
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.title('AAPL')
    plt.show()

    dt = date2num(date(2019, 4, 9))
    ax.annotate(str(apple.loc['2019-04-09', 'High']), xy=(dt - 2, 175))
    ax.annotate(str(apple.loc['2019-04-09', 'Low']), xy=(dt - 2, 168))

    pandas_candlestick_ohlc(apple.loc['2019-01-26':'2018-04-26', :], ticker='AAPL', lag='day', label_date='2018-04-09', x1=175, x2=168, apple=apple)


if __name__ == '__main__':
    main()
