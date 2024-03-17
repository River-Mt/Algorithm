select 
    a.product_id,
    a.product_name,
    a.price * b.amount total_sales
from food_product a, (
    select
        product_id,
        sum(amount) amount
    from food_order
    where 1=1
        and to_char(produce_date, 'yyyy-mm') = '2022-05'
    group by product_id    
) b
where a.product_id = b.product_id
order by total_sales desc, a.product_id