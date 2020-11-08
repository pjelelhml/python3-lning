from db import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = 'DELETE FROM contatos WHERE nome = %s'
args = ('Lucas',)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'{cursor.rowcount} registros deletado(s)')
    