UPDATE 
    estados
SET 
    nome = 'Maranhão'
WHERE sigla = 'MA'

SELECT e.NOME FROM estados e WHERE SIGLA = 'MA'

UPDATE estados
SET 
    nome = 'Paraná',
    populacao = 11.32
WHERE sigla = 'PR';