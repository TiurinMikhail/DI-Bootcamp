SELECT
    m.medal_name,
    AVG(gc.age) AS average_age
FROM 
    olympics.competitor_event ce
JOIN 
    olympics.games_competitor gc ON ce.competitor_id = gc.id
JOIN 
    olympics.medal m ON ce.medal_id = m.id
WHERE
    ce.medal_id in (1,2,3)
GROUP BY
    m.medal_name;




SELECT nr.region_name, 
	COUNT(DISTINCT(gc.id)) AS unique_competitors
FROM olympics.games_competitor AS gc 
	JOIN olympics.person AS p ON gc.person_id=p.id				 
	JOIN olympics.person_region AS pr ON p.id=pr.person_id						 
	JOIN olympics.noc_region AS nr ON nr.id = pr.region_id
WHERE gc.id IN (
        SELECT
            competitor_id
        FROM
            olympics.competitor_event 
        GROUP BY
            competitor_id
        HAVING
            COUNT(DISTINCT event_id) > 3
    )
GROUP BY
    nr.region_name
ORDER BY
    unique_competitors DESC
LIMIT 5;



---Create a temporary table to store the total number of medals won by each competitor
--and filter to show only those who have won more than 2 medals. Use subqueries to aggregate the data.
drop table MedalCounts
	
CREATE TEMPORARY TABLE MedalCounts AS
SELECT gc.person_id, p.full_name,COUNT(ce.medal_id) AS total_medals
FROM olympics.competitor_event as ce join olympics.games_competitor as gc on ce.competitor_id=gc.id
									  join olympics.person as p on gc.person_id=p.id
									  join olympics.medal as m on m.id = ce.medal_id
where m.medal_name in ('Gold','Silver','Bronze')
group by gc.person_id, p.full_name;

SELECT *
FROM MedalCounts
WHERE total_medals > 2
order by total_medals desc;



---Use a subquery within a DELETE statement to remove records of competitors who have not won any
--medals from a temporary table created for analysis.

CREATE TEMPORARY TABLE tempCompetitors AS
(SELECT gc.id as comp_id,p.id as person_id, p.full_name,ce.medal_id
FROM olympics.competitor_event as ce join olympics.games_competitor as gc on ce.competitor_id=gc.id
									  join olympics.person as p on gc.person_id=p.id
									  join olympics.medal as m on m.id = ce.medal_id);

DELETE FROM tempCompetitors
WHERe medal_id = 4;




--Exercise 2: Advanced Data Manipulation And Optimization
--Task 1: Update the heights of competitors based on the average height of 
--competitors from the same region. Use a correlated subquery within the UPDATE
--statement.

-- select count(distinct person_id) from olympics.person_region
	
-- with avg_height_by_region (
-- select distinct(person_id), region_name
-- from olympics.person_region pr left join olympics.noc_region nr on pr.region_id=nr.id
-- group by pr.person_id
-- order by pr.person_id
-- )

-- UPDATE olympics.person AS p1
-- SET height = (
--     SELECT AVG(p2.height)
--     FROM olympics.person AS p2
--     JOIN olympics.person_region AS pr2 ON p2.id = pr2.person_id
--     WHERE pr2.region_id = (
--         SELECT pr1.region_id
--         FROM olympics.person_region AS pr1
--         WHERE pr1.person_id = p1.id
--     )
-- )
-- WHERE p1.height IS NOT NULL;


UPDATE olympics.person AS p1
SET height = (
    SELECT AVG(p2.height)  
    FROM olympics.person AS p2
    JOIN olympics.person_region AS pr2 ON p2.id = pr2.person_id
    WHERE pr2.region_id IN (
        SELECT pr1.region_id
        FROM olympics.person_region AS pr1
        WHERE pr1.person_id = p1.id
    )
)
WHERE p1.height is NULL or p1.height = 0; 


--Task 2: Insert new records into a temporary table for competitors who
--participated in more than one event in the same games and list their total
--number of events participated. Use nested subqueries for filtering.

CREATE TEMPORARY TABLE temp_competitor_events (
    competitor_id INTEGER,
    games_id INTEGER,
    total_events INTEGER
);

INSERT INTO temp_competitor_events (competitor_id, games_id, total_events)
SELECT competitor_id, games_id, COUNT(event_id) AS total_events
FROM (
    SELECT DISTINCT ce.competitor_id, gc.games_id, ce.event_id
    FROM olympics.competitor_event AS ce
    JOIN olympics.games_competitor AS gc ON ce.competitor_id = gc.id
) AS subquery
GROUP BY competitor_id, games_id
HAVING COUNT(event_id) > 1;

select * from temp_competitor_events;

drop table temp_competitor_events;


--Task 3: Identify regions where the average number of medals won per competitor 
--is greater than the overall average. Use subqueries to calculate and compare
--averages.

WITH person_by_region AS (
    SELECT pr.person_id, nr.region_name
    FROM olympics.person_region pr 
    JOIN olympics.noc_region nr ON pr.region_id = nr.id
),
person_name_by_region AS (
    SELECT p.id AS person_id, p.full_name, pbr.region_name
    FROM olympics.person p 
    JOIN person_by_region pbr ON p.id = pbr.person_id
),
games_info AS (
    SELECT gc.person_id, ce.medal_id
    FROM olympics.games_competitor AS gc
    JOIN olympics.competitor_event AS ce ON gc.id = ce.competitor_id
),
average_number_of_medals_by_person AS (
    SELECT pn.person_id, pn.full_name, pn.region_name, COUNT(gi.medal_id) AS number_of_medals
    FROM person_name_by_region pn
    JOIN games_info gi ON pn.person_id = gi.person_id
    WHERE gi.medal_id IN (1, 2, 3)
    GROUP BY pn.person_id, pn.full_name, pn.region_name
),
average_medals_by_region AS (
    SELECT region_name, AVG(number_of_medals) AS avg_medals
    FROM average_number_of_medals_by_person
    GROUP BY region_name
),
overall_average_medals AS (
    SELECT AVG(number_of_medals) AS overall_avg_medals
    FROM average_number_of_medals_by_person
)
SELECT amr.region_name, ROUND(amr.avg_medals, 2) AS avg_medals
FROM average_medals_by_region amr
WHERE amr.avg_medals > (SELECT overall_avg_medals FROM overall_average_medals)
order by ROUND(amr.avg_medals, 2) desc;


--Task 4: Create a temporary table to track competitors’ participation across 
--different seasons and identify those who have participated in both Summer 
--and Winter games.
	

CREATE TEMPORARY TABLE competitor_in_both_seasons as(
	with comp_in_summer as(
				select gc.id as comp_id, gc.games_id , g.season,gc.person_id
				from olympics.games_competitor as gc  join olympics.games g on g.id=gc.games_id
				where g.season = 'Summer'),
	comp_in_winter as (select gc.id as comp_id, gc.games_id , g.season, gc.person_id
				from olympics.games_competitor as gc  join olympics.games g on g.id=gc.games_id
				where g.season = 'Winter'),
	comp_by_season as (
				select *
				from comp_in_summer as s join comp_in_winter as w using(person_id)
	)
	select distinct(p.full_name)
	from comp_by_season as cs left join olympics.person as p on cs.person_id=p.id
);

select *
from competitor_in_both_seasons
order by full_name;

drop table competitor_in_both_seasons;


