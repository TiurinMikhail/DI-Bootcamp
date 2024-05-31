--EX1 Task 1: Identify competitors who have won at least one medal in 
--events spanning both Summer and Winter Olympics. Create a temporary table to
--store these competitors and their medal counts for each season, and then display
--the contents of this table.
-- CREATE TEMP TABLE IF NOT EXISTS temp_medal_winners AS (
--     SELECT DISTINCT
--         gc.person_id
--     FROM
--         olympics.games_competitor gc
--     JOIN
--         olympics.competitor_event ce ON gc.id = ce.competitor_id
--     JOIN
--         olympics.games g ON ce.event_id = g.id
--     WHERE
--         g.season IN ('Summer', 'Winter')
--     GROUP BY
--         gc.person_id
--     HAVING
--         COUNT(DISTINCT CASE WHEN g.season = 'Summer' THEN g.id END) > 0
--         AND COUNT(DISTINCT CASE WHEN g.season = 'Winter' THEN g.id END) > 0
-- );

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
	select distinct(person_id)
	from comp_by_season as cs left join olympics.person as p on cs.person_id=p.id
);

CREATE TEMP TABLE IF NOT EXISTS temp_medal_counts AS (
    SELECT
        gc.person_id,
        g.season,
        COUNT(ce.medal_id) AS medal_count
    FROM
        olympics.games_competitor gc
    JOIN
        olympics.competitor_event ce ON gc.id = ce.competitor_id
    JOIN
        olympics.games g ON ce.event_id = g.id
    WHERE
        gc.person_id IN (SELECT person_id FROM competitor_in_both_seasons)
    GROUP BY
        gc.person_id, g.season
);

SELECT full_name,season,medal_count
FROM temp_medal_counts tmc left join olympics.person p on p.id=tmc.person_id;


--Task 2: Create a temporary table to store competitors who have won medals in 
--exactly two different sports, and then use a subquery to identify the top 3
--competitors with the highest total number of medals across all sports.
--Display the contents of this table.



CREATE TEMPORARY TABLE winners_in_two_sports as(
	with competitor_with_medal as(
		select gc.id as competitor_id, person_id,event_id,medal_id
		from olympics.games_competitor gc left join olympics.competitor_event ce on ce.competitor_id=gc.id
		where ce.medal_id in (1,2,3)
	),
	event_info as (
		select e.id as event_id, s.id as sport_id 
		from olympics.event e left join olympics.sport s on e.sport_id=s.id
	),
	competitor_with_medal_info as (
		select *
		from competitor_with_medal cwm left join olympics.person p on cwm.person_id=p.id
	),
	competitor_with_medal_in_two_sports as(
		select person_id,full_name, count(distinct(sport_id)) as  number_of_sports
		from competitor_with_medal_info cwmi join event_info ei using(event_id)
		group by person_id, full_name
		having count(distinct(sport_id)) = 2
	)
	select person_id,full_name, count(medal_id) as  number_of_medals
	from competitor_with_medal_info cwmi join event_info ei using(event_id)
	where person_id in (select person_id from competitor_with_medal_in_two_sports)
	group by person_id,full_name
	order by number_of_medals desc
);

select *
from winners_in_two_sports
limit 3;

drop table winners_in_two_sports;
-- CREATE TEMPORARY TABLE winners_in_two_sports as(
-- with competitor_with_medal as(
-- 		select gc.id as competitor_id, person_id,event_id,medal_id
-- 		from olympics.games_competitor gc join olympics.competitor_event ce on ce.competitor_id=gc.id
-- 		where ce.medal_id in (1,2,3)
-- 	),
-- 	event_info as (
-- 		select e.id as event_id, s.id as sport_id ,sport_name
-- 		from olympics.event e join olympics.sport s on e.sport_id=s.id
-- 	),
-- 	competitor_with_medal_info as (
-- 		select *
-- 		from competitor_with_medal cwm join olympics.person p on cwm.person_id=p.id
-- 	)
-- 		select full_name, count(medal_id) as  number_of_medals
-- 		from competitor_with_medal_info cwmi join event_info ei using(event_id)
-- 		group by full_name
-- 		having count(distinct(sport_id)) = 2);

-- select *
-- from winners_in_two_sports
-- order by number_of_medals desc
-- limit 3;


---v2
CREATE TEMPORARY TABLE Temp_Competitors_Medals AS
SELECT gc.person_id AS competitor_id,
       COUNT(DISTINCT e.sport_id) AS sport_count,
       COUNT(ce.medal_id) AS total_medals
FROM olympics.competitor_event ce
JOIN olympics.games_competitor gc ON ce.competitor_id = gc.id
JOIN olympics.event e ON ce.event_id = e.id
WHERE ce.medal_id in (1,2,3)
GROUP BY gc.person_id
HAVING COUNT(DISTINCT e.sport_id) = 2;

SELECT competitor_id, total_medals
FROM Temp_Competitors_Medals
ORDER BY total_medals DESC
LIMIT 3;

SELECT * FROM Temp_Competitors_Medals;

drop table Temp_Competitors_Medals;



--Exercise 2: Region And Competitor Performance


--Task 1: Retrieve the regions that have competitors who have won the highest number of medals in a single Olympic event. 
--Use a subquery to determine the event with the highest number of medals for each competitor, and then display the top 5 regions with 
--the highest total medals.
CREATE TEMPORARY TABLE competitors_medals_by_event AS(
		select competitor_id, event_id, count(medal_id) as total_medals
		from olympics.competitor_event 
		where medal_id in (1,2,3)
		group by competitor_id,event_id);

-- select distinct competitor_id
-- from olympics.competitor_event 

CREATE TEMPORARY TABLE event_with_highest_num_medals_for_competitor AS(
SELECT competitor_id, event_id, total_medals
FROM competitors_medals_by_event cme
WHERE total_medals = (SELECT MAX(total_medals)
				        FROM competitors_medals_by_event
				        WHERE competitor_id = cme.competitor_id));


--top 5 regions with the highest total medals
with person_region_info as(
	select p.id,p.full_name,nr.region_name
	from olympics.person p join olympics.person_region pr on p.id=pr.person_id
						   join olympics.noc_region nr on  pr.region_id=nr.id
)
select pri.region_name, count(ewh.total_medals) as total_medals_by_cntry
from olympics.games_competitor gc join person_region_info pri on pri.id=gc.person_id
								   join	 event_with_highest_num_medals_for_competitor ewh on ewh.competitor_id=gc.id
where gc.id in (select competitor_id from event_with_highest_num_medals_for_competitor)
group by region_name
order by count(ewh.total_medals) desc
limit 5;

--check for one event with higthest number medal (the evnet_id=14)
with person_region_info as(
	select p.id,p.full_name,nr.region_name
	from olympics.person p join olympics.person_region pr on p.id=pr.person_id
						   join olympics.noc_region nr on  pr.region_id=nr.id
)
select ewh.event_id, count(ewh.total_medals) as total_medals_by_cntry
from olympics.games_competitor gc join person_region_info pri on pri.id=gc.person_id
								   join	 event_with_highest_num_medals_for_competitor ewh on ewh.competitor_id=gc.id
where gc.id in (select competitor_id from event_with_highest_num_medals_for_competitor)
group by ewh.event_id
order by count(ewh.total_medals) desc
limit 1;

-- check for the top 5 countries by one event with the highest number of medals
with person_region_info as(
	select p.id,p.full_name,nr.region_name
	from olympics.person p join olympics.person_region pr on p.id=pr.person_id
						   join olympics.noc_region nr on  pr.region_id=nr.id
)
select pri.region_name, count(ewh.total_medals) as total_medals_by_cntry
from olympics.games_competitor gc join person_region_info pri on pri.id=gc.person_id
								   join	 event_with_highest_num_medals_for_competitor ewh on ewh.competitor_id=gc.id
where gc.id in (select competitor_id from event_with_highest_num_medals_for_competitor) and ewh.event_id = 14
group by pri.region_name
order by count(ewh.total_medals) desc
limit 5;

drop table competitors_medals_by_event;
drop table event_with_highest_num_medals_for_competitor;


--Task 2: Create a temporary table to store competitors who have participated in more than three Olympic Games but have not won any medals.
--Retrieve and display the contents of this table, including their full names and the number of games they participated in.


CREATE TEMPORARY TABLE Temp_Competitors_No_Medals AS(
with competitors_games_count AS (
    select gc.person_id,p.full_name, count(DISTINCT gc.games_id) AS games_count
    from olympics.games_competitor gc join olympics.person p on gc.person_id=p.id
    group by gc.person_id,p.full_name
    having count(DISTINCT gc.games_id) > 3
),
competitors_with_no_medals as (
	select distinct competitor_id
    from olympics.competitor_event ce join olympics.games_competitor gc  on gc.id=ce.competitor_id
	where medal_id = 4
)
select distinct(cgc.full_name), cgc.games_count
from olympics.games_competitor gc join competitors_games_count cgc using(person_id)
where gc.id in (select * from competitors_with_no_medals) and gc.person_id in (select person_id from competitors_games_count)						
);

select * 
from Temp_Competitors_No_Medals;

drop table Temp_Competitors_No_Medals;






