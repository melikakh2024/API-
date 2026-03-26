import requests
import json
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

response=requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/tickers')
data=response.json()
print(type(data))
#it=iter(data.items())
#print(next(it))
#print(next(it))
#print(data["tickers"][1]["market"])
#print(data["tickers"][3]["market"])

df = pd.json_normalize(data["tickers"], sep=",")
df["name"] = data["name"]
print(df.head())

engine=create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/my_db')
df.to_sql('bitcoin', con=engine)