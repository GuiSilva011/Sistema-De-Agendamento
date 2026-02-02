from banco import conectar

def cadastrar_agendamento(nome, email, telefone, servico, data, hora):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO agendamentos (nome_cliente, email, telefone, servico, data, hora)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, email, telefone, servico, data, hora))

    conn.commit()
    conn.close()

def buscar_por_data(data):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, nome_cliente, servico, hora 
    FROM agendamentos WHERE data=?
    """, (data,))
    
    dados = cursor.fetchall()
    conn.close()
    return dados

def listar_agendamentos(data=None):
    conn = conectar()
    cursor = conn.cursor()

    if data:
        cursor.execute("""
            SELECT nome_cliente, email, telefone, servico, data, hora
            FROM agendamentos
            WHERE data = ?
            ORDER BY id ASC
        """, (data,))
    else:
        cursor.execute("""
            SELECT nome_cliente, email, telefone, servico, data, hora
            FROM agendamentos
            ORDER BY id ASC
        """)

    dados = cursor.fetchall()
    conn.close()
    return dados