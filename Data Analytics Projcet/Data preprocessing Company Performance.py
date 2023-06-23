import pandas as pd
import numpy as np
#MarketCap Data
data_marketcap=pd.read_csv("best_marketcap_companies.csv")
data_marketcap=data_marketcap[:7501]
data_marketcap["Market Cap"]=data_marketcap["Market Cap"].astype(float)
data_marketcap["Multiplicative"]=data_marketcap["Multiplicative"].astype(float)
data_marketcap["Share Price"]=data_marketcap["Share Price"].str.replace(",","")
data_marketcap["Share Price"]=data_marketcap["Share Price"].astype(float)
data_marketcap["Market Cap"]=data_marketcap["Market Cap"]*data_marketcap["Multiplicative"]
data_marketcap=data_marketcap.drop(columns="Multiplicative")

#Profit Data
data_profit=pd.read_csv("best_profitable_companies.csv")
data_profit=data_profit[:5101]
data_profit["Earnings"]=data_profit["Earnings"].astype(float)
data_profit["Multiplicative"]=data_profit["Multiplicative"].astype(float)
data_profit["Earnings"]=data_profit["Earnings"]*data_profit["Multiplicative"]
data_profit=data_profit.drop(columns="Multiplicative")

#Revenue Data
data_revenue=pd.read_csv("best_revenue_companies.csv")
data_revenue=data_revenue[:7001]
data_revenue["Revenue"]=data_revenue["Revenue"].astype(float)
data_revenue["Multiplicative"]=data_revenue["Multiplicative"].astype(float)
data_revenue["Revenue"]=data_revenue["Revenue"]*data_revenue["Multiplicative"]
data_revenue=data_revenue.drop(columns="Multiplicative")

#Merged Data
merged_data = pd.merge(data_profit,data_marketcap, on="Name")
merged_data = pd.merge(merged_data, data_revenue, on="Name")
merged_data=merged_data.drop(columns=["Share Price_x","Country_x","Share Price_y","Country_y"])
merged_data=merged_data.drop_duplicates(subset="Name")
print(merged_data.to_csv("Company Performance.csv",index=False)) 