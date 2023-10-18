-- Lists all records in table with specified name (NOT NULL)
-- in descending order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC
