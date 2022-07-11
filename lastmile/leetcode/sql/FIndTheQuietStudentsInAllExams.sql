with top_bottom as (
	select
		s.student_id,
		s.student_name,
		rank() over (partition by exam_id order by score desc) rk_top,
		rank() over (partition by exam_id order by score asc) rk_bot
	FROM
		Exam e
	left join
		Student s
	on s.student_id =e.student_id
)
select distinct
	student_id ,
	student_name
from
	top_bottom
WHERE
	student_id not in (select student_id from top_bottom where rk_top=1 or rk_bot=1)
order by student_id
