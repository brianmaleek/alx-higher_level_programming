-- script creates the database hbtn_0d_2 and the user user_0d_2.
-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
-- The user_0d_2 password should be set to user_0d_2_pwd
-- If the database hbtn_0d_2 already exists, your script should not fail
-- If the user user_0d_2 already exists, your script should not fail

-- create hbtn_0d_2 database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- create user_0d_2 user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- grant select privilege to user_0d_2 on hbtn_0d_2 database
GRANT USAGE ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- reload privileges
FLUSH PRIVILEGES;
