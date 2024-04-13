with wt as(
/* 해당 스킬을 보유한 개발자만을 JOIN 조건으로 사용하여 JOIN */
    select *
    from skillcodes s, developers d
    where substr(reverse(conv(d.skill_code, 10, 2)), length(conv(s.code, 10, 2)), 1) = 1
)

select
    id,
    email,
    first_name,
    last_name
from developers d
where 'Front End' in (select category from wt where id = d.id)
order by id