import sqlite3

conn = sqlite3.connect("agendamentos.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT UNIQUE,
    senha TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS agendamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_cliente TEXT,
    servico TEXT,
    data TEXT,
    hora TEXT
)
""")

cursor.execute("INSERT OR IGNORE INTO usuarios (usuario, senha) VALUES ('admin', '123')")

conn.commit()
conn.close()

print("Banco criado com sucesso!")