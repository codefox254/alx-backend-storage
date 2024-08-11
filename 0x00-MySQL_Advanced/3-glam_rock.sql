-- Task: Select band names and compute their lifespan for Glam rock bands
-- You should use attributes 'formed' and 'split' for computing the lifespan
-- Your script can be executed on any database

SELECT band_name, 
       (IFNULL(split, 2022) - formed) AS lifespan
FROM metal_bands 
WHERE style LIKE '%Glam rock%' 
ORDER BY lifespan DESC;
