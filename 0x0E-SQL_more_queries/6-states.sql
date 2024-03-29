-- script creates database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
-- states description:
-- id INT unique, auto generated, can’t be null and is a primary key
-- name VARCHAR(256) can’t be null
-- If the database hbtn_0d_usa already exists, your script should not fail
-- If the table states already exists, your script should not fail

-- create database if not exists hbtn_0d_usa;
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- create table if not exists states
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
);
