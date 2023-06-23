import pandas as pd
import numpy as np
import openpyxl

data_start_business=pd.read_excel("Starting a Business.xlsx")[9:].dropna(axis=1)
data_getting_credit=pd.read_excel("Getting Credit.xlsx")[9:].dropna(axis=1)
data_electricity=pd.read_excel("Getting Electricity.xlsx")[9:].dropna(axis=1)
data_property=pd.read_excel("Registering Property.xlsx")[9:].dropna(axis=1)
data_trading=pd.read_excel("Trading across Borders.xlsx")[9:].dropna(axis=1)
data_insolvency=pd.read_excel("Resolving Insolvency.xlsx")[9:].dropna(axis=1)
data_construction_permits=pd.read_excel("Dealing with Construction Permits.xlsx")[9:].dropna(axis=1)
data_protecting_minority_investors=pd.read_excel("Protecting Minority Investors.xlsx")[9:].dropna(axis=1)
data_paying_taxes=pd.read_excel("Paying Taxes.xlsx")[9:].dropna(axis=1)

Columns= ["Location","Starting a Business score","Getting Credit score","Getting Electricity score","Dealing with Construction Permits score","Registering Property score","Protecting Minority Investors score","Paying Taxes score","Trading across Borders score","Resolving Insolvency score"]

merged=pd.merge(data_start_business,data_getting_credit,"inner",on="Location")
merged=pd.merge(merged,data_electricity,"inner",on="Location")
merged=pd.merge(merged,data_property,"inner",on="Location")
merged=pd.merge(merged,data_trading,"inner",on="Location")
merged=pd.merge(merged,data_insolvency,"inner",on="Location")
merged=pd.merge(merged,data_construction_permits,"inner",on="Location")
merged=pd.merge(merged,data_protecting_minority_investors,"inner",on="Location")
merged=pd.merge(merged,data_paying_taxes,"inner",on="Location")

print(merged[Columns].to_excel("World Bank Business indicators.xlsx",index=False))