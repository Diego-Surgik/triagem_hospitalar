import customtkinter as ctk

# 1. Configurações da Janela
ctk.set_appearance_mode("dark")
janela = ctk.CTk()
janela.geometry("500x600")
janela.title("Sistema de Triagem")

# 2. Título
titulo = ctk.CTkLabel(janela, text="Ficha de Triagem", font=("Arial", 20))
titulo.pack(pady=20)

# 3. Entradas de Texto
entrada_nome = ctk.CTkEntry(janela, placeholder_text="Nome do Paciente", width=300)
entrada_nome.pack(pady=10)

entrada_idade = ctk.CTkEntry(janela, placeholder_text="Idade do Paciente", width=300)
entrada_idade.pack(pady=10)

# 4. Menus Suspensos
menu_plano = ctk.CTkOptionMenu(janela, values=["SUS", "Convênio", "Particular"], width=300)
menu_plano.set("Selecione o Plano de Saúde")
menu_plano.pack(pady=10)

menu_dor = ctk.CTkOptionMenu(janela, values=["Sem dor ou leve", "Moderada", "Intensa", "Extrema (Emergência)"], width=300)
menu_dor.set("Selecione o Nível de Dor")
menu_dor.pack(pady=10)

# 5. O Cérebro (A Função)
def salvar_dados():
    nome = entrada_nome.get()
    idade_texto = entrada_idade.get() # Puxa como texto
    plano = menu_plano.get()
    dor = menu_dor.get()
    
    # Converte para número para a matemática funcionar
    idade = int(idade_texto)
    
    # --- A INTELIGÊNCIA CLÍNICA ---
    if dor == "Extrema (Emergência)":
        classificacao = "EMERGÊNCIA (Atendimento Imediato)"
    elif dor == "Intensa" or idade >= 65:
        classificacao = "PRIORIDADE (Aguardar Sala Amarela)"
    else:
        classificacao = "NORMAL (Aguardar Sala Verde)"
        
    # --- INJETANDO O RESULTADO NA JANELA ---
    texto_final = f"Paciente: {nome} | {idade} anos\n>>> {classificacao} <<<"
    
    label_resultado.configure(text=texto_final, text_color="yellow")
        
    # PASSO 2: Injetando o resultado na janela (e colocando uma cor de destaque!)
    texto_final = f"Paciente: {nome} | {idade} anos\n>>> {classificacao} <<<"
    
    label_resultado.configure(text=texto_final, text_color="yellow")

# 6. O Botão (que chama o cérebro)
botao_salvar = ctk.CTkButton(janela, text="Salvar Ficha", command=salvar_dados)
botao_salvar.pack(pady=30)

botao_salvar = ctk.CTkButton(janela, text="Salvar Ficha", command=salvar_dados)
botao_salvar.pack(pady=30)

# PASSO 1: A etiqueta que vai mostrar o resultado (nasce com o texto vazio "")
label_resultado = ctk.CTkLabel(janela, text="", font=("Arial", 16, "bold"))
label_resultado.pack(pady=10)

janela.mainloop()

# 7. O Guarda de Trânsito
janela.mainloop()
