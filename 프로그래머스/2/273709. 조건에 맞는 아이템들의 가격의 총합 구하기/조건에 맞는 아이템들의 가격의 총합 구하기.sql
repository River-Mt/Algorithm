select distinct sum(price) over(partition by rarity) as TOTAL_PRICE
from item_info 
where rarity = 'LEGEND'
