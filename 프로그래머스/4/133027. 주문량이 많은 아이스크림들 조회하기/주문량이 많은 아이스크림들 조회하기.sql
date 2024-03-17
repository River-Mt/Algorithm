


select flavor
from (
    select
        a.flavor
    ,   sum(a.total_order + b.total_order) sum
    from first_half a, july b
    where a.flavor = b.flavor
    group by a.flavor
    order by sum desc
)
where rownum <= 3