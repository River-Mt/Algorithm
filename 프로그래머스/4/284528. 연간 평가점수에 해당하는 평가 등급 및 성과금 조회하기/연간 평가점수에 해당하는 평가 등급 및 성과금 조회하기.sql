with wt as (
    select 
        t.emp_no,
        case
            when t.score >= 96 then 'S' 
            when t.score >= 90 then 'A'
            when t.score >= 80 then 'B'
            else 'C'
        end as grade,
        case
            when t.score >= 96 then 0.2 
            when t.score >= 90 then 0.15
            when t.score >= 80 then 0.1
            else 0
        end as rate
    from (
        select
            emp_no,
            sum(score) / 2 score
        from hr_grade
        group by emp_no
    ) t
)

select 
    a.emp_no,
    a.emp_name,
    b.grade,
    (a.sal * b.rate) bonus
from hr_employees a, wt b
where 1=1
    and a.emp_no = b.emp_no