-- script creates a table second_table if it doesn’t exist
-- in the database hbtn_0c_0 in MySQL server and add multiples rows.
-- second_table description:
-- @param: id INT
-- @param: name VARCHAR(256)
-- @param: score INT
-- script should create these records:
-- @param: id = 1, name = “John”, score = 10
-- @param: id = 2, name = “Alex”, score = 3
-- @param: id = 3, name = “Bob”, score = 14
-- @param: id = 4, name = “George”, score = 8

CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
INSERT INTO second_table (id, name, score) VALUES
(1, "John", 10),
(2, "Alex", 3),
(3, "Bob", 14),
(4, "George", 8);
