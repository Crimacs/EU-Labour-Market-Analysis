import numpy as np
import pandas as pd

#Caricare il dataset
df = pd.read_csv('distribuzione_per_settore.csv')
#visualizzare righe e descrizione del dataset
print(df.head())
print(df.info())
print(df.describe())
#Visualizzare i valori unici
for col in df.columns:
    print(f"Colonna: {col}")
    print(df[col].unique())
    print("---")

#Creare un nuovo dataset con le colonne di interesse
df_settori = df[['geo', 'Statistical classification of economic activities in the European Community (NACE Rev. 2)', 'Unit of measure', 'TIME_PERIOD', 'National accounts indicator (ESA 2010)', 'OBS_VALUE']]
#Rinominare le colonne per maggiore chiarezza
df_settori.columns = ['nazione', 'classificazione_settore', 'misura', 'anno', 'national_indicator', 'valore']
#Visualizzare le prime righe e le informazioni del nuovo dataset
print(df_settori.head())
print(df_settori.info())
print(df_settori.describe())
#Verificare la presenza di valori nulli
print(df_settori.isnull().sum())
#Rimuovere eventuali righe con valori nulli e duplicati
df_settori = df_settori.dropna()
df_settori = df_settori.drop_duplicates()
#rimuovere le doppie virgolette dalla colonna classificazione_settore
df_settori['classificazione_settore'] = df_settori['classificazione_settore'].str.replace('"', '')
#Salvare il nuovo dataset in un file CSV
df_settori.to_csv('analisi_settori_pulito.csv', index=False)
