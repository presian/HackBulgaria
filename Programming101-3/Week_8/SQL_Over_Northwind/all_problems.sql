--1 List all employees with their first name, last name and title.
SELECT 
	FirstName,
	LastName,
	Title
FROM employees

--2 List all employees from Seattle.
SELECT
	*
FROM employees 
WHERE  City = 'Seattle'

--3 List all employees from London.
SELECT
	*
FROM employees 
WHERE  City = 'London'

--4 List all employees that work in the Sales department.
SELECT
	*
FROM employees
WHERE Title LIKE '%Sales%'

--5 List all females employees that work in the Sales department.
SELECT
	*
FROM employees
WHERE Title LIKE '%Sales%'
	AND TitleOfCourtesy IN ('Ms.', 'Mrs.')

--6 List the 5 oldest employees.
SELECT
	*
FROM employees
ORDER BY BirthDate
LIMIT 5

--7 List the first 5 hires of the company.
SELECT
	*
FROM employees
ORDER BY HIreDate
LIMIT 5

--8 List the employee who reports to no one (the boss)
SELECT
	*
FROM employees
WHERE ReportsTo IS NULL

--9 List all employes by their first and last name, and the first and last name of the employees that they report to.
SELECT
	e.FirstName,
	e.LastName,
	m.FirstName,
	m.LastName
FROM employees e
LEFT JOIN employees m
ON e.ReportsTo = m.EmployeeID

--10 Count all female employees.
SELECT
	*
FROM employees
WHERE TitleOfCourtesy IN ('Ms.', 'Mrs.')

--11 Count all male employees.
SELECT
	*
FROM employees
WHERE TitleOfCourtesy NOT IN ('Ms.', 'Mrs.')

--12 Count how many employees are there from the different cities. For example, there are 4 employees from London.
SELECT
	City,
	COUNT(*)
FROM employees
GROUP BY City

--13 List all OrderIDs and the employees (by first and last name) that have created them.
SELECT
	o.OrderID,
	e.FirstName,
	e.LastName
FROM orders o
LEFT JOIN employees e
ON o.EmployeeID =  e.EmployeeID

--14 List all OrderIDs and the shipper name that the order is going to be shipped via.
SELECT
	o.OrderID,
	s.CompanyName
FROM orders o
LEFT JOIN shippers s
ON o.ShipVia =  s.ShipperID

--15 List all contries and the total number of orders that are going to be shipped there.
SELECT
	ShipCountry,
	COUNT(*) 
FROM orders
GROUP BY ShipCountry

--16 Find the employee that has served the most orders.
SELECT
	e.FirstName,
	e.LastName,
	COUNT(*) AS COUNT
FROM orders o
LEFT JOIN Employees e
ON o.EmployeeID = e.EmployeeID
GROUP BY o.EmployeeID
ORDER BY COUNT DESC
LIMIT 1

--17 Find the customer that has placed the most orders.
SELECT
	c.CompanyName,
	COUNT(*) AS COUNT
FROM orders o
LEFT JOIN customers c
ON o.CustomerID = c.CustomerID
GROUP BY o.CustomerID
ORDER BY COUNT DESC
LIMIT 1

--18 List all orders, with the employee serving them and the customer, that has placed them.
SELECT
	*
FROM orders o
LEFT JOIN employees e
ON o.EmployeeID = e.EmployeeID
LEFT JOIN customers c
ON o.CustomerID = c.CustomerID

--19 List for which customer, which shipper is going to deliver the order.
SELECT
	c.CompanyName,
	s.CompanyName
FROM orders o
LEFT JOIN customers c
ON o.CustomerID = c.CustomerID
LEFT JOIN shippers s
ON o.ShipVia = s.ShipperID