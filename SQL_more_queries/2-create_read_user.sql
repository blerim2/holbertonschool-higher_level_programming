-- Connect to MySQL server as root (you can replace 'root' with your actual MySQL username)
mysql -u root -p

-- Create the database 'hbtn_0d_2' if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user 'user_0d_2' with the specified password
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on the database 'hbtn_0d_2' to the user 'user_0d_2'
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;

-- Exit MySQL
EXIT;
