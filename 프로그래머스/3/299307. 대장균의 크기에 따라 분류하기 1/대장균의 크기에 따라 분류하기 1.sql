select 
    E.id AS ID,
    case 
        when E.size_of_colony > 1000 then 'HIGH'
        when E.size_of_colony > 100 then 'MEDIUM'
        else 'LOW'
    end AS SIZE
from ECOLI_DATA E
order by ID



