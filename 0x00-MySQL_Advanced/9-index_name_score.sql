-- Task: Create an index idx_name_first_score on the table names using the first letter of name and the score
-- This script creates an index named 'idx_name_first_score' on the 'names' table

CREATE INDEX idx_name_first_score
ON names (name(1), score);
