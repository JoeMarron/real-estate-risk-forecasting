
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

![ret_hist](https://github.com/joemarron/real-estate-risk-forecasting/blob/main/plots/average_returns.png)

## Modelling
To optimise the models for each region/property Type combination, we carried out a random search cross-validation process, optimising for the below hyperparameters.
| Hyperparameter       | Values           |
| -------------------- | ---------------- |
| Hidden nodes         | [32, 64, 128]    |
| Learning rate        | [0.01, 0.001]    |
| No. of hidden layers | [3, 4]           |
| Drop out rate        | [0.05, 0.1, 0.2] |

The epochs remained the same for each at 200, however early stopping was implemented as to reduce the computation time where possible, which can be seen in the below plot which only reached 124 epochs before the loss converged on an approximate optimum. The scaling of the data was also done within the ML modelling pipeline, using StandardScaler which transforms the data to have amean of 0 and a standard deviation of 1.

<h4 align="center">
Average English Property ANN Optimal Model Loss Plot (MAE, MSE, RMSE)
</h4>

![loss_plot](https://github.com/joemarron/real-estate-risk-forecasting/blob/main/plots/average_England_ANN_optimal_model_loss_plt.png)

## Results Summary
The results of the modelling demonstrated varying results across each region and property type. The best RMSE acheived for each of these models can be seen in the table below. The closest replication of the VaR calculation achieved was for the average property type in London with an RMSE of 0.277. London in general provided the closest predictions to the VaR actual calculations with a mean RMSE of 0.3381. 

| region                   | average | detached | flat   | semi_detached | terraced |
| ------------------------ | ------- | -------- | ------ | ------------- | -------- |
| England                  | 0.3273  | 0.3700   | 0.5400 | 0.4043        | 0.4350   |
| London                   | 0.2770  | 0.3973   | 0.3680 | 0.2977        | 0.3503   |
| South West               | 0.4693  | 0.4833   | 0.4653 | 0.4150        | 0.3650   |
| West Midlands            | 0.8390  | 0.4957   | 0.4860 | 0.7590        | 0.6337   |
| Yorkshire and The Humber | 0.4313  | 0.3943   | 0.5493 | 0.4933        | 0.4113   |



