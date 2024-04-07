select
    tt.id as ID,
    case 
        when tt.rate <= 0.25 then 'CRITICAL'
        when tt.rate <= 0.5 then 'HIGH'
        when tt.rate <= 0.75 then 'MEDIUM'
        else 'LOW'
    end as COLONY_NAME
from (
    select
        t.ord,
        t.ord / (select count(*) from ECOLI_DATA) as rate,
        t.id,
        t.size_of_colony
    from (
        select 
            row_number() over(order by e.size_of_colony desc) as ord,
            e.id,
            e.size_of_colony
        from ECOLI_DATA e
    ) t
) tt
order by ID