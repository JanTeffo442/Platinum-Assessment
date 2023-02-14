1.1
SELECT client_id FROM CLIENT_INFO_TABLE
UNION
SELECT department FROM COMPANY_TABLE;

1.2 INNER JOIN


1.3.1
SELECT employee_name,manager_id
FROM employee;

1.3.2 Pieter is the manager

2.
SELECT
SUM(CASE WHEN s < 0 THEN s ELSE 0 END) AS sum_negative,
SUM(CASE WHEN s > 0 THEN s ELSE 0 END) AS sum_positive
FROM numbers;

3.
SELECT id,COUNT(id) AS DuplicateEntries
FROM employees
GROUP BY id
HAVING COUNT(id)>1;

3.1
SELECT age from
(SELECT age FROM employees
ORDER BY age DESC LIMIT 4)
AS Third ORDER BY age DESC LIMIT 4;

4.
CREATE TABLE Table1(
Make VARCHAR(50),
Model VARCHAR(50),
Manufacture_Date DATE,
Costs BIGINT,
Model_id VARCHAR(10)
);


CREATE TABLE Table2(
Manufacturer VARCHAR(50),
Model_id VARCHAR(10),
Parts VARCHAR(50),
Warranty_Expiry_Date DATE,
City VARCHAR(50)
);



5.1
CREATE TEMPORARY TABLE if not exists temporary_table AS (
SELECT 
make,model,costs,manufacture_date FROM table1 
UNION 
SELECT 
parts,warranty_expiry_date FROM table2
);

5.2
DROP TABLE #TEMP
CREATE TABLE #TEMP
(
  -- Define your Columns here
)  
SELECT [COLUMNS] INTO #TEMP  FROM [SOURCE-TABLE]

6.
SELECT * FROM OPENQUERY(Vicidial,SELECT 8 FROM Users);



