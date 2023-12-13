-- Use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- List the cities of California
SELECT id, name FROM cities
-- Filter the cities by the state name using a subquery
WHERE state_id IN (
  -- Get the state id of California from the states table
  SELECT id FROM states
  WHERE name = 'California'
)
-- Sort the results by the cities.id column
ORDER BY id;
