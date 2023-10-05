
# Deep Learning for VaR Predictions in the UK Residential Real Estate Market

For my MSc dissertation, I explored if deep learning models could replicate traditional Value-at-Risk (VaR) calculations within the UK property industry. 

Specifically, I used [UK House Price Index data](https://www.gov.uk/government/collections/uk-house-price-index-reports) to calculate VaR using a *traditional* method (Filtered Historical Simulation VaR using GJR-GARCH), with which I then trained Artificial Neural  (ANN), Recurrent Neural Networks (RNN) and an RNN with an LSTM layer. The below shows results of a predicted VaR (95% CI) compared against the traditionally calculated VaR and the actual returns, indicating breaches of the VaR for both actual and predicted.

<h4 align="center">
VaR Backtest Plot for Average English Properties (Actual v Predictions)
</h4>
![example_VaR](https://github.com/joemarron/real-estate-risk-forecasting/blob/main/average_England_ANN_var_prediction_backtest.png)

I will then assess how the model performs, after hyperparameter optimisation, and compare to traditional methods.

## Initial Exploration
Below shows the first results of VaR forecasting using the GJR-GARCH FHS VaR model, coded using Python, for Harworth Group PLC, a northern based UK REIT. The below code shows part of the function written to acheive the VaR calculations so far.

```
def gjr_garch_var(p=1, o=1, q=1, prices=None, first_obs = None,
                  last_obs=None, start_forecast=None, horizon=1,
                  single_var=False, verbose=False):
    
    prices = prices[first_obs:]
    returns = prices.pct_change().dropna()*100


    model = arch_model(returns, p=p, o=o, q=q)
    result = model.fit(last_obs=last_obs, update_freq=5, disp='off')
    if verbose == True:
        print(result.summary())
    
    forecasts = result.forecast(start=start_forecast, horizon=horizon, reindex=False)
    conditional_mean = pd.DataFrame(forecasts.mean[start_forecast:]['h.%s' % horizon])
    conditional_var = pd.DataFrame(forecasts.variance[start_forecast:]['h.%s' % horizon])
    std_returns = (returns[first_obs:start_forecast] - result.params["mu"]) / result.conditional_volatility
    std_returns = std_returns.dropna()
    q = std_returns.quantile([0.01, 0.05])
    
    
    VaR = conditional_mean.values - np.sqrt(conditional_var).values * q.values[None, :]
    df = pd.DataFrame(VaR, columns=["VaR(99%)", "VaR(95%)"], index=conditional_var.index)

    ...
```

The below back-testing plot shows that the VaR calculated using stock data for HWG.L from 2016 to 2020 forecasts the 95% and 99% VaR relatively well for 2021/22 with a 95% breach of 1.79% and no breaches of the 99% CI. 

## TBC
After implementation of a deep learning model and upon completion of my dissertation, I will update this README with a summary of my findings.



