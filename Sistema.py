
from datetime import date, datetime
from Pessoa import Endereco, PessoaFisica, PessoaJuridica


def main():
    lista_pf = []
    lista_pj = []
    while True:
        opcao = int(input("Escolha uma opção: 1 - Pessoa física / 2 - Pessoa juridica / 0 - Sair: "))

        if opcao == 1:
            while True:
                opcao_pf = int(input("Escolha uma opção: 1 - Cadastrar pessoa física / 2 - Listar pessoa física / 3 - Excluir / 4 - Atualizar lista / 0 - Voltar ao menu anterior: "))

                if opcao_pf == 1:
                    novaPessoa = PessoaFisica()
                    novoEndereco = Endereco()
                    
                    novaPessoa.nome = input("Digite o nome da pessoa física: ")
                    novaPessoa.cpf = input("Digite o cpf: ")
                    novaPessoa.rendimento = float(input("Digite o rendimento (somente numeros): "))

                    data_nascimento = input("Digite a date de nascimento (dd/mm/aaaa): ")
                    novaPessoa.dataNascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
                    idade = (date.today() - novaPessoa.dataNascimento).days // 365

                    if idade >= 18:
                        print("A pessoa tem mais de 18 anos")
                    else:
                        print("A pessoa tem menos de 18 anos. Retorne ao menu...")
                        continue
                    
                    novoEndereco.logradouro = input("Informe o logradouro: ")
                    novoEndereco.numero = input("Informe o numero: ")
                    enderecoComercial = input("Este endereço é comercial: S/N: ")
                    novoEndereco.endereco_Comercial = enderecoComercial.strip().upper() == 'S'
                    
                    novaPessoa.endereco = novoEndereco

                    lista_pf.append(novaPessoa)

                    print("Cadastro realizado com sucesso!!")
                elif opcao_pf == 2:
                    if lista_pf:
                        for pessoa in lista_pf:
                            print(pessoa.nome)
                            print(pessoa.cpf)
                            print(f"Endereço: {pessoa.endereco.logradouro}, {pessoa.endereco.numero}")
                            print(f"Imposto a ser pago: {pessoa.calcular_imposto(pessoa.rendimento)}")
                            print("Digite 0 para sair: ")
                            input()
                    else:
                        print("Lista Vazia")
                elif opcao_pf == 3:
                    remov_cpf = input("Qual CPF voce deseja remover?: ")

                    pessoa_encontrada = False

                    for cada_pf in lista_pf:    
                        if cada_pf.cpf == remov_cpf:
                            lista_pf.remove(cada_pf)
                            pessoa_encontrada = True
                            print("Pessoa removida!")
                            break
                        else:
                         print("CPF não encontrado") 
                elif opcao_pf == 4:
                    verif_cpf = input("Digite o CPF de qual nome voce deseja editar (Exatamente como digitaste): ")
                    for cada_item in lista_pf:
                        if cada_item.cpf == verif_cpf:
                            atualizar_lisa = input("Qual opção voce quer atualizar? 0 - Sair / 1 - nome / 2 - cpf / 3 - rendimento / 4 - data de nascimento / 5 - logadouro / 6 - Endereço comercial")
                            if atualizar_lisa == "1":
                                novo_nome = input("Qual o novo nome que voce deseja cadastrar?: ")
                                novaPessoa.nome = novo_nome
                            elif atualizar_lisa == "2":
                                novo_cpf = input("Digite o novo cpf: ")
                                novaPessoa.cpf = novo_cpf
                            elif atualizar_lisa == "3":
                                novo_rend = input("Digite o rendimento atual: ")
                                novaPessoa.rendimento = novo_rend
                            elif atualizar_lisa == "4":
                                novo_nascimento = input("Digite o nascimento atual: ")
                                novaPessoa.dataNascimento = novo_nascimento
                            elif atualizar_lisa == "5":
                                novo_log = input("Digite o logadouro atual: ")
                                novoEndereco.logradouro = novo_log
                        else:
                            print("Nao existe")
                            pass                            
                        

                elif opcao == 0: 
                    print("Voltando ao menu interior")
                    break
                else: 
                    print("Opção inválida, por favor digite uma das opções inidicadas: ")
        elif opcao == 2: 
            while True:
                opcao_pj = int(input("Escolha uma opção: 1 - Cadastrar pessoa juridica / 2 - Listar pessoa juridica / 3 - Remover Pessoa 0 - Voltar ao menu anterior: "))
                if opcao_pj == 1:
                    novapj = PessoaJuridica()
                    novo_end_pj = Endereco()
                    novapj.nome = input("Digite o nome da pessoa Juridica: ")
                    novapj.cnpj = input("Digite o cnpj da pessoa juridica: ")
                    novapj.rendimento = int(input("Digite o rendimento da pessoa juridica:"))
                    novapj.lucro = int(input("Digite o Lucro da pessoa juridica: "))
                    
                    novo_end_pj.logradouro = input("Digite o logradouro da pessoa juridica: ")
                    novo_end_pj.numero = input("Digite o numero do endereço da pessoa juridica: ")
                    novo_end_pj.endereco_Comercial = input("Esse endereço é comercial? [S/N]").upper()
                    novapj.endereco = novo_end_pj
                    lista_pj.append(novapj)
                elif opcao_pj == 2:
                    if lista_pj:
                        for cada_pj in lista_pj:
                            print(f"Nome {cada_pj.nome}")
                            print(f"Rendimento: {cada_pj.rendimento}")
                            print(f"Endereço: {cada_pj.endereco}")
                            print(f"Rendimento: {cada_pj.rendimento}")
                            print(f"Cnpj: {cada_pj.cnpj}")
                            print(f"Lucro: {cada_pj.lucro}")
                            print(f"Imposto a ser pago: {cada_pj.calcular_imposto(cada_pj.rendimento, cada_pj.lucro)}")
                            print("Digite 0 para sair: ")
                            input()
                        else:
                            print("Lista Vazia!")              
                elif opcao_pj == 3:
                    remov_cpf = input("Qual cnpj voce deseja remover?: ")

                    pessoa_encontrada = False

                    for cada_pj in lista_pj:    
                        if cada_pj.cnpj == remov_cpf:
                            lista_pf.remove(cada_pj)
                            pessoa_encontrada = True
                            print("Pessoa removida!")
                            break
                        else:
                         print("CPF não encontrado") 
                elif opcao == 0:
                    print("Voltando ao menu anterior")
                    break
                else:
                    print("Opção invalida!")    


                    
        elif opcao == 0:
            print("Obrigado por utilizar o nome sistema! Valeu!")
            break
        else: 
            print("Opção inválida, por favor digite uma das opções válidas!")

if __name__ == "__main__":
    main()
                            


                    