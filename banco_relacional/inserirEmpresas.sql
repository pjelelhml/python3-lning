insert into empresas
    (nome, cnpj)
values
    ('Bradesco', 1231231231243),
    ('Vale', 594386565656),
    ('Cielo', 03594305946546);

alter table empresas modify cnpj VARCHAR(15);

desc empresas;

insert into empresas_unidades
    (empresa_id, cidade_id, sede)
values
    (1, 1, 1),
    (1, 2, 0),
    (2, 1, 0),
    (2, 2, 1);