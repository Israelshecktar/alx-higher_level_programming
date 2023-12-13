-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- List the cities by states
SELECT cities.id, cities.name, states.name
-- Join the cities and states tables on the state_id column
FROM cities
JOIN states ON cities.state_id = states.id
-- Sort the results by the cities.id column
ORDER BY cities.id;
