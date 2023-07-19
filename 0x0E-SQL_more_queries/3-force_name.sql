-- Write a script that creates the table force_name on your MySQL server, force_name(id INT, name VARCHAR(256) can’t be null), database name will be passed, shouldn't fail
CREATE TABLE IF NOT EXISTS `force_name` (`id` INT, `name` VARCHAR(256) NOT NULL)
