-- task101
SELECT `city`, AVG(`temperature`) AS `avg_temp` GROUP BY `city` ORDER BY `avg_temp` DESC