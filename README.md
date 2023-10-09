
# Deep Learning for VaR Predictions in the UK Residential Real Estate Market

For my MSc dissertation, I explored if deep learning models could replicate traditional Value-at-Risk (VaR) calculations within the UK property industry. 

Specifically, I used [UK House Price Index data](https://www.gov.uk/government/collections/uk-house-price-index-reports) to calculate VaR using a *traditional* method (Filtered Historical Simulation VaR using GJR-GARCH), with which I then trained Artificial Neural  (ANN), Recurrent Neural Networks (RNN) and an RNN with an LSTM layer. The below shows results of a predicted VaR (95% CI) compared against the traditionally calculated VaR and the actual returns, indicating breaches of the VaR for both actual and predicted.

<h4 align="center">
VaR Backtest Plot for Average English Properties (Actual v ANN Predictions)
</h4>

![example_VaR](https://github.com/joemarron/real-estate-risk-forecasting/blob/main/plots/average_England_ANN_var_prediction_backtest.png)

## Exploratory Data Analysis

Below shows the general structure of the dataset with the columns we used in this research, with examples from the East Midlands region.

| Date       | RegionName    | AveragePrice | DetachedPrice | SemiDetachedPrice | TerracedPrice | FlatPrice |
| ---------- | ------------- | ------------ | ------------- | ----------------- | ------------- | --------- |
| 01/01/1995 | East Midlands | 45544.52     | 68923.94      | 41227.5           | 32870.49      | 30954.76  |
| 01/02/1995 | East Midlands | 46051.57     | 68634.75      | 42051.34          | 33423.75      | 31600.06  |
| 01/03/1995 | East Midlands | 45383.82     | 67658.6       | 41388.96          | 33005.72      | 30958.9   |

This plot demonstrates the difference in average detached property prices across different regions in the UK. It is clear how the regions have a drastic impact on the prices of properties, with London average prices (green) over double the national average (red).

<h4 align="center">
Average Detached Property Prices Across English Regions
</h4>

![price_hist](https://github.com/joemarron/real-estate-risk-forecasting/blob/main/plots/average_detached_lineplot.png)

For VaR calculations we need the returns from period to period, in this case the return from one month to the next in the HPI. Hence, the below plot shows the returns for each region for the average property type as an example. The differences in the volatility clustering and distributions is clear - for this project scope we used a subset of these regions, namely London, South West, West Midlands and Yorkshire and The Humber as well as the English national averages. This was to represent England fairly both geographically and statistically whilst making the work managable in terms of model training times. The results need to be considered in this context, with possibly improved results when using the full dataset.

<h4 align="center">
Average Property Returns Across English Regions
</h4>

![price_hist](https://github.com/joemarron/real-estate-risk-forecasting/blob/main/plots/average_returns.png)

## Results Summary



