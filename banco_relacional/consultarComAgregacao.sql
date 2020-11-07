select
    regiao 'Região',
    sum(populacao) Total
from estados
group by regiao
order by Total desc

select
    sum(populacao) Total
from estados

select
    avg(populacao) Total
from estados