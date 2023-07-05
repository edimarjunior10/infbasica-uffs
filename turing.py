def resumo():
    mensagem = "Linus Benedict Torvalds é um engenheiro de software finlandês, nascido em 28 de dezembro de 1969, na cidade de Helsinki. Conhecer sua biografia é importante, já que ele é mundialmente conhecido por ter sido o criador do Kernel do Linux, base fundamental sobre a qual são construídos diversos sistemas operacionais gratuitos, como as distribuições Linux Ubuntu, Debian, Fedora e etc, além de produtos do Google, como o Chrome OS e o Android."
    return mensagem


def doutorado():
    mensagem = ""
    return mensagem


def contribuicoes():
    mensagem = "Mais do que criador do Linux, Torvalds é um defensor do software livre e do código aberto, modelo em que o produto do desenvolvimento de programadores é liberado de forma gratuita para uso, modificação e, em alguns casos, exploração pela comunidade. "
    return mensagem


def artigos():
    mensagem = "Em virtude da sua contribuição decisiva para a popularização do software livre, Torvalds é visto como uma figura de referência no mundo da tecnologia. Suas palestras, TEDs e conferências são eventos aguardados e concorridos por todos que têm interesse em desenvolvimento e engenharia, além da difusão do código aberto e do software livre."
    return mensagem


def citacoes():
    mensagem = "Uma frase famosa de engenheiro é: “código aberto é o único jeito certo de se fazer software”."
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Allan Turing.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
            """
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
