-- Setup mysql test database

-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;
-- Create user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant privileges to user
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
-- Grant SELECT privileges to new user on 'performance_schema' database
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';

FLUSH PRIVILEGES;