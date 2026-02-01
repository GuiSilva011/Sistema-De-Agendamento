from banco import conectar

def cadastrar_agendamento(nome, servico, data, hora):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO agendamentos (nome_cliente, servico, data, hora)
    VALUES (?, ?, ?, ?)
    """, (nome, servico, data, hora))

    conn.commit()   # ← ISSO É O QUE SALVA DE VERDADE
    conn.close()

def buscar_por_data(data):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT nome_cliente, servico, hora FROM agendamentos WHERE data=?", (data,))
    dados = cursor.fetchall()

    conn.close()
    return dados