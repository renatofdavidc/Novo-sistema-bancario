def menu():
    print('============ MENU PRINCIPAL ============')
    print('[1] - Depositar')
    print('[2] - Sacar')
    print('[3] - Ver extrato')
    print('[4] - Nova conta')
    print('[5] - Listar contas')
    print('[6] - Novo usuário')
    print('[7] - Sair')
    print('=========================================')
    opcao = input('Escolha uma opção: ')
    return opcao

def depositar(saldo, valor_deposito, extrato):
    print('===== DEPÓSITOS =====')
    if valor_deposito <= 0:
        print('Valor inválido!')
    else: 
        saldo += valor_deposito
        print(f'O novo saldo é R${saldo:.2f}')
        extrato += f'Depósito: R${valor_deposito:.2f}\n'
    return saldo, extrato

def sacar(saldo, limite_saques_diarios, limite_valor_saque, numero_saques, valor_saque, extrato):
    print('===== SAQUE =====')
    if saldo <= 0:
        print('Não há dinheiro para ser sacado!')
    else:
        if valor_saque > saldo:
            print('Não há dinheiro suficiente na conta para realizar o saque!')
        else:
            if valor_saque > 500 or valor_saque <= 0:
                print('O valor escolhido é maior do que o limite ou negativo, o saque não pode ser realizado.')
            else:
                if numero_saques < limite_saques_diarios:
                    saldo -= valor_saque
                    extrato += f'Saque: R${valor_saque:.2f}\n'
                    print(f'O novo saldo é R${saldo:.2f}')
                    numero_saques += 1
                else:
                    print('ERRO! Limite de saques diários atingido.')
    return saldo, extrato, numero_saques

def ver_extrato(saldo, extrato):
    print('===== EXTRATO =====')
    print('Não foram realizadas movimentações!' if not extrato else extrato)
    print(f'Saldo da conta: R${saldo:.2f}')

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (Somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print('Já existe um usuário com esse CPF!')
        return
    nome = input('Informe o nome do usuário: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço: rua/bairro/cidade/estado: ')
    
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    print('Usuário criado com sucesso!')
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Digite o CPF: ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print('Conta criada com sucesso!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    print('Usuário não encontrado!')
    
def listar_contas(contas):
    for conta in contas:
        print(f"Agência: {conta['agencia']}")
        print(f"C/C: {conta['numero_conta']}")
        print(f"Titular: {conta['usuario']['nome']}")

def main():
    saldo = 0
    numero_saques = 0
    extrato = ''
    limite_saques_diarios = 3
    limite_valor_saque = 500
    usuarios = []
    contas = []
    agencia = '0001'
    
    while True:
        opcao = menu()
        
        match opcao:
            case '1':
                valor_deposito = float(input('Digite o valor a ser depositado: '))
                saldo, extrato = depositar(saldo, valor_deposito, extrato)
            case '2':
                valor_saque = float(input('Informe o valor do saque: '))
                saldo, extrato, numero_saques = sacar(saldo=saldo, limite_saques_diarios=limite_saques_diarios, limite_valor_saque=limite_valor_saque, numero_saques=numero_saques, valor_saque=valor_saque, extrato=extrato)
            case '3':
                ver_extrato(saldo, extrato=extrato)
            case '4':
                numero_conta = len(contas) + 1
                conta = criar_conta(agencia,numero_conta, usuarios)
                if conta:
                    contas.append(conta)
            case '5':
                listar_contas(contas)
            case '6':
                criar_usuario(usuarios)
            case '7':
                break
            case _:
                print('Opção inválida, tente novamente!')

main()
