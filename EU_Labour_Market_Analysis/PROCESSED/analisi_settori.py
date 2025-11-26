import pandas as pd

df = pd.read_csv("analisi_settori.csv")

# circa 150 MB = 1.2M righe → creiamo chunk da 400k righe
chunk_size = 400_000

for i, start in enumerate(range(0, len(df), chunk_size), start=1):
    df[start:start+chunk_size].to_csv(f"analisi_settori_part{i}.csv", index=False)

print("Creati i file analisi_settori_part1.csv, part2, part3")