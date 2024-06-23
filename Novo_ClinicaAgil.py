import datetime
import json

pacientes = []
agendamentos = []

def salvar_dados():
    with open('pacientes.json', 'w') as f:
        json.dump(pacientes, f)
    with open('agendamentos.json', 'w') as f:
        json.dump(agendamentos, f)

def carregar_dados():
    global pacientes, agendamentos
    try:
        with open('pacientes.json', 'r') as f:
            pacientes = json.load(f)
        with open('agendamentos.json', 'r') as f:
            agendamentos = json.load(f)
    except FileNotFoundError:
        pacientes = []
        agendamentos = []

def cadastrar_paciente():
    nome = input("Digite o nome do paciente: ")
    telefone = input("Digite o telefone do paciente: ")
    for paciente in pacientes:
        if paciente['telefone'] == telefone:
            print("Paciente já cadastrado!")
            return
    pacientes.append({'nome': nome, 'telefone': telefone})
    print("Paciente cadastrado com sucesso")

def marcar_consulta():
    if not pacientes:
        print("Nenhum paciente cadastrado ainda.")
        return
    for i, paciente in enumerate(pacientes):
        print(f"{i + 1}. {paciente['nome']} - {paciente['telefone']}")
    indice_paciente = int(input("Selecione o número do paciente: ")) - 1
    if indice_paciente < 0 or indice_paciente >= len(pacientes):
        print("Seleção inválida.")
        return
    dia = input("Digite o dia (AAAA-MM-DD): ")
    hora = input("Digite a hora (HH:MM): ")
    especialidade = input("Digite a especialidade: ")
    horario_consulta = f"{dia} {hora}"
    for agendamento in agendamentos:
        if agendamento['horario'] == horario_consulta:
            print("Horário de consulta já ocupado.")
            return
    horario_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    if horario_consulta < horario_atual:
        print("Não é possível agendar consultas no passado.")
        return
    agendamentos.append({
        'paciente': pacientes[indice_paciente],
        'horario': horario_consulta,
        'especialidade': especialidade
    })
    print("Consulta agendada com sucesso")

def cancelar_consulta():
    if not agendamentos:
        print("Nenhuma consulta agendada ainda.")
        return
    for i, agendamento in enumerate(agendamentos):
        print(f"{i + 1}. {agendamento['paciente']['nome']} - {agendamento['horario']} - {agendamento['especialidade']}")
    indice_agendamento = int(input("Selecione o número da consulta: ")) - 1
    if indice_agendamento < 0 or indice_agendamento >= len(agendamentos):
        print("Seleção inválida.")
        return
    del agendamentos[indice_agendamento]
    print("Consulta cancelada com sucesso")

def menu_principal():
    carregar_dados()
    while True:
        print("\n1. Cadastrar um paciente")
        print("2. Marcar uma consulta")
        print("3. Cancelar uma consulta")
        print("4. Sair")
        escolha = input("Selecione uma opção: ")
        if escolha == '1':
            cadastrar_paciente()
        elif escolha == '2':
            marcar_consulta()
        elif escolha == '3':
            cancelar_consulta()
        elif escolha == '4':
            salvar_dados()
            break
        else:
            print("Seleção inválida.")

if __name__ == "__main__":
    menu_principal()
    