with recursive all_days_cte as (
	select
		min(period_start) as dt
	from
		Sales
	union
	select
		DATE_ADD(dt, interval 1 day)
	from
		all_days_cte
	where
		dt <= (select max(period_end) from Sales)

)
select
	s.product_id,
	p.product_name,
	DATE_FORMAT(c.dt, '%Y') as report_year,
	sum(s.average_daily_sales) as total_amount
from
	Product p
join
	Sales s
on
	s.product_id =p.product_id
JOIN
	all_days_cte c
WHERE
	dt BETWEEN period_start and period_end
group by
	1,2,3
order by product_id
