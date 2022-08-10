-- list all shows contained in `hbtn_0d_tvshows` that have at least one genre
-- each record should display `tv_shows.title` `tv_show_genres.genre_id`
-- results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
-- you can use only one SELECT statement
SELECT `tv_shows`.`title`, `tv_show_genres`.`genre_id`
FROM `hbtn_0d_tvshows`.`tv_shows`
INNER JOIN `hbtn_0d_tvshows`.`tv_show_genres` ON `tv_shows`.`id` = `tv_show_genres`.`genre_id`
ORDER BY `tv_shows`.`title`, `tv_show_genres`.`genre_id`;
