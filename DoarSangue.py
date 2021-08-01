def doador():
    nome = str(input('Qual o seu nome senhor(a)?'))
    print('Meu nome é {}'.format(nome))
    idade = int(input('Qual a sua idade?'))
    print('Minha idade é {}'.format(idade))
    peso = float(input('Digite o seu peso'))
    print('Meu peso é {}'.format(peso))
    if idade >= 18 and peso >= 50:
        print('Muito bem senhor(a) {}, você pode doar sangue.'.format(nome))
    else:
        print('Desculpe mas você não pode doar sangue, obrigado pela colaboração!')
doador()










