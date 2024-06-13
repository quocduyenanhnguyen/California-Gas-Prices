import requests
from bs4 import BeautifulSoup
import pandas as pd

#We can change fuel=A to B, C, D to see price for other type of gas
r = requests.get("http://www.californiagasprices.com/index.aspx?fuel=A")
rB = requests.get("http://www.californiagasprices.com/index.aspx?fuel=B")
rC = requests.get("http://www.californiagasprices.com/index.aspx?fuel=C")
rD = requests.get("http://www.californiagasprices.com/index.aspx?fuel=D")
soup = BeautifulSoup(r.content, "lxml")
soupB = BeautifulSoup(rB.content, "lxml")
soupC = BeautifulSoup(rC.content, "lxml")
soupD = BeautifulSoup(rD.content, "lxml")
table = soup.find("table", class_="p_v2")
table2 = soup.find("table", class_="p_v2 p_v2b")
tableB = soupB.find("table", class_="p_v2")
table2B = soupB.find("table", class_="p_v2 p_v2b")
tableC = soupC.find("table", class_="p_v2")
table2C = soupC.find("table", class_="p_v2 p_v2b")
tableD = soupD.find("table", class_="p_v2")
table2D = soupD.find("table", class_="p_v2 p_v2b")

#Regular Price
header = [th.get_text(strip=True) for th in table.tr.select("th")]
header2 = [th.get_text(strip=True) for th in table2.tr.select("th")]

#Midgrade
headerB = [th.get_text(strip=True) for th in tableB.tr.select("th")]
header2B = [th.get_text(strip=True) for th in table2B.tr.select("th")]

#Premium
headerC = [th.get_text(strip=True) for th in tableC.tr.select("th")]
header2C = [th.get_text(strip=True) for th in table2C.tr.select("th")]

#Diesel Fuel
headerD = [th.get_text(strip=True) for th in tableD.tr.select("th")]
header2D = [th.get_text(strip=True) for th in table2D.tr.select("th")]

all_data = []
all_dataB = []
all_dataC = []
all_dataD = []

for row in table.select("tbody tr:has(th)"):
    price = row.select_one("th div.price_num").text
    address = row.select_one("td dl.address")
    station = (address.dt.text.strip(), address.dd.text)
    area = row.select_one("td a.p_area").text
    thanks_by = row.select_one("td a.mem").text
    last_updated_thanks = row.select_one("td div.tm").text
    thanks = (thanks_by, last_updated_thanks)
    all_data.append([price, station, area, thanks])

for row in table2.select("tbody tr:has(th)"):
    price = row.select_one("th div.price_num").text
    address = row.select_one("td dl.address")
    station = (address.dt.text.strip(), address.dd.text)
    area = row.select_one("td a.p_area").text
    thanks_by = row.select_one("td a.mem").text
    last_updated_thanks = row.select_one("td div.tm").text
    thanks = (thanks_by, last_updated_thanks)
    all_data.append([price, station, area, thanks])

for row in tableB.select("tbody tr:has(th)"):
    price = row.select_one("th div.price_num").text
    address = row.select_one("td dl.address")
    station = (address.dt.text.strip(), address.dd.text)
    area = row.select_one("td a.p_area").text
    thanks_by = row.select_one("td a.mem").text
    last_updated_thanks = row.select_one("td div.tm").text
    thanks = (thanks_by, last_updated_thanks)
    all_dataB.append([price, station, area, thanks])

for row in table2B.select("tbody tr:has(th)"):
    price = row.select_one("th div.price_num").text
    address = row.select_one("td dl.address")
    station = (address.dt.text.strip(), address.dd.text)
    area = row.select_one("td a.p_area").text
    thanks_by = row.select_one("td a.mem").text
    last_updated_thanks = row.select_one("td div.tm").text
    thanks = (thanks_by, last_updated_thanks)
    all_dataB.append([price, station, area, thanks])

for row in tableC.select("tbody tr:has(th)"):
    price = row.select_one("th div.price_num").text
    address = row.select_one("td dl.address")
    station = (address.dt.text.strip(), address.dd.text)
    area = row.select_one("td a.p_area").text
    thanks_by = row.select_one("td a.mem").text
    last_updated_thanks = row.select_one("td div.tm").text
    thanks = (thanks_by, last_updated_thanks)
    all_dataC.append([price, station, area, thanks])

for row in table2C.select("tbody tr:has(th)"):
    price = row.select_one("th div.price_num").text
    address = row.select_one("td dl.address")
    station = (address.dt.text.strip(), address.dd.text)
    area = row.select_one("td a.p_area").text
    thanks_by = row.select_one("td a.mem").text
    last_updated_thanks = row.select_one("td div.tm").text
    thanks = (thanks_by, last_updated_thanks)
    all_dataC.append([price, station, area, thanks])

for row in tableD.select("tbody tr:has(th)"):
    price = row.select_one("th div.price_num").text
    address = row.select_one("td dl.address")
    station = (address.dt.text.strip(), address.dd.text)
    area = row.select_one("td a.p_area").text
    thanks_by = row.select_one("td a.mem").text
    last_updated_thanks = row.select_one("td div.tm").text
    thanks = (thanks_by, last_updated_thanks)
    all_dataD.append([price, station, area, thanks])

for row in table2D.select("tbody tr:has(th)"):
    price = row.select_one("th div.price_num").text
    address = row.select_one("td dl.address")
    station = (address.dt.text.strip(), address.dd.text)
    area = row.select_one("td a.p_area").text
    thanks_by = row.select_one("td a.mem").text
    last_updated_thanks = row.select_one("td div.tm").text
    thanks = (thanks_by, last_updated_thanks)
    all_dataD.append([price, station, area, thanks])


df = pd.DataFrame(all_data, columns=header)
df.insert(0, 'last_updated_price', pd.to_datetime('now').replace(microsecond=0))
#print(df)

dfB = pd.DataFrame(all_dataB, columns=header)
dfB.insert(0, 'last_updated_price', pd.to_datetime('now').replace(microsecond=0))
#print(dfB)

dfC = pd.DataFrame(all_dataC, columns=header)
dfC.insert(0, 'last_updated_price', pd.to_datetime('now').replace(microsecond=0))
#print(dfC)

dfD = pd.DataFrame(all_dataD, columns=header)
dfD.insert(0, 'last_updated_price', pd.to_datetime('now').replace(microsecond=0))
#print(dfD)
#print(dfD.dtypes)

df.to_csv("/Users/annanguyen/Documents/Anna_Projects/Web_Scraping_Python_projects/Regular_Gas.csv", mode='a', index=False)
dfB.to_csv("/Users/annanguyen/Documents/Anna_Projects/Web_Scraping_Python_projects/Midgrade_Gas.csv", mode='a', index=False)
dfC.to_csv("/Users/annanguyen/Documents/Anna_Projects/Web_Scraping_Python_projects/Premium_Gas.csv", mode='a', index=False)
dfD.to_csv("/Users/annanguyen/Documents/Anna_Projects/Web_Scraping_Python_projects/Diesel_Fuel_Gas.csv", mode='a', index=False)





