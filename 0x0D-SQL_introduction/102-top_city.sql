-- Import in hbtn_0c_0 database this table dump: download (same as Temperatures #0)
-- script displays the top 3 of cities temperature during July and August ordered by temperature (descending)
--
-- city    avg_temp
-- Naperville  76.9412
-- San Diego   73.7941
-- Sunnyvale   73.2353

SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month = 7 or month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
