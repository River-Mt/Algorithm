select 
   a.author_id
 , c.author_name
 , a.category
 , sum(b.sales * a.price)
from book a, author c,(
    select 
        book_id
    ,   sales
    from book_sales
    where to_char(sales_date, 'yyyy-mm-dd') like '2022-01%'
) b
where 1=1 
    and a.author_id = c.author_id
    and a.book_id = b.book_id
group by a.author_id, c.author_name, a.category
order by a.author_id, a.category desc