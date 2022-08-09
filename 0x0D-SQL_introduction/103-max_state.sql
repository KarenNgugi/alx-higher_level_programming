-- display max temperature of each state (ordered by state name)
SELECT `state`, MAX(`state`) AS `max_temp` FROM `temperatures` GROUP BY `state` ORDER BY `max_temp` DESC;
