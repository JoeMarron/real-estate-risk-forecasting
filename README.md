
# Enhancing Estimations of Future Risk for UK REITs using Deep Learning

***Work in Progress*** \
For my MSc dissertation, I am exploring if deep learning models can improve accuracy of traditional Value-at-Risk (VaR) calculations within the UK property industry. 

Specifically, I will be using share price data for several UK REITs to calculate VaR using a *traditional* method (Filtered Historical Simulation VaR using GJR-GARCH). I will train a Deep Feed-Forward Neural Network (DFFNN) on thousands of traditionally calculated VaR figures for different time windows/confidence interval combinations, combined with returns data for different data sources that can have an effect on the property industry (GDP, Inflation, House Price Index, etc.).

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


![example_VaR](https://github.com/joemarron/real-estate-risk-forecasting/blob/main/Example_GJR_Garch_FHS_VaR.png)

## Continued Work
After implemntation of a deep learning model and upon completion of my dissertation, I will update this README with a summary of my findings.



