def main():
    # Lista para armazenar os equipamentos
    equipamentos = []

    # Loop para solicitar ao usuário inserir até três equipamentos
    for i in range(3):
        equipamento = input(f"Informe o equipamento {i + 1}: ")
        equipamentos.append(equipamento)

    # Exibir a lista de equipamentos inseridos pelo usuário
    print("Lista de Equipamentos:")
    for equipamento in equipamentos:
        print(f"- {equipamento}")

if __name__ == "__main__":
    main()

