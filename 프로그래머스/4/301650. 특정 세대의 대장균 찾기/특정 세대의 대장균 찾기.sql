

select 
    b.id as ID
from ecoli_data b
where b.parent_id in (
    select 
        a.id
    from ecoli_data a
    where a.parent_id in (
        select id
        from ecoli_data
        where parent_id is null
    )
)
order by ID

