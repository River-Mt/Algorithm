select
    a.item_id,
    a.item_name
from item_info a
where a.item_id in(
    select 
        item_id
    from item_tree
    where parent_item_id is null
)
order by a.item_id