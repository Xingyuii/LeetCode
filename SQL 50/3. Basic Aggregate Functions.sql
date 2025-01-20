# 1. - 1757. Recyclable and Low Fat Products
# Write your MySQL query statement below
SELECT product_id FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y'

# 2. -  584. Find Customer Referee
Select  name 
From Customer
Where referee_id != 2 OR referee_id IS NULL

# 3. - 595. Big Countries
# Write your MySQL query statement below
select name, population, area from World
where area>=3000000 or population>=25000000

