import tkinter as tk
from tkinter import messagebox
from datetime import datetime  
from login import verificar_login
from sistema import cadastrar_agendamento, listar_agendamentos
from tkinter import ttk

# ================= TELA PRINCIPAL =================
print("versao nova")

def tela_principal():
    login_window.destroy()

    app = tk.Tk()
    app.title("Sistema de Agendamentos")
    app.geometry("500x450")
    app.configure(bg="#f2f2f2")

    titulo = tk.Label(app, text="Sistema de Agendamentos", font=("Arial", 16, "bold"), bg="#f2f2f2")
    titulo.pack(pady=10)

    frame = tk.Frame(app, bg="#f2f2f2")
    frame.pack(pady=10)

    tk.Label(frame, text="Nome do Cliente:", bg="#f2f2f2").grid(row=0, column=0, sticky="e")
    entry_nome = tk.Entry(frame, width=30)
    entry_nome.grid(row=0, column=1, pady=5)

    tk.Label(frame, text="Email:", bg="#f2f2f2").grid(row=1, column=0, sticky="e")
    entry_email = tk.Entry(frame, width=30)
    entry_email.grid(row=1, column=1, pady=5)

    tk.Label(frame, text="Telefone:", bg="#f2f2f2").grid(row=2, column=0, sticky="e")
    entry_telefone = tk.Entry(frame, width=30)
    entry_telefone.grid(row=2, column=1, pady=5)

    tk.Label(frame, text="Serviço:", bg="#f2f2f2").grid(row=3, column=0, sticky="e")
    entry_servico = tk.Entry(frame, width=30)
    entry_servico.grid(row=3, column=1, pady=5)
    
    tk.Label(frame, text="Data (AAAA-MM-DD):", bg="#f2f2f2").grid(row=4, column=0, sticky="e")
    entry_data = tk.Entry(frame, width=30)
    entry_data.grid(row=4, column=1, pady=5)

    tk.Label(frame, text="Hora (HH:MM):", bg="#f2f2f2").grid(row=5, column=0, sticky="e")
    entry_hora = tk.Entry(frame, width=30)
    entry_hora.grid(row=5, column=1, pady=5)

    #  FUNÇÃO LIMPAR CAMPOS
    def limpar():
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        entry_servico.delete(0, tk.END)
        entry_data.delete(0, tk.END)
        entry_hora.delete(0, tk.END)

    def abrir_lista():
        janela = tk.Toplevel(app)
        janela.title("Agendamentos")
        janela.geometry("800x450")

        tk.Label(janela, text="Filtrar por data (AAAA-MM-DD):").pack(pady=5)
        entry_filtro = tk.Entry(janela)
        entry_filtro.pack()

        colunas = ("Nome", "Email", "Telefone", "Serviço", "Data", "Hora")
        tabela = ttk.Treeview(janela, columns=colunas, show="headings")

        for col in colunas:
            tabela.heading(col, text=col)
            tabela.column(col, width=120)

        tabela.pack(fill="both", expand=True, pady=10)

        # CARREGA NA TELA
        def carregar_tabela(dados):
            tabela.delete(*tabela.get_children())
            for linha in dados:
                tabela.insert("", tk.END, values=linha)
        # FILTRO
        def filtrar():
            data = entry_filtro.get().strip()
            if data:
                dados = listar_agendamentos(data)
            else:
                dados = listar_agendamentos()
            carregar_tabela(dados)
        tk.Button(janela, text="Filtrar", command=filtrar).pack(pady=5)

        # MOSTRA TODOS AO ABRIR
        carregar_tabela(listar_agendamentos())

    #  SALVAR COM VALIDAÇÃO
    def salvar():
        nome = entry_nome.get().strip()
        email = entry_email.get().strip()
        telefone = entry_telefone.get().strip()
        servico = entry_servico.get().strip()
        data = entry_data.get().strip()
        hora = entry_hora.get().strip()
        
        if not nome or not servico or not data or not hora:
            messagebox.showwarning("Atenção", "Preencha os campos obrigatórios!")
            return

        try:
            datetime.strptime(data, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Erro", "Data inválida! Use AAAA-MM-DD")
            return
        
        try:
            datetime.strptime(hora, "%H:%M")
        except ValueError:
            messagebox.showerror("Erro", "Hora inválida! Use HH:MM")
            return
        
        cadastrar_agendamento(nome, email, telefone, servico, data, hora)
        messagebox.showinfo("Sucesso", "Agendamento cadastrado!")

        limpar()

    # BOTÕES
    tk.Button(app, text="Cadastrar", width=20, bg="#4CAF50", fg="white", command=salvar).pack(pady=5)
    tk.Button(app, text="Exibir Agendamentos", width=20, command=abrir_lista).pack(pady=5)
    tk.Button(app, text="Sair", width=20, bg="red", fg="white", command=app.destroy).pack(pady=10)

    app.mainloop()


# ================= LOGIN =================
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x220")

tk.Label(login_window, text="Usuário").pack(pady=5)
entry_user = tk.Entry(login_window)
entry_user.pack()

tk.Label(login_window, text="Senha").pack(pady=5)
entry_pass = tk.Entry(login_window, show="*")
entry_pass.pack()

def logar():
    if verificar_login(entry_user.get(), entry_pass.get()):
        tela_principal()
    else:
        messagebox.showerror("Erro", "Login inválido!")

tk.Button(login_window, text="Entrar", command=logar).pack(pady=10)

login_window.mainloop()