-- script lists all records of the table second_table
-- of the database hbtn_0c_0 in your MySQL server.
-- Results should display both the score and the name (in this order)
-- Records should be ordered by score (top first)
--
-- score name
-- 14  Bob
-- 10  John
-- 8   George
-- 3   Alex

SELECT score, name FROM second_table ORDER BY score DESC;
