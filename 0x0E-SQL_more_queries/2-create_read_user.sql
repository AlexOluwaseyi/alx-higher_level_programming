-- Creates database hbtn_0d_2 and user_0d_2
-- Assigns SELECT privilege in the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost;
GRANT SELECT
ON hbtn_0d_2.*
TO user_0d_2@localhost;
