-------- Basic Joins -------- EASY -------- 
# 1378. Replace Employee ID With The Unique Identifier
# Write your MySQL query statement below
Select unique_id, name
FROM Employees
LEFT JOIN EmployeeUNI
ON Employees.id = EmployeeUNI.id;

# 1068. Product Sales Analysis I
-- Table: Sales

-- +-------------+-------+
-- | Column Name | Type  |
-- +-------------+-------+
-- | sale_id     | int   |
-- | product_id  | int   |
-- | year        | int   |
-- | quantity    | int   |
-- | price       | int   |
-- +-------------+-------+
-- (sale_id, year) is the primary key (combination of columns with unique values) of this table.
-- product_id is a foreign key (reference column) to Product table.
-- Each row of this table shows a sale on the product product_id in a certain year.
-- Note that the price is per unit.
 

-- Table: Product

-- +--------------+---------+
-- | Column Name  | Type    |
-- +--------------+---------+
-- | product_id   | int     |
-- | product_name | varchar |
-- +--------------+---------+
-- Write a solution to report the product_name, year, and price for each sale_id in the Sales table.

Select product_name, year, price FROM Sales
left join Product
on Product.product_id = Sales.product_id

# 1581. Customer Who Visited but Did Not Make Any Transactions
-- Table: Visits

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | visit_id    | int     |
-- | customer_id | int     |
-- +-------------+---------+
-- visit_id is the column with unique values for this table.
-- This table contains information about the customers who visited the mall.
 

-- Table: Transactions

-- +----------------+---------+
-- | Column Name    | Type    |
-- +----------------+---------+
-- | transaction_id | int     |
-- | visit_id       | int     |
-- | amount         | int     |
-- +----------------+---------+
-- transaction_id is column with unique values for this table.
-- This table contains information about the transactions made during the visit_id.
 

-- Write a solution to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.


SELECT Visits.customer_id, count(Visits.visit_id) as count_no_trans from Visits
left join Transactions
on Visits.visit_id = Transactions.visit_id
where  Transactions.transaction_id is null
GROUP BY Visits.customer_id

# 197. Rising Temperature
-- Table: Weather

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | recordDate    | date    |
-- | temperature   | int     |
-- +---------------+---------+
-- id is the column with unique values for this table.
-- There are no different rows with the same recordDate.
-- This table contains information about the temperature on a certain day.
 

-- Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).

-- Return the result table in any order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Weather table:
-- +----+------------+-------------+
-- | id | recordDate | temperature |
-- +----+------------+-------------+
-- | 1  | 2015-01-01 | 10          |
-- | 2  | 2015-01-02 | 25          |
-- | 3  | 2015-01-03 | 20          |
-- | 4  | 2015-01-04 | 30          |
-- +----+------------+-------------+
-- Output: 
-- +----+
-- | id |
-- +----+
-- | 2  |
-- | 4  |
-- +----+
-- Explanation: 
-- In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
-- In 2015-01-04, the temperature was higher than the previous day (20 -> 30).
SELECT w1.id
FROM Weather w1
JOIN Weather w2
  ON DATE_ADD(w2.recordDate, INTERVAL 1 DAY) = w1.recordDate # add查找明天的日期
WHERE w1.temperature > w2.temperature;


# 1661. Average Time of Process per Machine
select a1.machine_id, round(avg(a2.timestamp-a1.timestamp), 3) as processing_time 
from Activity a1
join Activity a2 
on a1.machine_id=a2.machine_id and a1.process_id=a2.process_id
and a1.activity_type='start' and a2.activity_type='end'
group by a1.machine_id

-- Table: Activity

-- +----------------+---------+
-- | Column Name    | Type    |
-- +----------------+---------+
-- | machine_id     | int     |
-- | process_id     | int     |
-- | activity_type  | enum    |
-- | timestamp      | float   |
-- +----------------+---------+
-- The table shows the user activities for a factory website.
-- (machine_id, process_id, activity_type) is the primary key (combination of columns with unique values) of this table.
-- machine_id is the ID of a machine.
-- process_id is the ID of a process running on the machine with ID machine_id.
-- activity_type is an ENUM (category) of type ('start', 'end').
-- timestamp is a float representing the current time in seconds.
-- 'start' means the machine starts the process at the given timestamp and 'end' means the machine ends the process at the given timestamp.
-- The 'start' timestamp will always be before the 'end' timestamp for every (machine_id, process_id) pair.
-- It is guaranteed that each (machine_id, process_id) pair has a 'start' and 'end' timestamp.
 

-- There is a factory website that has several machines each running the same number of processes. Write a solution to find the average time each machine takes to complete a process.

-- The time to complete a process is the 'end' timestamp minus the 'start' timestamp. The average time is calculated by the total time to complete every process on the machine divided by the number of processes that were run.

-- The resulting table should have the machine_id along with the average time as processing_time, which should be rounded to 3 decimal places.

-- Return the result table in any order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Activity table:
-- +------------+------------+---------------+-----------+
-- | machine_id | process_id | activity_type | timestamp |
-- +------------+------------+---------------+-----------+
-- | 0          | 0          | start         | 0.712     |
-- | 0          | 0          | end           | 1.520     |
-- | 0          | 1          | start         | 3.140     |
-- | 0          | 1          | end           | 4.120     |
-- | 1          | 0          | start         | 0.550     |
-- | 1          | 0          | end           | 1.550     |
-- | 1          | 1          | start         | 0.430     |
-- | 1          | 1          | end           | 1.420     |
-- | 2          | 0          | start         | 4.100     |
-- | 2          | 0          | end           | 4.512     |
-- | 2          | 1          | start         | 2.500     |
-- | 2          | 1          | end           | 5.000     |
-- +------------+------------+---------------+-----------+
-- Output: 
-- +------------+-----------------+
-- | machine_id | processing_time |
-- +------------+-----------------+
-- | 0          | 0.894           |
-- | 1          | 0.995           |
-- | 2          | 1.456           |
-- +------------+-----------------+
-- Explanation: 
-- There are 3 machines running 2 processes each.
-- Machine 0's average time is ((1.520 - 0.712) + (4.120 - 3.140)) / 2 = 0.894
-- Machine 1's average time is ((1.550 - 0.550) + (1.420 - 0.430)) / 2 = 0.995
-- Machine 2's average time is ((4.512 - 4.100) + (5.000 - 2.500)) / 2 = 1.456

# 577. Employee Bonus
Select e.name, b.bonus 
from Employee e
left join Bonus b
on e.empId = b.empId
where b.bonus<1000 or b.bonus is null
group by e.empId

# 1280. Students and Examinations
