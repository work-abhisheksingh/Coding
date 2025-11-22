import numpy as np

def holt_linear(y, alpha, beta, forecast_steps):
    n = len(y)
    level = np.zeros(n)
    trend = np.zeros(n)
    forecast = np.zeros(n + forecast_steps)
    
    # Initialization
    level[0] = y[0]
    trend[0] = y[1] - y[0]  # initial slope
    
    forecast[0] = y[0]
    
    # Updating level and trend
    for t in range(1, n):
        level[t] = alpha * y[t] + (1 - alpha) * (level[t-1] + trend[t-1])
        trend[t] = beta * (level[t] - level[t-1]) + (1 - beta) * trend[t-1]
        forecast[t] = level[t] + trend[t]
    
    # Forecasting future values
    for h in range(1, forecast_steps + 1):
        forecast[n + h - 1] = level[-1] + h * trend[-1]
    
    return forecast

# Example data
sales = np.array([50, 55, 60, 66, 72, 78])

# Parameters
alpha = 0.8  # level smoothing
beta = 0.2   # trend smoothing
forecast_steps = 5

predictions = holt_linear(sales, alpha, beta, forecast_steps)
print("Forecast:", predictions)
