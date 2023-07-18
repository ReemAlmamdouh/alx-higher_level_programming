-- displays the max temperature of each state (ordered by State name).

SELECT state, MAX(value) AS MAX_temp
FROM temperatures
WHERE month = 7 or month = 8
GROUP BY state
ORDER BY state;
