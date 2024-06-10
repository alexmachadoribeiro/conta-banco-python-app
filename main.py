# importações
import os
from modulo import *

# programa principal
if __name__ == '__main__':
    # lista de dicionários
    correntistas = [
        {
            'Nome':'Admin',
            'Saldo': 1000
        }
    ]

    # entra no programa
    while True:
        exibir_menu()
        opcao = input('Opção desejada: ')
        os.system('cls')

        # cadastra um novo correntista
        if opcao == '1':
            # cria um dicionário
            correntista = {
                'Nome':'',
                'Saldo':0
            }

            correntista['Nome'] = input('Informe o nome a ser cadastrado: ')
            correntistas.append(correntista)
            print(f'{correntista['Nome']} cadastrado com sucesso.')
            continue

        # entra nas operações
        elif opcao == '2':
            titular = input('Informe o nome do titular: ')

            try:
                # pesquisa pelo correntista
                for i in range(len(correntistas)):
                    if titular in correntistas[i]['Nome']:
                        nome = correntistas[i]['Nome']
                        saldo = correntistas[i]['Saldo']
                        
                        # exibe as operações
                        while True:
                            exibir_dados(nome, i, saldo)
                            exibir_operacoes()

                            operacao = input('Operação desejada: ')
                            os.system('cls')
                            # verifica a operação escolhida
                            match operacao:
                                # exibe o saldo
                                case '1':
                                    print(f'Saldo: R$ {saldo:,.2f}')
                                    continue
                                # depósito
                                case '2':
                                    valor = str(input('Valor do depósito: R$ '))
                                    valor = float(valor.replace(',', '.'))
                                    saldo = depositar_valor(saldo, valor)
                                    correntistas[i]['Saldo'] = saldo

                                    print('Depósito efetuado com sucesso.')
                                    print(f'Saldo atual: R$ {saldo:,.2f}')

                                    continue
                                # saque
                                case '3':
                                    valor = str(input('Valor do saque: R$ '))
                                    valor = float(valor.replace(',', '.'))

                                    if valor < saldo:
                                        saldo = sacar_valor(saldo, valor)
                                        correntistas[i]['Saldo'] = saldo

                                        print('Saque efetuado com sucesso.')
                                        print(f'Saldo atual: R$ {saldo:,.2f}')
                                    else:
                                        print('Não foi possível efetuar o saque.')
                                    continue
                                # encerra as operações e volta para o menu anterior
                                case '4':
                                    break
                                # operação inexistente
                                case _:
                                    print('Operação inválida.')
                                    continue
                    # avança para o próximo loop caso o nome não seja encontrado
                    else:
                        continue
            # mensagem de nome não encontrado
            except:
                print(f'{nome} não encontrado.')
            # volta para o menu anterior
            continue
        # exibe a lista de correntistas
        elif opcao == '3':
            for correntista in correntistas:
                print(correntista)
            continue
        # exclui correntista
        elif opcao == '4':
            indice = int(input('Informe o ID da conta a ser excluída: '))

            try:
                del[correntistas[indice]]
                print(f'Conta {indice} deletada com sucesso.')
            except:
                print('Não foi possível deletar conta.')
            continue
        # encerra programa
        elif opcao == '5':
            break
        # invalida a opção
        else:
            print('Opção inválida.')