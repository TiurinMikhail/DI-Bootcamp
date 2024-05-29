---Daily chl
--Task 1: Calculate The Average Budget Growth Rate For Each Production Company
--Calculate the average budget growth rate for each production company across all 
--movies they have produced. Use window functions to determine the budget growth
--rate and then calculate the average growth rate.


WITH company_info AS (
    SELECT * 
    FROM movies.movie_company
    LEFT JOIN movies.production_company USING (company_id)
),
budget_growth AS (
    SELECT 
        company_name, 
        CAST(budget AS NUMERIC) AS budget,
        CAST(LAG(budget) OVER (PARTITION BY company_name ORDER BY movie_id) AS NUMERIC) AS previous_budget
    FROM movies.movie AS m
    LEFT JOIN company_info ci USING(movie_id)
),
budget_growth_rate AS (
    SELECT 
        company_name, 
        budget, 
        previous_budget,
        CASE 
            WHEN previous_budget = 0 THEN NULL
            ELSE 100*((budget - previous_budget) / previous_budget) --multiply by 100?
        END AS growth_rate
    FROM budget_growth
	where previous_budget is not NULL
)
SELECT company_name , round(avg(growth_rate),0) as Average_Budget_Growth_Rate
FROM budget_growth_rate
where growth_rate is not NULL and company_name is not NULL
group by company_name
order by round(avg(growth_rate),0) desc;

