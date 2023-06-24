# Top-5K-Companies-Performance-VS-Country-s-Economic-Performance
## Problem Statement
The objective of this project was to gather useful information about the top 5000 companies from the [website](https://companiesmarketcap.com/). We scraped the data and compared their performances based on their national economic indicators extracted from the [world bank archive](https://archive.doingbusiness.org/en/data/exploretopics/starting-a-business). From the datasets, we tried to understand-
1. Which companies are performing best?
2. Which countries have the highest number of companies and how much they are contributing to the economy?
3. The correlation both within and among the Business and Economic indicators
4. Is there any specific patterns to develop a predictive model based on that?
## Methodology
The scraped and archived data were analyzed using Tableau Public. Various charts have been developed to understand the data structure and identify any patterns. Bar charts, map charts, scatter plots, and line, bubble, and honeycomb charts were developed to see if any correlations and trends were present among the samples. The public dashboards are [here](https://public.tableau.com/app/profile/ragib.hasan/viz/DataAnalysisProject_16873100451240/CorrelationbetweenBusinessPerformanceIndicatorsandEconomicIndicators?publish=yes). for reference. 
## Findings from the [Dashboard]
1. The top 10 companies represent 53% of the overall market cap.
2. The United state has the highest no. of companies (around 40%) among the top 5K companies around the world, therefore it is the highest-grossing economy.
3. There is a slightly positive correlation among the business performance indicators. However, the indicators have less effect on the share prices of the companies
4. The economic indicators do not directly affect the companies' performance in the global market other macro conditions may be responsible and need further investigation.
5. There is little correlation between the country's economic conditions and the country's performance in doing business around the world. However, the correlation is not conclusive and requires further investigations with more companies or other indicators.
## Build from Sources
1. Clone the repo
```bash
git clone https://github.com/RHasan97/Top-5K-Companies-Performance-VS-Country-s-Economic-Performance.git
```
2. Installing and activating the virtual environment
```bash
virtualenv --no-site-packages  venv
source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Download Chrome WebDrive from https://chromedriver.chromium.org/downloads
<<<<<<< HEAD
5. Get the data using scrappers and from archives
=======
5. Get the data using scrappers and from archives.  
>>>>>>> c2b911af509d41ebfe43ca64133ea5bb3200981d
