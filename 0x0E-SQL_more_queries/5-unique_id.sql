-- Write a script that creates the table unique_id on your MySQL server, (id INT 1 UNIQUE, name 256), database name passed, shouldn't fail
CREATE TABLE IF NOT EXISTS `unique_id` (`id` INT UNIQUE DEFAULT 1, `name` VARCHAR(256))
