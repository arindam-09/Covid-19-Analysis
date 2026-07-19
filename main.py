import pandas as pd
df=pd.read_csv("covid_19_clean_complete.csv")
print(df.head(5))
print(df.describe())
print(df.info())
print(df.isnull().sum())

df['Province/State']=df['Province/State'].fillna(df['Country/Region'])
print(df.isnull().sum())

df.columns=df.columns.str.replace(" ","_")
df.columns=df.columns.str.replace("/","_")
df.columns=df.columns.str.lower()
print(df.columns)

print("duplicate_rows",df.duplicated().sum())

print(df.dtypes)
print(df["date"].head(10))



df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
df["date"] = df["date"].dt.strftime("%d/%m/%Y")
print(df["date"].tail())

# calculate negative value 
print((df[["confirmed","deaths","recovered","active"]]<0).sum())
print(df[df["active"] < 0])

df["active"] = df["confirmed"] - df["deaths"] - df["recovered"]
print((df[["confirmed","deaths","recovered","active"]]<0).sum())

# handle negative value with 0

df["active"] = df["active"].clip(lower=0)
print((df[["confirmed", "deaths", "recovered", "active"]] < 0).sum())


print(df["country_region"].nunique())
print(df['who_region'].unique())

# # # connet to my sql__________
 
# # from sqlalchemy import create_engine
# # from urllib.parse import quote_plus

# # password = quote_plus("")
# # engine = create_engine(f"mysql+mysqlconnector://root:{password}@localhost:3306/covid_19")

# # df.to_sql("covid_19", con=engine, if_exists="replace", index=False)