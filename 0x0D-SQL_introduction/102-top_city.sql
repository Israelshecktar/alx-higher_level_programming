-- Display the top 3 of cities temperature during July and August
SELECT city, AVG (temp) AS avg_temp FROM temperature
WHERE MONTH (date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
