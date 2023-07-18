-- task103
SELECT `state`, MAX(`temperature`) AS `max_temp` GROUP BY `state` ORDER BY `state`
