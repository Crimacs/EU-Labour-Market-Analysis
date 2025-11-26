import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr , spearmanr

#Caricamento dei dataset
disoccupazione = pd.read_csv('disoccupazione_media.csv')
giovani = pd.read_csv('disoccupazione_giovanile.csv')

#Visualizzazione dei dataset
print(disoccupazione.head())
print(giovani.head())
print(disoccupazione.info())
print(giovani.info())
print(disoccupazione.describe())
print(giovani.describe())

#Merge dei dataset
df_disoccupazione = disoccupazione.merge(giovani, on=['nazione', 'anno'], how='inner')
print(df_disoccupazione.head())
#Correlazione globale
x = df_disoccupazione['tasso_disoccupazione_medio']
y = df_disoccupazione['tasso_disoccupazione_giovanile']
pearson_corr, pearson_p = pearsonr(x, y)
spearman_corr, spearman_p = spearmanr(x, y)
print(f"Correlazione di Pearson: {pearson_corr}, p-value: {pearson_p}")
print(f"Correlazione di Spearman: {spearman_corr}, p-value: {spearman_p}")
#Scatter plot più linea di regressione
plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.5)
m, q = np.polyfit(x, y, 1)
plt.plot(x, m*x + q, color='red')
plt.xlabel('Tasso di Disoccupazione Medio')
plt.ylabel('Tasso di Disoccupazione Giovanile')
plt.title('Correlazione tra Disoccupazione Media e Giovanile')
plt.tight_layout()
plt.show()

#Caricare dataset stipendi
stipendi = pd.read_csv('stipendio_medio.csv')
print(stipendi.head())
print(stipendi.info())
#Visualizzare i valori unici nella colonna 'anno'
print(stipendi['anno'].unique())

#Merge stipendi con disoccupazione media negli anni corrispondenti
df_stipendi_disoccupazione = stipendi.merge(disoccupazione, on=['nazione', 'anno'], how='inner')
print(df_stipendi_disoccupazione.head())
#Correlazione tra stipendio medio e tasso di disoccupazione medio
x_stipendi = df_stipendi_disoccupazione['stipendio_medio_annuo']
y_disoccupazione = df_stipendi_disoccupazione['tasso_disoccupazione_medio']
pearson_corr_stipendi, pearson_p_stipendi = pearsonr(x_stipendi, y_disoccupazione)
spearman_corr_stipendi, spearman_p_stipendi = spearmanr(x_stipendi, y_disoccupazione)
print(f"Correlazione di Pearson (Stipendi vs Disoccupazione): {pearson_corr_stipendi}, p-value: {pearson_p_stipendi}")
print(f"Correlazione di Spearman (Stipendi vs Disoccupazione): {spearman_corr_stipendi}, p-value: {spearman_p_stipendi}")
#Scatter plot più linea di regressione per stipendi e disoccupazione
plt.figure(figsize=(10, 6))
plt.scatter(x_stipendi, y_disoccupazione, alpha=0.5)
m_stipendi, q_stipendi = np.polyfit(x_stipendi, y_disoccupazione, 1)
plt.plot(x_stipendi, m_stipendi*x_stipendi + q_stipendi, color='red')
plt.xlabel('Stipendio Medio Annuo')
plt.ylabel('Tasso di Disoccupazione Medio')
plt.title('Correlazione tra Stipendio Medio e Disoccupazione Media')
plt.tight_layout()
plt.show()

#Forecasting semplice del tasso di disoccupazione medio in Italia
from statsmodels.tsa.arima.model import ARIMA
it= disoccupazione[disoccupazione['nazione']=='IT'].copy()
it= it.sort_values('anno')
it_series = it.set_index('anno')['tasso_disoccupazione_medio']
#Plot della serie temporale
plt.figure(figsize=(10, 6))
plt.plot(it_series.index, it_series.values, marker="o")
plt.title("Tasso di disoccupazione Italia (storico)")
plt.ylabel("%")
plt.xlabel("Anno")
plt.grid(True)
plt.show()

#Modello ARIMA
model = ARIMA(it_series, order=(1, 1, 1))
model_fit = model.fit()
print(model_fit.summary())

#Previsioni future
n_forecast = 3
forecast = model_fit.forecast(steps=n_forecast)
last_year = it_series.index.max()
future_years = np.arange(last_year + 1, last_year + 1 + n_forecast)

forecast_series = pd.Series(forecast.values, index=future_years)

#Plot delle previsioni
plt.figure(figsize=(7,4))
plt.plot(it_series.index, it_series.values, marker="o", label="Storico")
plt.plot(forecast_series.index, forecast_series.values, marker="x", linestyle="--", label="Previsione")
plt.title("Forecast disoccupazione Italia (ARIMA)")
plt.xlabel("Anno")
plt.ylabel("%")
plt.grid(True)
plt.legend()
plt.show()

