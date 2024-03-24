select 
    id ID
  , ifnull(length, 0) LENGTH
from fish_info
order by length desc
limit 10