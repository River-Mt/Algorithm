select 
    a.id AS ID,
    (select z.fish_name from fish_name_info z where a.fish_type = z.fish_type) AS FISH_NAME,
    a.length AS LENGTH
from fish_info a
where (fish_type, length) in (
    select
        fish_type,
        max(length)
    from fish_info
    group by fish_type
)
order by a.id


