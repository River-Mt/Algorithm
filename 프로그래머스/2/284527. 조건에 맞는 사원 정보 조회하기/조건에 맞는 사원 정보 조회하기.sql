select 
    a.score,
    b.emp_no,
    b.emp_name,
    b.position,
    b.email
from (
    select 
        g.emp_no,
        sum(g.score) as score
    from hr_grade g
    group by g.emp_no
) a 
join hr_employees b on a.emp_no = b.emp_no
order by score desc
limit 1

    