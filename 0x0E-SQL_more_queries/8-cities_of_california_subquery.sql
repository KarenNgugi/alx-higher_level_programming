-- list all Californian cities that can be found in database `hbtn_0d_usa`
SELECT * FROM `cities` WHERE `id` =
	(SELECT `id` FROM `states` WHERE `name` = "California";)
ORDER BY `cities`.`id`;
