import customtkinter as ctk

# 1. Configurações da Janela Principal
ctk.set_appearance_mode("dark")
janela = ctk.CTk()
janela.geometry("500x700")
janela.title("Totem Touch")

# ==========================================
# MOTOR DE TRANSIÇÃO
# ==========================================
def ir_para_tela_nome():
    tela_inicio.pack_forget() 
    tela_nome.pack(fill="both", expand=True) 

def ir_para_tela_idade():
    tela_nome.pack_forget() 
    tela_idade.pack(fill="both", expand=True) 

def ir_para_tela_cpf():
    tela_idade.pack_forget() 
    tela_cpf.pack(fill="both", expand=True) 

def ir_para_tela_plano():
    tela_cpf.pack_forget() 
    tela_plano.pack(fill="both", expand=True) 

def ir_para_tela_dor():
    tela_plano.pack_forget() 
    tela_dor.pack(fill="both", expand=True) 

def ir_para_tela_resultado():
    tela_dor.pack_forget() 
    tela_resultado.pack(fill="both", expand=True) 

# ==========================================
# TELA 1: PRONTO-ATENDIMENTO
# ==========================================
tela_inicio = ctk.CTkFrame(janela, fg_color="transparent")
tela_inicio.pack(fill="both", expand=True)

titulo_inicio = ctk.CTkLabel(tela_inicio, text="Bem-vindo ao Hospital", font=("Arial", 28, "bold"))
titulo_inicio.pack(pady=50)

botao_iniciar = ctk.CTkButton(tela_inicio, text="Pronto-Atendimento", font=("Arial", 20, "bold"), height=80, width=300, command=ir_para_tela_nome)
botao_iniciar.pack(pady=50)

# ==========================================
# TELA 2: NOME DO PACIENTE
# ==========================================
tela_nome = ctk.CTkFrame(janela, fg_color="transparent")

titulo_nome = ctk.CTkLabel(tela_nome, text="Qual o seu nome?", font=("Arial", 24, "bold"))
titulo_nome.pack(pady=(30, 10))

entrada_nome = ctk.CTkEntry(tela_nome, font=("Arial", 24), height=50, width=450, justify="center")
entrada_nome.pack(pady=10)

def digitar_nome(letra):
    entrada_nome.insert("end", letra)

def apagar_letra_nome():
    texto_atual = entrada_nome.get()
    if texto_atual: 
        entrada_nome.delete(0, "end")
        entrada_nome.insert(0, texto_atual[:-1])
        
def espaco_nome():
    entrada_nome.insert("end", " ")

frame_teclado_nome = ctk.CTkFrame(tela_nome, fg_color="transparent")
frame_teclado_nome.pack(pady=20)

linhas_teclado = [
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
    ["Z", "X", "C", "V", "B", "N", "M"]
]

for i, linha in enumerate(linhas_teclado):
    linha_frame = ctk.CTkFrame(frame_teclado_nome, fg_color="transparent")
    linha_frame.pack(pady=2)
    for letra in linha:
        ctk.CTkButton(linha_frame, text=letra, font=("Arial", 18, "bold"), width=40, height=50, 
                      command=lambda l=letra: digitar_nome(l)).pack(side="left", padx=2)

frame_controles = ctk.CTkFrame(frame_teclado_nome, fg_color="transparent")
frame_controles.pack(pady=5)

ctk.CTkButton(frame_controles, text="ESPAÇO", font=("Arial", 16, "bold"), width=250, height=50, command=espaco_nome).pack(side="left", padx=5)
ctk.CTkButton(frame_controles, text="<-- Apagar", font=("Arial", 16, "bold"), width=120, height=50, fg_color="#E67E22", hover_color="#CA6F1E", command=apagar_letra_nome).pack(side="left", padx=5)

botao_avancar_nome = ctk.CTkButton(tela_nome, text="Avançar", font=("Arial", 20, "bold"), height=50, width=250, command=ir_para_tela_idade)
botao_avancar_nome.pack(pady=30)

# ==========================================
# TELA 3: IDADE
# ==========================================
tela_idade = ctk.CTkFrame(janela, fg_color="transparent")

titulo_idade = ctk.CTkLabel(tela_idade, text="Qual a sua idade?", font=("Arial", 24, "bold"))
titulo_idade.pack(pady=(30, 10))

entrada_idade = ctk.CTkEntry(tela_idade, font=("Arial", 30), height=50, width=150, justify="center")
entrada_idade.pack(pady=10)

def digitar_idade(numero):
    texto_atual = entrada_idade.get()
    if len(texto_atual) < 3:  
        entrada_idade.insert("end", numero)

def apagar_ultimo_idade():
    texto_atual = entrada_idade.get()
    entrada_idade.delete(0, "end")
    entrada_idade.insert(0, texto_atual[:-1]) 

frame_teclado_idade = ctk.CTkFrame(tela_idade, fg_color="transparent")
frame_teclado_idade.pack(pady=20)

for i, numeros in enumerate([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]):
    for j, num in enumerate(numeros):
        ctk.CTkButton(frame_teclado_idade, text=num, font=("Arial", 24), width=80, height=80, command=lambda n=num: digitar_idade(n)).grid(row=i, column=j, padx=5, pady=5)

ctk.CTkButton(frame_teclado_idade, text="Limpar", font=("Arial", 16, "bold"), width=80, height=80, fg_color="#C0392B", hover_color="#922B21", command=lambda: entrada_idade.delete(0, "end")).grid(row=3, column=0, padx=5, pady=5)
ctk.CTkButton(frame_teclado_idade, text="0", font=("Arial", 24), width=80, height=80, command=lambda: digitar_idade("0")).grid(row=3, column=1, padx=5, pady=5)
ctk.CTkButton(frame_teclado_idade, text="<--", font=("Arial", 20, "bold"), width=80, height=80, fg_color="#E67E22", hover_color="#CA6F1E", command=apagar_ultimo_idade).grid(row=3, column=2, padx=5, pady=5)

botao_avancar_idade = ctk.CTkButton(tela_idade, text="Avançar", font=("Arial", 20, "bold"), height=50, width=250, command=ir_para_tela_cpf)
botao_avancar_idade.pack(pady=20)

# ==========================================
# TELA 4: CPF
# ==========================================
tela_cpf = ctk.CTkFrame(janela, fg_color="transparent")

titulo_cpf = ctk.CTkLabel(tela_cpf, text="Digite seu CPF", font=("Arial", 24, "bold"))
titulo_cpf.pack(pady=(30, 10))

entrada_cpf = ctk.CTkEntry(tela_cpf, font=("Arial", 30), height=50, width=300, justify="center")
entrada_cpf.pack(pady=10)

def digitar_cpf(numero):
    texto_atual = entrada_cpf.get()
    if len(texto_atual) < 11:  
        entrada_cpf.insert("end", numero)

def apagar_ultimo_cpf():
    texto_atual = entrada_cpf.get()
    entrada_cpf.delete(0, "end")
    entrada_cpf.insert(0, texto_atual[:-1])

frame_teclado_cpf = ctk.CTkFrame(tela_cpf, fg_color="transparent")
frame_teclado_cpf.pack(pady=20)

for i, numeros in enumerate([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]):
    for j, num in enumerate(numeros):
        ctk.CTkButton(frame_teclado_cpf, text=num, font=("Arial", 24), width=80, height=80, command=lambda n=num: digitar_cpf(n)).grid(row=i, column=j, padx=5, pady=5)

ctk.CTkButton(frame_teclado_cpf, text="Limpar", font=("Arial", 16, "bold"), width=80, height=80, fg_color="#C0392B", hover_color="#922B21", command=lambda: entrada_cpf.delete(0, "end")).grid(row=3, column=0, padx=5, pady=5)
ctk.CTkButton(frame_teclado_cpf, text="0", font=("Arial", 24), width=80, height=80, command=lambda: digitar_cpf("0")).grid(row=3, column=1, padx=5, pady=5)
ctk.CTkButton(frame_teclado_cpf, text="<--", font=("Arial", 20, "bold"), width=80, height=80, fg_color="#E67E22", hover_color="#CA6F1E", command=apagar_ultimo_cpf).grid(row=3, column=2, padx=5, pady=5)

botao_avancar_cpf = ctk.CTkButton(tela_cpf, text="Avançar", font=("Arial", 20, "bold"), height=50, width=250, command=ir_para_tela_plano)
botao_avancar_cpf.pack(pady=20)

# ==========================================
# TELA 5: PLANO DE SAÚDE
# ==========================================
tela_plano = ctk.CTkFrame(janela, fg_color="transparent")

titulo_plano = ctk.CTkLabel(tela_plano, text="Selecione o seu Plano", font=("Arial", 24, "bold"))
titulo_plano.pack(pady=(40, 20))

plano_selecionado = ctk.StringVar(value="") 

def escolher_plano(plano):
    plano_selecionado.set(plano) 
    ir_para_tela_dor()           

frame_botoes_plano = ctk.CTkFrame(tela_plano, fg_color="transparent")
frame_botoes_plano.pack(pady=10)

def criar_botao(nome, linha, coluna):
    ctk.CTkButton(frame_botoes_plano, text=nome, font=("Arial", 18, "bold"), 
                  height=65, width=220, command=lambda n=nome: escolher_plano(n)).grid(row=linha, column=coluna, padx=10, pady=8)

criar_botao("SUS", 0, 0)
criar_botao("Unimed", 0, 1)
criar_botao("Amil", 1, 0)
criar_botao("Bradesco Saúde", 1, 1)
criar_botao("SulAmérica", 2, 0)
criar_botao("Hapvida", 2, 1)
criar_botao("NotreDame", 3, 0)
criar_botao("Prevent Senior", 3, 1)
criar_botao("Outros Convênios", 4, 0)
criar_botao("Particular", 4, 1)

# ==========================================
# TELA 6: NÍVEL DE DOR
# ==========================================
tela_dor = ctk.CTkFrame(janela, fg_color="transparent")

titulo_dor = ctk.CTkLabel(tela_dor, text="Como você descreve sua dor agora?", font=("Arial", 24, "bold"))
titulo_dor.pack(pady=(50, 40))

dor_selecionada = ctk.StringVar(value="")

def escolher_dor(nivel):
    dor_selecionada.set(nivel)
    ir_para_tela_resultado()
    gerar_resultado() # <--- A função que vai processar tudo!

btn_extrema = ctk.CTkButton(tela_dor, text="Dor Extrema (Insuportável)", font=("Arial", 22, "bold"), height=75, width=400, 
                            fg_color="#C0392B", hover_color="#922B21", command=lambda: escolher_dor("Extrema"))
btn_extrema.pack(pady=15)

btn_intensa = ctk.CTkButton(tela_dor, text="Dor Intensa (Forte)", font=("Arial", 22, "bold"), height=75, width=400, 
                            fg_color="#D35400", hover_color="#A04000", command=lambda: escolher_dor("Intensa"))
btn_intensa.pack(pady=15)

btn_moderada = ctk.CTkButton(tela_dor, text="Dor Moderada", font=("Arial", 22, "bold"), height=75, width=400, 
                             fg_color="#27AE60", hover_color="#1E8449", command=lambda: escolher_dor("Moderada"))
btn_moderada.pack(pady=15)

btn_leve = ctk.CTkButton(tela_dor, text="Dor Leve ou Nenhuma", font=("Arial", 22, "bold"), height=75, width=400, 
                         fg_color="#2980B9", hover_color="#1A5276", command=lambda: escolher_dor("Leve"))
btn_leve.pack(pady=15)

# ==========================================
# TELA 7: RESULTADO
# ==========================================

tela_resultado = ctk.CTkFrame(janela, fg_color="transparent")

titulo_resultado = ctk.CTkLabel(tela_resultado, text="Classificação Concluída!", font=("Arial", 28, "bold"))
titulo_resultado.pack(pady=(50, 20))

# Espaços onde o Python vai injetar os dados gerados
label_dados = ctk.CTkLabel(tela_resultado, text="", font=("Arial", 20))
label_dados.pack(pady=10)

label_senha = ctk.CTkLabel(tela_resultado, text="", font=("Arial", 36, "bold"))
label_senha.pack(pady=30)

# --- AS MEMÓRIAS DA FILA ---
fila_vermelha = 1
fila_amarela = 1
fila_verde = 1
fila_azul = 1

def resetar_totem():
    # Limpa as caixas de texto para o próximo paciente
    entrada_nome.delete(0, "end")
    entrada_idade.delete(0, "end")
    entrada_cpf.delete(0, "end")
    
    # Esconde o resultado e volta para a Tela 1
    tela_resultado.pack_forget()
    tela_inicio.pack(fill="both", expand=True)

def gerar_resultado():
    global fila_vermelha, fila_amarela, fila_verde, fila_azul
    
    # 1. Puxando as informações das telas anteriores
    nome = entrada_nome.get()
    idade_texto = entrada_idade.get()
    cpf = entrada_cpf.get()
    plano = plano_selecionado.get()
    dor = dor_selecionada.get()
    
    # Prevenção de erro caso a idade fique vazia
    idade = int(idade_texto) if idade_texto.isdigit() else 0

    # 2. O Protocolo de Manchester
    if dor == "Extrema":
        classificacao = "🔴 SALA VERMELHA (Imediato)"
        cor = "#C0392B"
        senha = f"V-{fila_vermelha:03d}"
        fila_vermelha += 1
        
    elif dor == "Intensa" or idade >= 65:
        classificacao = "🟡 SALA AMARELA (Urgência)"
        cor = "#D35400"
        senha = f"A-{fila_amarela:03d}"
        fila_amarela += 1
        
    elif dor == "Moderada":
        classificacao = "🟢 SALA VERDE (Pouco Urgente)"
        cor = "#27AE60"
        senha = f"E-{fila_verde:03d}"
        fila_verde += 1
        
    else:
        classificacao = "🔵 SALA AZUL (Não Urgente)"
        cor = "#2980B9"
        senha = f"Z-{fila_azul:03d}"
        fila_azul += 1

    # 3. Injetando tudo na Tela 7
    texto_paciente = f"Paciente: {nome}\nIdade: {idade} anos | CPF: {cpf}\nPlano: {plano}"
    label_dados.configure(text=texto_paciente)
    
    texto_final = f"{classificacao}\n\nSUA SENHA:\n{senha}"
    label_senha.configure(text=texto_final, text_color=cor)

    # 4. Salvando no Banco de Dados
    with open("historico_plantao.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Senha: {senha} | Nome: {nome} | Idade: {idade} | CPF: {cpf} | Plano: {plano} | {classificacao}\n")

    # 5. O Reset Automático (O Python conta até 6 segundos e limpa o totem)
    janela.after(6000, resetar_totem)

# O Comando que mantém a janela aberta (DEVE ser sempre a última linha!)
janela.mainloop()

janela.mainloop()