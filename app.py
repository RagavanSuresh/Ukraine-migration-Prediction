import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import Database_Connection

df = pd.DataFrame.from_dict(Database_Connection.cursor)

sns.pairplot(df)

df["Country of asylum"].value_counts()
Y = df["Refugees under UNHCR's mandate"]
X = df["Year"]

plt.plot(X, Y)

df_new = df["Refugees under UNHCR's mandate"].groupby(by=df["Year"]).sum()

df_new = pd.DataFrame({"Year": df_new.index, "Pred": df_new})

df_new.plot()

from statsmodels.graphics.tsaplots import plot_acf

df_new['SMA_10'] = df_new["Pred"].rolling(10, min_periods=1).mean()
df_new['SMA_20'] = df_new["Pred"].rolling(20, min_periods=1).mean()

colors = ['green', 'red', 'orange']
df_new.plot(color=colors, linewidth=3, figsize=(12, 6))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(labels=['Average Refugee', '10-years SMA', '20-years SMA'], fontsize=14)
plt.title('The yearly average refugee', fontsize=20)
plt.xlabel('Year', fontsize=16)
plt.ylabel('No of Refugee', fontsize=16)

df_new['ema_0.1'] = df_new["Pred"].ewm(alpha=0.1, adjust=False).mean()
df_new['ema_0.3'] = df_new["Pred"].ewm(alpha=0.3, adjust=False).mean()

colors = ['green', 'red', 'orange']
df_new[["Year", "ema_0.1", "ema_0.3"]].plot(color=colors, linewidth=3, figsize=(12, 6))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(labels=['Average Refugee', '0.1 EMA', '0.3 EMA'], fontsize=14)
plt.title('The yearly average refugee', fontsize=20)
plt.xlabel('Year', fontsize=16)
plt.ylabel('No of Refugee', fontsize=16)

plot_acf(df_new["Pred"])
plt.show()

from pandas.plotting import lag_plot

lag_plot(df_new["Pred"])
plt.show()

from statsmodels.tsa.ar_model import AutoReg

X = df_new["Pred"]
train, test = X[1:len(X) - 7], X[len(X) - 7:]
# train autoregression
model = AutoReg(train, lags=2)
model_fit = model.fit()
print('Coefficients: %s' % model_fit.params)
# Predictions
predictions = model_fit.predict(start=len(train), end=len(train) + len(test) - 1, dynamic=False)
print(predictions)

# plot results
plt.plot(test)
plt.plot(predictions, color='red')
plt.show()
