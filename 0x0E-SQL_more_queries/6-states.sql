-- script that creates the database and a table with some specify info

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
name VARCHAR(256) NOT NULL);