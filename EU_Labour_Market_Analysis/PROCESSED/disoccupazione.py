import numpy as np
import pandas as pd

# Carica i dati da un file CSV
df_disoccupazione = pd.read_csv('disoccupazione.csv')
#Descrizione del dataset
print(df_disoccupazione.describe())
print(df_disoccupazione.info())
# Visualizza le prime righe del dataset
print(df_disoccupazione.head())
#crea un dataset da questo dataframe con le colonne solo interessanti
df_analisi_disoccupazione = df_disoccupazione[['geo', 'age', 'Unit of measure', 'sex', 'TIME_PERIOD', 'OBS_VALUE']]
# Rinomina le colonne per una migliore comprensione
df_analisi_disoccupazione.columns = ['Nazione', 'fascia_eta', 'misura', 'sesso', 'periodo_temporale', 'valore_osservato']
# Visualizza le prime righe del nuovo dataset
print(df_analisi_disoccupazione.head())
#valori unici per ogni colonna
for col in df_analisi_disoccupazione.columns:
    print(f'Valori unici per la colonna {col}: {df_analisi_disoccupazione[col].unique()}')
# pulire i dati rimuovendo righe con valori nulli e duplicati
df_analisi_disoccupazione = df_analisi_disoccupazione.dropna()
df_analisi_disoccupazione = df_analisi_disoccupazione.drop_duplicates()
# Verifica la presenza di valori nulli
print(df_analisi_disoccupazione.isnull().sum())
# Salva il nuovo dataset in un file CSV
df_analisi_disoccupazione.to_csv('analisi_disoccupazione.csv', index=False)
