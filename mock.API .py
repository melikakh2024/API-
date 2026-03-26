#%%LIBRARIES
import pandas  as pd
import json


#%%READING MOCK API AND FLATTEN
file_path = r"E:\MINI PROJECTS\API\mock.json.txt"
with open(file_path, "r") as f:
    data = json.load(f)
df_projects = pd.json_normalize(
    data,
    record_path=["users","projects"],
    meta=[["users","id"],["users","name"] ,"company", "industry"],
    errors="ignore",
    sep="."
)
df_projects=df_projects.explode(["tags"])
df_address = pd.json_normalize(
    data,
    record_path=["users","address","history"],
    meta=[["users","address","geo","lat"], ["users","address","geo","lng"],["users","address","city"] ,"company", "industry",["users","name"] ,["users","id"]],
    errors="ignore",
    sep="."
)
print(df_address.shape)
print(df_projects.shape)
df_final=df_projects.merge(df_address,how="inner",on=["company","industry"])
print(df_final.shape)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
print(df_final.head(5))
#%%SQL CONNECT
import sqlalchemy

engine=sqlalchemy.create_engine("postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/my_db")
df_final.to_sql("mockAPI" , con=engine,schema="public",if_exists="replace")

