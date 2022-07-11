with recursive possible_routes as (
	select
		city_to,
		concat(city_from, '->', city_to) as route,
		distance
	from
		cities_route
	where
		city_from ='Groningen'

	union ALL

	select
		cr.city_to,
		concat(pr.route, '->', cr.city_to) as route,
		pr.distance+cr.distance
	from
		cities_route cr
	join
		possible_routes pr
	on
	pr.city_to=cr.city_from

)

select * from possible_routes;


--CREATE TABLE `leet1`.`cities_route` (
--  `city_from` VARCHAR(50) NOT NULL,
--  `city_to` VARCHAR(45) NULL,
--  `distance` DOUBLE NULL,
--  PRIMARY KEY (`city_from`));

--
--INSERT INTO leet1.cities_route (city_from,city_to,distance) VALUES
--	 ('Amsterdam','Haarlem',30.0),
--	 ('Groningen','Heerenveen',61.4),
--	 ('Harlingen','Wieringerwerf',52.3),
--	 ('Heerenveen','Lelystad',74.0),
--	 ('Hoorn','Amsterdam',46.1),
--	 ('Lelystad','Amsterdam',57.2),
--	 ('Wieringerwerf','Hoorn',26.5);
