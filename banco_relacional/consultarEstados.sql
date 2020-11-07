SELECT * FROM estados

SELECT nome, sigla FROM estados
SELECT sigla, nome FROM estados

SELECT
    nome as 'Nome do Estado', sigla 
FROM 
    estados
WHERE 
    regiao = 'Sul';

SELECT
    NOME, REGIAO 
FROM 
    estados 
WHERE 
    POPULACAO >= 10 
ORDER BY POPULACAO DESC

