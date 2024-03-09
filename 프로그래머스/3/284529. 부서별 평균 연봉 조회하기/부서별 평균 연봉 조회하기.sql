select
    d.dept_id as DEPT_ID,
    d.dept_name_en as DEPT_NAME_EN,
    round(avg(e.sal), 0) as AVG_SAL
from HR_DEPARTMENT d
    join HR_EMPLOYEES e
    on d.dept_id = e.dept_id
group by d.dept_id
order by AVG_SAL desc