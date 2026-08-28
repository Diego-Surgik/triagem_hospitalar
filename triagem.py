pacientes_atendidos =[]
plantao = "sim"
while plantao == "sim":
    nome_do_paciente = input("Digite o nome do paciente:") .title() .strip()
    idade = int(input("Digite a idade do paciente:")) 
    dor = int(input("Digite o nível de dor do paciente (0 a 10): "))

    paciente_atual ={
     "nome" : nome_do_paciente,
     "idade" : idade,
        "dor" : dor
    }
    pacientes_atendidos.append(paciente_atual)
    print(f"Paciente: {nome_do_paciente} idade: {idade} anos")



    if dor >= 8:
        print("Classificação: EMERGENCIA")
    elif idade >= 65:
        print("Classificação: PRIORIDADE")
    else:
     print("Classificação: NORMAL")

    plantao = input("Deseja registrar novo paciente? (sim/não)") .lower() .strip()

print("\n--- RELATÓRIO FINAL DO PLANTÃO ---")

for paciente in pacientes_atendidos:
    
    nome = paciente["nome"]
    idade = paciente["idade"]
    dor = paciente["dor"]
    
    print(f"- Paciente: {nome} | Idade: {idade} | Nível de Dor: {dor}")
