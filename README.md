
# Deep Learning for VaR Predictions in the UK Residential Real Estate Market

For my MSc dissertation, I explored if deep learning models could replicate traditional Value-at-Risk (VaR) calculations within the UK property industry. 

Specifically, I used [UK House Price Index data](https://www.gov.uk/government/collections/uk-house-price-index-reports) to calculate VaR using a *traditional* method (Filtered Historical Simulation VaR using GJR-GARCH), with which I then trained Artificial Neural  (ANN), Recurrent Neural Networks (RNN) and an RNN with an LSTM layer. The below shows results of a predicted VaR (95% CI) compared against the traditionally calculated VaR and the actual returns, indicating breaches of the VaR for both actual and predicted.

<h4 align="center">
VaR Backtest Plot for Average English Properties (Actual v ANN Predictions)
</h4>

![example_VaR](https://github.com/joemarron/real-estate-risk-forecasting/blob/main/plots/average_England_ANN_var_prediction_backtest.png)

## Exploratory Data Analysis

![price_hist](https://github.com/joemarron/real-estate-risk-forecasting/blob/main/plots/average_detached_lineplot.png)
![price_hist](https://github.com/joemarron/real-estate-risk-forecasting/blob/main/plots/average_returns.png)

## Results Summary



