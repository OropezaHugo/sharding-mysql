to set up the DBs:
CREATE DATABASE shard1;
CREATE DATABASE shard2;

USE shard1;
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

USE shard2;
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);
