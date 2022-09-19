#Consulta 1
SELECT SUM (cumulative_confirmed) AS total_cases_worldwide
FROM bigquery-public-data.covid19_open_data.covid19_open_data
WHERE DATE = "2020-04-20"
LIMIT 10;

#Consulta 2
SELECT COUNT (state) AS count_of_states FROM (
SELECT --Count(Distinct subregion1_name) AS count_of_states
subregion1_name as state, Sum(cumulative_deceased) as total_deaths
FROM bigquery-public-data.covid19_open_data.covid19_open_data
where subregion1_name is not null and country_name = "United States of America" AND DATE = "2020-04-20" 
group by country_name, subregion1_name) inf
where total_deaths > 150
Order by count_of_states desc;

#Consulta 3
SELECT * FROM (
SELECT subregion1_name as state,  SUM (cumulative_confirmed) AS total_confirmed_cases
FROM bigquery-public-data.covid19_open_data.covid19_open_data
where subregion1_name is not null and country_code = "US"AND DATE = "2020-04-20"
group by subregion1_name
Order by total_confirmed_cases desc
) WHERE total_confirmed_cases > 2000
LIMIT 10;

#Consulta 4
SELECT SUM (cumulative_confirmed) AS total_confirmed_cases,
  SUM (cumulative_deceased) AS total_deaths,(SUM(cumulative_deceased)/SUM (cumulative_confirmed))*100 as case_fatality_ratio
FROM bigquery-public-data.covid19_open_data.covid19_open_data
WHERE country_name="Italy" AND date BETWEEN "2020-05-01" AND "2020-05-31";

#Consulta 5
SELECT
 date
FROM
  `bigquery-public-data.covid19_open_data.covid19_open_data`
WHERE
 country_name = 'Italy'
 AND cumulative_deceased > 10000
ORDER BY date
LIMIT 1;

#Consulta 6 
WITH india_cases_by_date AS (
  SELECT
    date,
    SUM(cumulative_confirmed) AS cases
  FROM
    `bigquery-public-data.covid19_open_data.covid19_open_data`
  WHERE
    country_name="India"
    AND date between '2020-02-25' and '2020-03-15'
  GROUP BY
    date
  ORDER BY
    date ASC
 )

, india_previous_day_comparison AS
(SELECT
  date,
  cases,
  LAG(cases) OVER(ORDER BY date) AS previous_day,
  cases - LAG(cases) OVER(ORDER BY date) AS net_new_cases
FROM india_cases_by_date
)
SELECT
  COUNT(date)
FROM
  india_previous_day_comparison
WHERE
  net_new_cases = 0;

#Consulta 7
WITH us_cases_by_date AS (
  SELECT
    date,
    SUM( cumulative_confirmed ) AS cases
  FROM
    `bigquery-public-data.covid19_open_data.covid19_open_data`
  WHERE
    country_name="United States of America"
    AND date between '2020-03-22' and '2020-04-20'
  GROUP BY
    date
  ORDER BY
    date ASC
 )

, us_previous_day_comparison AS
(SELECT
  date,
  cases,
  LAG(cases) OVER(ORDER BY date) AS previous_day,
  cases - LAG(cases) OVER(ORDER BY date) AS net_new_cases,
  (cases - LAG(cases) OVER(ORDER BY date))*100/LAG(cases) OVER(ORDER BY date) AS percentage_increase
FROM us_cases_by_date
)
SELECT
  Date,
  cases AS Confirmed_Cases_On_Day,
  previous_day AS Confirmed_Cases_Previous_Day,
  percentage_increase AS Percentage_Increase_In_Cases
FROM
  us_previous_day_comparison
WHERE
  percentage_increase > 10

#Consulta 8
WITH cases_by_country AS (
  SELECT
    country_name AS country,
    SUM(cumulative_confirmed) AS cases,
    SUM(cumulative_recovered) AS recovered_cases
  FROM
    `bigquery-public-data.covid19_open_data.covid19_open_data`
  WHERE
    date="2020-05-10"
  GROUP BY
    country_name
)

, recovered_rate AS (
  SELECT
    country, cases, recovered_cases,
    (recovered_cases * 100)/cases AS recovery_rate
  FROM
    cases_by_country
)

SELECT country, cases AS confirmed_cases, recovered_cases, recovery_rate
FROM
   recovered_rate
WHERE
   cases > 50000
ORDER BY recovery_rate DESC
LIMIT 10
