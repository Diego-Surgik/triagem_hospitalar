plantao = "sim"
while plantao == "sim":
    nome_do_paciente = input("Digite o nome do paciente:") .title() .strip()
    idade = int(input("Digite a idade do paciente:")) 
    dor = int(input("Digite o nível de dor do paciente (0 a 10): "))
    plantao = ("aberto")
    print(f"Paciente: {nome_do_paciente} idade: {idade} anos")



    if dor >= 8:
        print("Classificação: EMERGENCIA")
    elif idade >= 65:
        print("Classificação: PRIORIDADE")
    else:
     print("Classificação: NORMAL")

    plantao = input("Deseja registrar novo paciente? (sim/não)") .lower() .strip()





