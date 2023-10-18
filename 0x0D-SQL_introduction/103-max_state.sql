-- Max temp per state
SOURCE temperatures.sql
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC
