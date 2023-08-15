-- script lists all records of the table second_table of the database hbtn_0c_0 in MySQL server.
-- Don’t list rows without a name value
-- Results should display the score and the name (in this order)
-- Records should be listed by descending score
-- score   name
-- 18  Aria
-- 12  Aria
-- 10  John
-- 10  Bob

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
