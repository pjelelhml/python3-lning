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
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        for contato in contatos:
            print(f'{contato["grupo"]}: {contato["contato"]}')
