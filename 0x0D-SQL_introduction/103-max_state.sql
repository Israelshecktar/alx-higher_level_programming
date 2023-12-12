-- Display the max temperature of each state
SELECT state, MAX (temp) AS max_temp FROM temperature
GROUP BY state
ORDER BY state ASC;
