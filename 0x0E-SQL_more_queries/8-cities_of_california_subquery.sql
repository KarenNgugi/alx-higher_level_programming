-- list all Californian cities that can be found in database `hbtn_0d_usa`
SELECT `cities`.`id`, `cities`.`name` FROM `cities` WHERE `cities`.`id` =
	(SELECT `state`.`id` FROM `states` WHERE `state`.`name` = "California";)
ORDER BY `cities`.`id`;
