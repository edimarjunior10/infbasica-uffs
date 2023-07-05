def resumo():
    mensagem = "Linus Benedict Torvalds é um engenheiro de software finlandês, nascido em 28 de dezembro de 1969, na cidade de Helsinki. Conhecer sua biografia é importante, já que ele é mundialmente conhecido por ter sido o criador do Kernel do Linux, base fundamental sobre a qual são construídos diversos sistemas operacionais gratuitos, como as distribuições Linux Ubuntu, Debian, Fedora e etc, além de produtos do Google, como o Chrome OS e o Android."
    return mensagem


def doutorado():
    mensagem = "Linus Benedict Torvalds (Helsínquia, 28 de dezembro de 1969) é um engenheiro de software, nascido na Finlândia e naturalizado estado-unidense em 2010,[1][2] criador, e por muito tempo o desenvolvedor mais importante do núcleo Linux, sendo utilizado em importantes sistemas Linux, Android e Chrome OS. É também o criador do Git, sistema de controle de versão amplamente utilizado, e o aplicativo para planejamento e registro de mergulho, Subsurface.[3]"
    return mensagem


def contribuicoes():
<<<<<<< HEAD
    mensagem = "Linus define-se como sendo “completamente ateísta religioso”, adicionando: “acredito que as pessoas parecem pensar que a religião traz moral e apreciação a natureza"
=======
    mensagem = "Mais do que criador do Linux, Torvalds é um defensor do software livre e do código aberto, modelo em que o produto do desenvolvimento de programadores é liberado de forma gratuita para uso, modificação e, em alguns casos, exploração pela comunidade. "
>>>>>>> 3fa9d71d92751de6792e8314984b65223917a8c9
    return mensagem


def artigos():
    mensagem = "Em virtude da sua contribuição decisiva para a popularização do software livre, Torvalds é visto como uma figura de referência no mundo da tecnologia. Suas palestras, TEDs e conferências são eventos aguardados e concorridos por todos que têm interesse em desenvolvimento e engenharia, além da difusão do código aberto e do software livre."
    return mensagem


def citacoes():
<<<<<<< HEAD
    mensagem = "Junto ao médico Shinya Yamanaka, foi honrado pela Academia de Tecnologia da Finlândia, em 2012, com o Prêmio de Tecnologia do Milênio “em reconhecimento à sua criação de um novo núcleo de sistema operacional para computadores, que levou ao extensivamente utilizado, núcleo Linux”.[4] Torvalds também notoriamente recebeu os prêmios:"
=======
    mensagem = "Uma frase famosa de engenheiro é: “código aberto é o único jeito certo de se fazer software”."
>>>>>>> 3fa9d71d92751de6792e8314984b65223917a8c9
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
