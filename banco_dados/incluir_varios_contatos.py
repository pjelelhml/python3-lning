from db import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Lucas', '12343-4321'),
    ('Bia', '31343-4321'),
    ('Gui', '99343-4321'),
    ('Beca', '92343-4321'),
    ('Pedro', '22343-4321'),
    ('Julia', '32343-4321'),
    ('Leticia', '22343-4321'),
    ('Ronaldo', '14343-4321'),
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'foram incluídos {cursor.rowcount} registros!')
