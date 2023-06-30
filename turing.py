def resumo():
    mensagem = "A amizade de toda a vida que se criou entre Ada Lovelace e Charles Babbage gerou uma união inestimável de software e hardware, à qual devemos grande parte da vida moderna. Babbage tinha o sonho de construir uma grande máquina de calcular que permitiria que tabelas matemáticas fossem calculadas de forma confiável por máquinas. No final, ele projetou duas máquinas – a Máquina Diferencial e a Máquina Analítica – que jamais foram construídas por falta de financiamento e tecnologia necessária. A Máquina Analítica foi a primeira máquina da história que pôde ser programada para executar comandos de qualquer tipo. Ada se apaixonou por ela. Embora a ideia de Babbage fosse usá-la apenas para fins matemáticos, Ada percebeu que a máquina era capaz de realizar todos os tipos de processos, até mesmo compor música. 10 anos depois de conhecer Babbage, ela traduziu um artigo italiano sobre a Máquina Analítica e complementou o estudo com um conjunto de observações suas. Essas notas, que acabaram sendo mais extensas do que o artigo original, continham um algoritmo criado para ser processado por máquinas, sendo considerado o primeiro programa de computador já criado. Assim, Ada fez história se tornando a primeira pessoa programadora do mundo. Ela morreu de câncer de útero aos 36 anos, mas seu legado, continua vivo. Ela deu seu nome à linguagem de programação Ada e, todos os anos, na 2º terça-feira de outubro, as contribuições das mulheres para a ciência, tecnologia, engenharia e matemática são comemoradas no Dia Ada Lovelace."
    return mensagem


def doutorado():
    mensagem = ""
    return mensagem


def contribuicoes():
    mensagem = ""
    return mensagem


def artigos():
    mensagem = ""
    return mensagem


def citacoes():
    mensagem = ""
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
