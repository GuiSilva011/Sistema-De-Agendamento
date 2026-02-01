from banco import conectar

def verificar_login(usuario, senha):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE usuario=? AND senha=?", (usuario, senha))
    user = cursor.fetchone()

    conn.close()
    return user is not None