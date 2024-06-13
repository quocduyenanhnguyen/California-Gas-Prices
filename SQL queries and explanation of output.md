#### Data cleaning 
```
with cte as (select Price, substring_index(replace(replace(replace(Station, "('", ' '), "'", ''), ")", ''), ', ', 1) as Gas_Station, 
substring_index(replace(replace(replace(Station, "('", ' '), "'", ''), ")", ''), ', ', -1) as Gas_Station_Address,
Area,
substring_index(replace(replace(replace(Thanks, "('", ' '), "'", ''), ")", ''), ', ', 1) as Thanks_By, 
substring_index(replace(replace(replace(Thanks, "('", ' '), "'", ''), ")", ''), ', ', -1) as thanks_last_updated,
last_updated_price
from Regular_Gas),
cte1 as (
select Price, substring_index(replace(replace(replace(Station, "('", ' '), "'", ''), ")", ''), ', ', 1) as Gas_Station, 
substring_index(replace(replace(replace(Station, "('", ' '), "'", ''), ")", ''), ', ', -1) as Gas_Station_Address,
Area,
substring_index(replace(replace(replace(Thanks, "('", ' '), "'", ''), ")", ''), ', ', 1) as Thanks_By, 
substring_index(replace(replace(replace(Thanks, "('", ' '), "'", ''), ")", ''), ', ', -1) as thanks_last_updated,
last_updated_price
from midgrade_Gas),
cte2 as (
select Price, substring_index(replace(replace(replace(Station, "('", ' '), "'", ''), ")", ''), ', ', 1) as Gas_Station, 
substring_index(replace(replace(replace(Station, "('", ' '), "'", ''), ")", ''), ', ', -1) as Gas_Station_Address,
Area,
substring_index(replace(replace(replace(Thanks, "('", ' '), "'", ''), ")", ''), ', ', 1) as Thanks_By, 
substring_index(replace(replace(replace(Thanks, "('", ' '), "'", ''), ")", ''), ', ', -1) as thanks_last_updated,
last_updated_price
from premium_Gas),
cte3 as (
select Price, substring_index(replace(replace(replace(Station, "('", ' '), "'", ''), ")", ''), ', ', 1) as Gas_Station, 
substring_index(replace(replace(replace(Station, "('", ' '), "'", ''), ")", ''), ', ', -1) as Gas_Station_Address,
Area,
substring_index(replace(replace(replace(Thanks, "('", ' '), "'", ''), ")", ''), ', ', 1) as Thanks_By, 
substring_index(replace(replace(replace(Thanks, "('", ' '), "'", ''), ")", ''), ', ', -1) as thanks_last_updated,
last_updated_price
from diesel_fuel_Gas)
select distinct cte.Price as regular_price, cte1.price as midgrade_price, cte2.price as premium_price, cte3.price as diesel_fuel_price,
cte.gas_station, cte.gas_station_address, cte.Area, cte.last_updated_price
from cte
join cte1 on cte.gas_station = cte1.gas_station and cte.gas_station_address = cte1.gas_station_address
join cte2 on cte.gas_station = cte2.gas_station and cte.gas_station_address = cte2.gas_station_address
join cte3 on cte.gas_station = cte3.gas_station and cte.gas_station_address = cte3.gas_station_address
order by cte.last_updated_price desc
limit 10
;
```
#### Output
![Screen Shot 2024-06-12 at 9 25 01 PM](https://github.com/quocduyenanhnguyen/California-Gas-Prices/assets/92205707/e228a276-09cc-403f-8005-ba8990d372c1)

-> It looks nicer now, after cleaning the CSV files

# 1. Lowest and highest price in each gas type?
# Regular gas
```
select min(price), max(price) from Regular_Gas;
```
#### Output
![Screen Shot 2024-06-12 at 9 28 03 PM](https://github.com/quocduyenanhnguyen/California-Gas-Prices/assets/92205707/9a3d3f01-25a0-4b2f-8a21-277736bab336)

-> Highest regular gas price is $8.55, lowest is $3.69.

# Midgrade gas
```
select min(price), max(price) from Midgrade_Gas;
```
#### Output
![Screen Shot 2024-06-12 at 9 29 07 PM](https://github.com/quocduyenanhnguyen/California-Gas-Prices/assets/92205707/e284e490-417b-4a57-a15e-9e4e4807ebf8)

-> Highest midgrade gas price is $7.23, lowest is $3.75.

# Premium gas
```
select min(price), max(price) from Premium_Gas;
```
#### Output
![Screen Shot 2024-06-12 at 9 30 08 PM](https://github.com/quocduyenanhnguyen/California-Gas-Prices/assets/92205707/f54c6119-7773-42fd-92f3-2fcdba967f71)

-> Highest premium gas price is $7.39, lowest is $3.85.

# Diesel Fuel gas
```
select min(price), max(price) from Diesel_Fuel_Gas;
```
#### Output
![Screen Shot 2024-06-12 at 9 31 10 PM](https://github.com/quocduyenanhnguyen/California-Gas-Prices/assets/92205707/a28c90fb-4308-460f-9a59-985a21f246de)

-> Highest diesel fuel gas price is $8.55, lowest is $3.79.

# 2. Which gas station has the lowest and highest price in each gas type? (let's look at the first 3)
# Regular gas
```select distinct substring_index(replace(replace(replace(Station, "('", ' '), "'", ''), ")", ''), ', ', 1) as Gas_Station,
min(price), max(price)
from Regular_Gas
group by Gas_Station
limit 3;
```
#### Output
![Screen Shot 2024-06-12 at 9 33 34 PM](https://github.com/quocduyenanhnguyen/California-Gas-Prices/assets/92205707/ce97ebe3-378c-492b-ac42-b13639501a0e)


# Midgrade gas
```select distinct substring_index(replace(replace(replace(Station, "('", ' '), "'", ''), ")", ''), ', ', 1) as Gas_Station,
min(price), max(price)
from Midgrade_gas
group by Gas_Station
limit 3;
```
#### Output
![Screen Shot 2024-06-12 at 9 34 52 PM](https://github.com/quocduyenanhnguyen/California-Gas-Prices/assets/92205707/20bc0f4e-96f4-4237-8368-9e2c3704e9b2)

# Premium gas
```
select distinct substring_index(replace(replace(replace(Station, "('", ' '), "'", ''), ")", ''), ', ', 1) as Gas_Station,
min(price), max(price)
from Premium_gas
group by Gas_Station
limit 3;
```
#### Output
![Screen Shot 2024-06-12 at 9 35 25 PM](https://github.com/quocduyenanhnguyen/California-Gas-Prices/assets/92205707/846a2520-b49c-4252-8a0d-647a46ec4d4b)


# Diesel Fuel gas
```
select distinct substring_index(replace(replace(replace(Station, "('", ' '), "'", ''), ")", ''), ', ', 1) as Gas_Station,
min(price), max(price)
from Diesel_Fuel_gas
group by Gas_Station;
```
#### Output
![Screen Shot 2024-06-12 at 9 35 58 PM](https://github.com/quocduyenanhnguyen/California-Gas-Prices/assets/92205707/864904e1-cf85-4011-8645-0246c705565b)


# 3. Does the price change a lot from Jun 6 to Jun 12 for regular gas?
# price difference
```
with cte as (select date_format(last_updated_price, '%Y/%m/%d %H') as formatted_date, round(avg(price), 2) as average_price, 
lead(round(avg(price), 2)) over(order by date_format(last_updated_price, '%Y/%m/%d %H')) as next_value,
((lead(round(avg(price), 2)) over(order by date_format(last_updated_price, '%Y/%m/%d %H')) - round(avg(price), 2) ) * 100)/round(avg(price), 2) 
as price_difference
from regular_gas
group by formatted_date
order by formatted_date)
select formatted_date, average_price, round(lag(price_difference) over(order by formatted_date), 2) as price_difference
from cte
order by formatted_date 
;
```
#### Output
![Screen Shot 2024-06-12 at 9 37 45 PM](https://github.com/quocduyenanhnguyen/California-Gas-Prices/assets/92205707/aea43776-2453-45a4-afb3-02fe7a01b12a)

-> The price went up and down quite frequently, which see its peak on Jun 9 at 3:00 PM (it went down by 6.5%)

# average price difference 
```
with cte as (select date_format(last_updated_price, '%Y/%m/%d %H') as formatted_date, round(avg(price), 2) as average_price, 
lead(round(avg(price), 2)) over(order by date_format(last_updated_price, '%Y/%m/%d %H')) as next_value,
((lead(round(avg(price), 2)) over(order by date_format(last_updated_price, '%Y/%m/%d %H')) - round(avg(price), 2) ) * 100)/round(avg(price), 2) 
as price_difference
from regular_gas
group by formatted_date
order by formatted_date)
select round(avg(price_difference), 2) as average_price_difference
from cte;
```
#### Output
![Screen Shot 2024-06-12 at 9 44 14 PM](https://github.com/quocduyenanhnguyen/California-Gas-Prices/assets/92205707/4081959a-f447-4c7b-b4fa-da5bf69c5a9d)

-> On average, the price went down by 0.12%.

# 4. Which area has the highest average gas price?
# Regular gas
```
select distinct Area, round(avg(price), 0) as average_price_per_Area from Regular_Gas
group by Area 
order by average_price_per_Area desc
;
```
#### Output
![Screen Shot 2024-06-12 at 9 46 41 PM](https://github.com/quocduyenanhnguyen/California-Gas-Prices/assets/92205707/d138b000-fafe-4c45-a6f2-11b6e9c9e347)

-> Essex has the highest average regular gas price

# Midgrade gas
```
select distinct Area, round(avg(price), 0) as average_price_per_Area from Midgrade_Gas
group by Area 
order by average_price_per_Area desc
;
```
#### Output
![Screen Shot 2024-06-12 at 9 47 43 PM](https://github.com/quocduyenanhnguyen/California-Gas-Prices/assets/92205707/b513a415-d207-4803-94c9-e3917a12a460)

-> Vidal Junction has the highest average midgrade gas price

# Premium gas
```
select distinct Area, round(avg(price), 0) as average_price_per_Area from Premium_Gas
group by Area 
order by average_price_per_Area desc
;
```
#### Output
![Screen Shot 2024-06-12 at 9 48 39 PM](https://github.com/quocduyenanhnguyen/California-Gas-Prices/assets/92205707/59f4c73a-1c50-4eb9-b32e-4b1fddd83163)

-> Ludlow has the highest average premium gas price

# Diesel Fuel gas
```
select distinct Area, round(avg(price), 0) as average_price_per_Area from Diesel_Fuel_Gas
group by Area 
order by average_price_per_Area desc
;
```
#### Output
![Screen Shot 2024-06-12 at 9 49 50 PM](https://github.com/quocduyenanhnguyen/California-Gas-Prices/assets/92205707/d0e0c242-4287-4675-9cd9-23010fe7fab7)

-> Essex has the highest average diesel fuel gas price

# 5. What's the lowest average price per gas brand in the last 12 hours? 
# Regular Gas
```
select substring_index(replace(replace(replace(Station, "('", ' '), "'", ''), ")", ''), ', ', 1) as Gas_Station, round(avg(price), 2) as 
average_price_per_gas_brand
from Regular_Gas
where last_updated_price > now() - interval 12 hour
group by Gas_Station
order by average_price_per_gas_brand 
limit 2
;
```
#### Output
![Screen Shot 2024-06-12 at 9 50 58 PM](https://github.com/quocduyenanhnguyen/California-Gas-Prices/assets/92205707/1cf0da6b-ea6c-4ab4-a2db-192a3662b2ea)

-> Foxxy Gasoline and Diamond Gas & Mart each has the lowest average regular gas

# Midgrade Gas
```
select substring_index(replace(replace(replace(Station, "('", ' '), "'", ''), ")", ''), ', ', 1) as Gas_Station, round(avg(price), 2) as 
average_price_per_gas_brand
from Midgrade_Gas
where last_updated_price > now() - interval 12 hour
group by Gas_Station
order by average_price_per_gas_brand 
limit 1
;
```
#### Output
![Screen Shot 2024-06-12 at 9 52 12 PM](https://github.com/quocduyenanhnguyen/California-Gas-Prices/assets/92205707/c48d2dbc-20ab-4443-ac3f-78c2e48dda88)

-> Fastrip has the lowest average midgrade gas

# Premium Gas
```
select substring_index(replace(replace(replace(Station, "('", ' '), "'", ''), ")", ''), ', ', 1) as Gas_Station, round(avg(price), 2) as 
average_price_per_gas_brand
from Premium_Gas
where last_updated_price > now() - interval 12 hour
group by Gas_Station
order by average_price_per_gas_brand 
limit 1
;
```
#### Output
![Screen Shot 2024-06-12 at 9 53 10 PM](https://github.com/quocduyenanhnguyen/California-Gas-Prices/assets/92205707/38be15eb-7afe-458a-9642-e0c28a526fd4)

-> Fastrip has the lowest average premium gas

# Diesel Fuel Gas
```
select substring_index(replace(replace(replace(Station, "('", ' '), "'", ''), ")", ''), ', ', 1) as Gas_Station, round(avg(price), 2) as 
average_price_per_gas_brand
from Diesel_Fuel_Gas
where last_updated_price > now() - interval 12 hour
group by Gas_Station
order by average_price_per_gas_brand 
limit 1
;
```
#### Output
![Screen Shot 2024-06-12 at 9 53 56 PM](https://github.com/quocduyenanhnguyen/California-Gas-Prices/assets/92205707/4810b77c-1f47-4728-a0da-f9e0a8b99a33)

-> Wintun Mini Market has the lowest average diesel fuel gas

# 6. Which part of California sees the cheapeast average regular gas price, most expensive average regular gas price? Which gas station address sees most regular gas price fluctuation (highest delta), and the most price changes (more changes in price) in the last 12 hours according to this dataset? 
# The cheapest part of California
```
select Area, round(avg(price), 2) as 
average_price_per_gas_brand
from Regular_Gas
where last_updated_price > now() - interval 12 hour
group by Area
order by average_price_per_gas_brand 
limit 1
;
```
#### Output
![Screen Shot 2024-06-12 at 9 56 18 PM](https://github.com/quocduyenanhnguyen/California-Gas-Prices/assets/92205707/60f5d319-5f6b-4a0a-87c7-afb117c6c2b5)

-> Livermore has the cheapest average regular gas price

# The most expensive part
```
select Area, round(avg(price), 2) as 
average_price_per_gas_brand
from Regular_Gas
where last_updated_price > now() - interval 12 hour
group by Area
order by average_price_per_gas_brand desc
limit 1
;
```
#### Output
![Screen Shot 2024-06-12 at 9 58 10 PM](https://github.com/quocduyenanhnguyen/California-Gas-Prices/assets/92205707/c8ddaccb-e335-4860-829f-e09059c771c3)

-> Vidal Junction has the most expensive average regular gas price

# most regular gas price fluctuation (highest delta, if there are multiple deltas per gas station address then we will get the average of the deltas) gas station address in the last 12 hours (zero does not count because it means there's no changes)
```
with cte2 as (with cte1 as (with cte as (select distinct last_updated_price, substring_index(replace(replace(replace(Station, "('", ' '), "'", ''), ")", ''), ', ', 1) as Gas_Station,
substring_index(replace(replace(replace(Station, "('", ' '), "'", ''), ")", ''), ', ', -1) as Gas_Station_Address, price
from regular_gas
where last_updated_price > now() - interval 12 hour
order by gas_station, gas_station_address, last_updated_price)
select *, round(lead(price) over (partition by Gas_Station, Gas_Station_Address order by last_updated_price), 2) as next_value
from cte)
select *, round(next_value-price, 2) as delta from cte1)
select Gas_Station, Gas_Station_Address, avg(delta) as average_delta
from cte2
where delta != 0 and delta != -0
group by Gas_Station, Gas_Station_Address
order by average_delta desc
;
```
#### Output
![Screen Shot 2024-06-12 at 10 00 21 PM](https://github.com/quocduyenanhnguyen/California-Gas-Prices/assets/92205707/ff9ddc0e-8dba-42a7-a0e8-67690305f804)

-> Fastrip on 195 W Hermosa St & N Sweetbriar Ave has the highest delta, it went down by $0.04.

# Gas station address with the most price changes (i.e. number of deltas per Gas Station Address) in the last 12 hours
```
with cte2 as (with cte1 as (with cte as (select distinct last_updated_price, substring_index(replace(replace(replace(Station, "('", ' '), "'", ''), ")", ''), ', ', 1) as Gas_Station,
substring_index(replace(replace(replace(Station, "('", ' '), "'", ''), ")", ''), ', ', -1) as Gas_Station_Address, price
from regular_gas
where last_updated_price > now() - interval 12 hour
order by gas_station, gas_station_address, last_updated_price)
select *, round(lead(price) over (partition by Gas_Station, Gas_Station_Address order by last_updated_price), 2) as next_value
from cte)
select *, round(next_value-price, 2) as delta from cte1)
select Gas_Station, Gas_Station_Address, count(delta) as number_of_deltas
from cte2
where delta != 0 and delta != -0
group by Gas_Station, Gas_Station_Address
order by number_of_deltas desc
;
```
#### Output
![Screen Shot 2024-06-12 at 10 06 35 PM](https://github.com/quocduyenanhnguyen/California-Gas-Prices/assets/92205707/bd5f1266-3459-4785-bef6-92e5951fcf93)

-> In the last 12 hours, only Fastrip on 195 W Hermosa St & N Sweetbriar Ave has one delta.
