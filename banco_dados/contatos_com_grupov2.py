from collections import defaultdict
from db import nova_conexao
from mysql.connector.errors import ProgrammingError


sql = """
    SELECT
        grupos.descricao as grupo,
        contatos.nome as contato
    from contatos
    INNER JOIN grupos on contatos.grupo_id = grupos.id
    order by grupo, contato
"""

with nova_conexao() as conexao:
    try:
        # não funciona em todos os pacotes da pep249
        # o dictionary=True -> facilita pq transforma a tupla em dicionario
        cursor = conexao.cursor(dictionary=True)
        try:
            cursor.execute(sql)
            contatos = cursor.fetchall()
        finally:
            cursor.close()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        agrupados = defaultdict(list)
        for contato in contatos:
            for contato in contatos:
                agrupados[contato['grupo']].append(contato['contato'])

        print(agrupados)
