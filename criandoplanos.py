def recomendar_plano(consumo_mensal: float) -> str:
    if consumo_mensal <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    elif consumo_mensal <= 20:
        return "Plano Prata Fibra - 100Mbps"
    else:
        return "Plano Premium Fibra - 300Mbps"
        
# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input("Digite o consumo medio mensal de dados em GB: "))

  # Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print("O plano que te indicamos é:", recomendar_plano(consumo))
