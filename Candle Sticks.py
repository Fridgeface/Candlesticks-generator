import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv(r"./GBPCHF_Ticks_10.08.2020-10.08.2020.csv")

data.columns = ["Date", "open", "close", "Ask_vol", "Bid_vol"]

data["Date"] = pd.to_datetime(data["Date"])

data = data.drop_duplicates(keep=False)

data["Minute"] = data["Date"].dt.minute

Minutes = data["Minute"].tolist()
closePrices = data["close"].tolist()
openPrices = data["open"].tolist()

PreviousCandleSticks = {}
listOfPrices = []
counter = 0

listofMaxes = []
listofMins = []
listofOpens = []
listofCloses = []
timeMH = []

for i in range(1, len(data["close"])):

    if i == 0 or Minutes[i] == Minutes[i - 1]:
        listOfPrices.append(round(closePrices[i], 5))
        maxPrice = max(listOfPrices)
        minPrice = min(listOfPrices)

    elif Minutes[i] != Minutes[i - 1] and len(listOfPrices) != 0:

        openPrice = listOfPrices[-len(listOfPrices)]
        closePrice = listOfPrices[len(listOfPrices) - 1]

        listofMaxes.append(maxPrice)
        listofMins.append(minPrice)
        listofOpens.append(openPrice)
        listofCloses.append(closePrice)
        timeMH.append(data["Date"][i])
        listOfPrices.clear()
        counter += 1

    else:
        counter += 1
        listOfPrices.clear()

baseFigure = go.Figure(data=[go.Candlestick(x=timeMH,
                                            open=listofOpens,
                                            high=listofMaxes,
                                            low=listofMins,
                                            close=listofCloses)])
baseFigure.show()
