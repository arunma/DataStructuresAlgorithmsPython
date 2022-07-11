# Write your MySQL query statement below
with count_rank as (
    select
        username,
        activity,
        startDate,
        endDate,
        count(username) over (partition by username) as user_count,
        row_number() over (partition by username order by startDate desc) as rownum
    from
        UserActivity
)
select
    username,
    activity,
    startDate,
    endDate
from
    count_rank
where
    user_count=1 or rownum=2
