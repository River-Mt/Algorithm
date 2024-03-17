select
    count(1) as FISH_COUNT,
    (select z.fish_name from fish_name_info z where a.fish_type = z.fish_type)as FISH_NAME
from fish_info a
group by a.fish_type
order by FISH_COUNT desc