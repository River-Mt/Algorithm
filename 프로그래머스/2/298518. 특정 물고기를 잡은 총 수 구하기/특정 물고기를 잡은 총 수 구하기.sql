
select
    sum(a.FISH_COUNT) FISH_COUNT
from (
    select 
        b.fish_name
      , count(*) FISH_COUNT
    from fish_info a, fish_name_info b
    where a.fish_type = b.fish_type
    group by b.fish_name    
) a
where 1=1
    and a.fish_name = 'BASS'
    or a.fish_name = 'SNAPPER'