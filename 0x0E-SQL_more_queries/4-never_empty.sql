-- Write a script that creates the table id_not_null on your MySQL server, (id INT 1, name 256), database name passed, shouldn't fail
CREATE TABLE IF NOT EXISTS id_not_null(`id` INT DEFAULT 1, `name` VARCHAR(256))
