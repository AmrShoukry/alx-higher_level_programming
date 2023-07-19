-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT `tv_genres.name` AS `genre`, COUNT(`tv_shows_genres.genre_id`) AS `number_of_shows` 
FROM `tv_genres` INNER JOIN `tv_shows_genres` ON `tv_genres.id` = `tv_shows_genres.genre_id`
GROUP BY `genre`
ORDER BY `genre` DESC
