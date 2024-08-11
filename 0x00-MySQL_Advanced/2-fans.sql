-- Task: Calculate the total number of fans by origin and order the results
-- This script selects the origin and the sum of fans (as nb_fans)
-- from the metal_bands table, grouped by origin and ordered by nb_fans in descending order

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;