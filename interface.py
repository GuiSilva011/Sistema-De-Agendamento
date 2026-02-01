import tkinter as tk
from tkinter import messagebox
from datetime import datetime   # ← AQUI
from login import verificar_login
from sistema import cadastrar_agendamento, buscar_por_data

# ================= TELA PRINCIPAL =================
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

    tk.Label(frame, text="Serviço:", bg="#f2f2f2").grid(row=1, column=0, sticky="e")
    entry_servico = tk.Entry(frame, width=30)
    entry_servico.grid(row=1, column=1, pady=5)

    tk.Label(frame, text="Data (AAAA-MM-DD):", bg="#f2f2f2").grid(row=2, column=0, sticky="e")
    entry_data = tk.Entry(frame, width=30)
    entry_data.grid(row=2, column=1, pady=5)

    tk.Label(frame, text="Hora (HH:MM):", bg="#f2f2f2").grid(row=3, column=0, sticky="e")
    entry_hora = tk.Entry(frame, width=30)
    entry_hora.grid(row=3, column=1, pady=5)

    #  FUNÇÃO LIMPAR CAMPOS
    def limpar():
        entry_nome.delete(0, tk.END)
        entry_servico.delete(0, tk.END)
        entry_data.delete(0, tk.END)
        entry_hora.delete(0, tk.END)

    #  SALVAR COM VALIDAÇÃO
    def salvar():
        nome = entry_nome.get().strip()
        servico = entry_servico.get().strip()
        data = entry_data.get().strip()
        hora = entry_hora.get().strip()

        if not nome or not servico or not data or not hora:
            messagebox.showwarning("Atenção", "Todos os campos são obrigatórios!")
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
        
        cadastrar_agendamento(nome, servico, data, hora)
        messagebox.showinfo("Sucesso", "Agendamento cadastrado!")

        entry_nome.delete(0, tk.END)
        entry_servico.delete(0, tk.END)
        entry_data.delete(0, tk.END)
        entry_hora.delete(0, tk.END)
        entry_nome.focus()

    #  BUSCAR
    def buscar():
        data = entry_data.get()
        if not data:
            messagebox.showwarning("Atenção", "Informe a data!")
            return

        dados = buscar_por_data(data)
        texto = "\n".join([f"{n} - {s} - {h}" for n, s, h in dados])
        messagebox.showinfo("Resultados", texto if texto else "Nenhum agendamento.")

    # BOTÕES
    tk.Button(app, text="Cadastrar", width=20, bg="#4CAF50", fg="white", command=salvar).pack(pady=5)
    tk.Button(app, text="Buscar por Data", width=20, command=buscar).pack(pady=5)
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