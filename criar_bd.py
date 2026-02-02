import sqlite3

conn = sqlite3.connect("agendamentos.db")
cursor = conn.cursor()

# tabela Usuarios
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT UNIQUE,
    senha TEXT
)
""")

# tabela Agendamentos
cursor.execute("""
CREATE TABLE IF NOT EXISTS agendamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_cliente TEXT NOT NULL,
    email TEXT,
    telefone TEXT,
    servico TEXT NOT NULL,
    data TEXT NOT NULL,
    hora TEXT NOT NULL
)
""")

cursor.execute("INSERT OR IGNORE INTO usuarios (usuario, senha) VALUES ('admin', '123')")


conn.commit()
conn.close()

print("Banco atualizado com novos campos!")