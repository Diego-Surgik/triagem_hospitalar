import customtkinter as ctk

# 1. Configurações da Janela
ctk.set_appearance_mode("dark")
janela = ctk.CTk()
janela.geometry("500x650") 
janela.title("Sistema de Triagem")

# 2. Título
titulo = ctk.CTkLabel(janela, text="Ficha de Triagem", font=("Arial", 20, "bold"))
titulo.pack(pady=20)


# --- NOVIDADE: OS CONTADORES DE FILA ---
fila_vermelha = 1
fila_amarela = 1
fila_verde = 1
fila_azul = 1

# --- NOVIDADE: OS VIGIAS DE TECLADO ---
def limitar_cpf(event):
    texto = entrada_cpf.get()
    if len(texto) > 11:
        entrada_cpf.delete(11, "end") # Apaga tudo que passar do 11º caractere

def limitar_idade(event):
    texto = entrada_idade.get()
    if len(texto) > 3:
        entrada_idade.delete(3, "end") # Apaga tudo que passar do 3º caracteres


# 3. Entradas de Texto 
entrada_nome = ctk.CTkEntry(janela, placeholder_text="Nome Completo", width=300)
entrada_nome.pack(pady=10)

entrada_cpf = ctk.CTkEntry(janela, placeholder_text="CPF (Apenas Números)", width=300)
entrada_cpf.pack(pady=10)

entrada_idade = ctk.CTkEntry(janela, placeholder_text="Idade", width=300)
entrada_idade.pack(pady=10)

entrada_cpf.bind("<KeyRelease>", limitar_cpf)
entrada_idade.bind("<KeyRelease>", limitar_idade)

# 4. Menus Suspensos
menu_plano = ctk.CTkOptionMenu(janela, values=["SUS", "Convênio", "Particular"], width=300)
menu_plano.set("Selecione o Plano de Saúde")
menu_plano.pack(pady=10)

menu_dor = ctk.CTkOptionMenu(janela, values=["Sem dor ou leve", "Moderada", "Intensa", "Extrema (Emergência)"], width=300)
menu_dor.set("Selecione o Nível de Dor")
menu_dor.pack(pady=10)

# --- O RESET DA TELA ---
def limpar_tela():
    # Apaga os textos (do caractere 0 até o final)
    entrada_nome.delete(0, "end")
    entrada_cpf.delete(0, "end")
    entrada_idade.delete(0, "end")
    
    # Reseta os menus para a mensagem original
    menu_plano.set("Selecione o Plano de Saúde")
    menu_dor.set("Selecione o Nível de Dor")
    
    # Limpa a mensagem gigante do resultado
    label_resultado.configure(text="")

# 5. O Cérebro (A Função)
def salvar_dados():
    nome = entrada_nome.get().title() 
    cpf = entrada_cpf.get() 
    idade_texto = entrada_idade.get() 
    plano = menu_plano.get()
    dor = menu_dor.get()
    
    # --- O LEÃO DE CHÁCARA (A Validação de Segurança) ---
    if len(cpf) != 11 or not cpf.isdigit():
        label_resultado.configure(text="ERRO: O CPF deve ter exatamente 11 números!", text_color="red")
        janela.after(3000, limpar_tela)
        return 
        
    if not idade_texto.isdigit() or int(idade_texto) > 120:
        label_resultado.configure(text="ERRO: Idade inválida (máximo 120 anos).", text_color="red")
        janela.after(3000, limpar_tela)
        return 

    idade = int(idade_texto)
    
    # Avisando a função para usar as memórias da fila!
    global fila_vermelha, fila_amarela, fila_verde, fila_azul
    
    # --- O PROTOCOLO DE MANCHESTER COM SENHAS ---
    if dor == "Extrema (Emergência)":
        classificacao = "🔴 SALA VERMELHA (Imediato)"
        cor_texto = "red"
        senha = f"V-{fila_vermelha:03d}" # Gera V-001
        fila_vermelha += 1               # Aumenta a fila para o próximo paciente (V-002)
        
    elif dor == "Intensa" or idade >= 65:
        classificacao = "🟡 SALA AMARELA (Urgência)"
        cor_texto = "yellow"
        senha = f"A-{fila_amarela:03d}"
        fila_amarela += 1
        
    elif dor == "Moderada":
        classificacao = "🟢 SALA VERDE (Pouco Urgente)"
        cor_texto = "green"
        senha = f"E-{fila_verde:03d}"
        fila_verde += 1
        
    else:
        classificacao = "🔵 SALA AZUL (Não Urgente)"
        cor_texto = "cyan"
        senha = f"Z-{fila_azul:03d}"
        fila_azul += 1
        
    # --- INJETANDO O RESULTADO NO TOTEM ---
    # Agora a senha aparece gigante na tela!
    texto_final = f"Paciente: {nome} | {idade} anos\n{classificacao}\n\nSUA SENHA: {senha}"
    label_resultado.configure(text=texto_final, text_color=cor_texto)

    # Salvando no Banco de Dados (Agora com a Senha incluída!)
    with open("historico_plantao.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Senha: {senha} | CPF: {cpf} | Nome: {nome} | Idade: {idade} | Plano: {plano} | Classificação: {classificacao}\n")
    # ... (código de salvar no arquivo historico_plantao.txt) ...

    # Agenda a função limpar_tela para rodar daqui a 5000 milissegundos (5 segundos)
    janela.after(5000, limpar_tela)

# 6. O Botão e o Rótulo 
botao_salvar = ctk.CTkButton(janela, text="Salvar Ficha", command=salvar_dados)
botao_salvar.pack(pady=30)

label_resultado = ctk.CTkLabel(janela, text="", font=("Arial", 16, "bold"))
label_resultado.pack(pady=10)

# 7. O Guarda de Trânsito
janela.mainloop()