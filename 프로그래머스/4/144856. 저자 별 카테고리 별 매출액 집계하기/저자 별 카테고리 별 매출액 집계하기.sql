select 
   a.author_id
 , (select z.author_name from author z where z.author_id = a.author_id)
 , a.category
 , sum(b.sales * a.price)
from book a, (
    select 
        book_id
    ,   sales
    from book_sales
    where to_char(sales_date, 'yyyy-mm-dd') like '2022-01%'
) b
where 1=1 
    and a.book_id = b.book_id
group by a.author_id, a.category
order by a.author_id, a.category desc