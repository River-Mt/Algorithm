select  
    count(*) FISH_COUNT
  , max(a.length) MAX_LENGTH
  , a.fish_type FISH_TYPE
from (
    select 
        fish_type
      , case
            when length is null then 0
            when length <= 10 then 10 
            else length
        end length
    from fish_info) a
group by a.fish_type 
having avg(a.length) >= 33
order by a.fish_type


