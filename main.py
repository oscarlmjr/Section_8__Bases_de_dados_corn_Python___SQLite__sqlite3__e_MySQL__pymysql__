import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CUIDADO: fazendo delete sem where
cursor.execute(
	f'DELETE FROM {TABLE_NAME}'
)
connection.execute(
	f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# Cria a tabela
cursor.execute(
	f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
	'('
	'id INTEGER PRIMARY KEY AUTOINCREMENT,'
	'name TEXT,'
	'weight REAL'
	')'
)
connection.commit()

# Registrar valores nas colunas das tabela
# CUIDADO: sql injection
sql = (
	f'INSERT INTO {TABLE_NAME} '
	'(name, weight) '
	'VALUES '
	'(?, ?)'   #bindings, placeholders, parâmetros, etc.
)
# cursor.execute(sql, ['joana', 4])
cursor.executemany(
	sql, 
	(
	('joana', 4), ('Luiz', 5)
	)
	)
connection.commit()
print(sql)

cursor.close()
connection.close()
