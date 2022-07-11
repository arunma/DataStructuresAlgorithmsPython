-- https://learnsql.com/blog/sql-recursive-cte/

--CREATE TABLE `emp` (
--  `id` int NOT NULL,
--  `first` varchar(45) DEFAULT NULL,
--  `last` varchar(45) DEFAULT NULL,
--  `boss_id` int DEFAULT NULL,
--  PRIMARY KEY (`id`)
--) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
--
--INSERT INTO leet1.emp (id,`first`,`last`,boss_id) VALUES
--	 (1,'Domenic','Leaver',5),
--	 (2,'Cleveland','Hewins',1),
--	 (3,'Kakalina','Atherton',8),
--	 (4,'Roxanna','Fairlie',NULL),
--	 (5,'Hermie','Comsty',4),
--	 (6,'Pooh','Goss',8),
--	 (7,'Faulkner','Challiss',5),
--	 (8,'Bobbe','Blakeway',4),
--	 (9,'Laurene','Burchill',1),
--	 (10,'Augusta','Gosdin',8);

with recursive cte as(
	select
		id,
		first,
		last,
		boss_id,
		0 as hierarchy_level
	from
		emp
	where boss_id is NULL

	union ALL

	SELECT
		e.id,
		e.first,
		e.last,
		e.boss_id,
		hierarchy_level+1 as hierarchy_level
	from
		cte c
	join
		emp e
	where
		e.boss_id =c.id

)
select
	ch.id,
	ch.first,
	ch.last,
	pa.id,
	pa.first,
	pa.last,
	ch.hierarchy_level
from
	cte ch
left join
	emp pa
on
	ch.boss_id =pa.id