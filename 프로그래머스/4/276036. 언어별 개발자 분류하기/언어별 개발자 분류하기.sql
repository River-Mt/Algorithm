with wt as(
    select s.name, s.category, d.id, conv(s.code, 10, 2), conv(d.skill_code, 10, 2)
    from skillcodes s, developers d
    where substr(reverse(conv(d.skill_code, 10, 2)), length(conv(s.code, 10, 2)), 1) = 1
    order by d.id
), wt_02 as (
    select
        d.id,
        d.email,
        case
            when 1=1
                and 'Front End' in (select category from wt where id = d.id)
                and 'Python' in (select name from wt where id = d.id)
            then 'A'

            when 'C#' in (select name from wt where id = d.id)
            then 'B'

            when 'Front End' in (select category from wt where id = d.id)
            then 'C'

            else 'etc'
        end as GRADE
    from developers d
)

select 
    grade,
    id, 
    email
from wt_02
where grade <> 'etc'
order by grade, id
    







