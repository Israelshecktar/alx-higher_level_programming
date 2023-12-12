-- Display the average temperature by city
SELECT city, AVG(temp) AS avg_temp FROM temperature GROUP BY city ORDER BY avg_temp DESC;
