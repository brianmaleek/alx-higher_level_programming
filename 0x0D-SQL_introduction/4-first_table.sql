-- create first_table, table in the current database
-- if the table exists, script should not fail
-- table columns id, name

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
