# ml-stock-market-predict
1. **File - 20170130StockMarketPredict.py** 
A simple Stock Market Prediction example which uses Python 3.5, and a SciKit Learn
This project reads one-year historical data of the ticker 'GE' ( obtained from Google Finance ), and then fits a linear regression model to it, and also a RBF regression model to it. We then plot a graph of the underlying data set, as well as the generated linear and RBF regression models. Once these models have been trained,  they could be used to predict a value for the future.  
This project was meant as a simple getting introduction to doing ML in Python, and therefore can be improved in a number of ways, for example by incorporating other features ( other than historical price trends ). Another improvement, could be to improve the size of the current data set on which the model(s) were trained, and also to compare and contrast, on an on-going basis, the relative accuracy of the linear model with the RBF model in predicting future values.  

2. **File - ge.csv** 
The underlying data set used to train the model(s)

3. **File - simply_plot.py** 
A small file created to test the proper working and rendering of some sample data on my Mac, using Matplotlib. 

Credits - This project was inspired by Siraj Raval's wonderful series on Youtube.
