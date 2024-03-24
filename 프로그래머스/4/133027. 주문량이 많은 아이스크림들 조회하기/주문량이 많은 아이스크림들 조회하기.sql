select a.flavor
from 
   (select flavor, sum(total_order) total from first_half group by flavor) a
 , (select flavor, sum(total_order) total from july group by flavor) b
where a.flavor = b.flavor
group by a.flavor
order by sum(a.total + b.total) desc fetch next 3 rows only
