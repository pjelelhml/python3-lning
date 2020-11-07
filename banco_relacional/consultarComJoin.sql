select
    e.nome as Estado,
    c.nome as Cidade,
    e.regiao
from
    estados e,
    cidades c
where
    e.id = c.estado_id;

select
    e.nome as Estado,
    c.nome as Cidade,
    e.regiao
from
    estados e
    inner join cidades c on e.id = c.estado_id

