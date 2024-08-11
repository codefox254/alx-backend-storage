-- Task: Create a trigger that decreases the quantity of an item after adding a new order
-- This script creates a trigger named 'decrement' which will update the 'items' table

DELIMITER //

CREATE TRIGGER decrement
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END; //

DELIMITER ;