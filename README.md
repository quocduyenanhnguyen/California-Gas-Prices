# Software I used:
[MySQL Workbench](https://dev.mysql.com/downloads/workbench/): to write SQL 

[PyCharm CE](https://www.jetbrains.com/pycharm/download/?section=windows): to run Python script to scrap gas data

# Description: 

- I explored http://www.californiagasprices.com website to collect and analyze gas data. I came up with questions and then answered them.
- Data will be analyzed from Jun 6, 2024 to Jun 12, 2024. The data from the CSV files are refreshed daily using scheduling tool (i.e. Cron Job)
- Attached to this repository is my SQL queries and output/explanation of output, Python script to scrap data from the website, another Python script to delete any old CSV files that are older than 90 days, and 4 CSV files (Regular Gas, Midgrade Gas, Premium Gas, Diesel Fuel Gas)
- Link to Tableau viz: https://public.tableau.com/app/profile/anna.quoc.nguyen/viz/CaliforniaGasPricesfromJun62024toJun122024/Dashboard1
