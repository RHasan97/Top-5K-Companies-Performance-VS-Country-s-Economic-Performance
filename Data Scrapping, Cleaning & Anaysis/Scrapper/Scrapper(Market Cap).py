from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np

columns = ["Name", "Market Cap", "Multiplicative", "Share Price", "Country"]


def Compnay_details(row):
    information = row.text.split('\n')
    cn ={}
    cn["Name"] = information[1]
    cn["Market Cap"] = information[3].split()[0]
    cn["Multiplicative"]=information[3].split()[1]
    cn["Share Price"] = information[3].split()[2]
    cn["Country"] =' '.join(information[3].split()[4:])
    return cn


def main():
    Company_data=[]
    for page_id in range(1,77):
        url = f"https://companiesmarketcap.com/?page={page_id}"
        driver = webdriver.Chrome()
        driver.get(url)
        rankings = driver.find_element(By.CSS_SELECTOR, '#cmkt > div.table-container.shadow > table')
        rows = rankings.find_elements(By.CSS_SELECTOR, '#cmkt > div.table-container.shadow > table > tbody > tr')
        for idx, row in enumerate(rows):
            Company_data.append(Compnay_details(row))
        driver.close()

    df = pd.DataFrame(data=Company_data, columns=columns)
    print(df.info())

    for i in range (len(df["Multiplicative"])):
        if df["Multiplicative"][i]=="T":
            df["Multiplicative"][i] = int(10**12)
        elif df["Multiplicative"][i]=="B":
            df["Multiplicative"][i] = int(10**9)
        elif df["Multiplicative"][i]=="M":
            df["Multiplicative"][i] = int(10**6)

    df["Market Cap"] = df["Market Cap"].str.replace("$", "")
    df["Share Price"] = df["Share Price"].str.replace("$", "")
    
    df.to_csv("best_marketcap_companies.csv", index=False)
    return

if __name__ == "__main__":
    main()