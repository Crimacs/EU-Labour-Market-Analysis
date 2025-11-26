import numpy as np 
import pandas as pd

# Caricamento del dataset
df = pd.read_csv('distribuzioni_medie_per_paese.csv')
# Visualizzazione e descrizione del dataset
print(df.head())
print(df.info())
print(df.describe())
#Verificare valori unici
for column in df.columns:
    print(f'Colonna: {column}, Valori unici: {df[column].nunique()}')
# Creare un nuovo dataset con le colonne che ci interessano
df_distribuzione = df[['geo', 'TIME_PERIOD', 'OBS_VALUE']]
#Rinominare le colonne per una migliore comprensione
df_distribuzione.columns = ['Nazione', 'anno', 'valore']
# Visualizzare le righe e la descerizione del nuovo dataset
print(df_distribuzione.head())
print(df_distribuzione.info())
print(df_distribuzione.describe())
#Verificare la presenza di valori nulli
print(df_distribuzione.isnull().sum())
#Rimuovere duplicati
df_distribuzione = df_distribuzione.drop_duplicates()
#Salvare il nuovo dataset in un file CSV
df_distribuzione.to_csv('analisi_distribuzione_paesi.csv', index=False)