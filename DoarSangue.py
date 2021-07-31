nome = str(input('Bom dia, qual o seu nome? '))
print('Olá senhor(a) {}, bem vindo ao hospital do amor.'.format(nome))

idade = int(input('Qual sua idade? '))
print('Muito bem, você tem {} anos. '.format(idade))

peso = float(input('Qual o seu peso? '))
print('Perfeito, seu peso é de {} Kg. '.format(peso))

if idade >= 18 and peso >= 50:
    print('Muito bem senhor(a) {}, você pode doar sangue.'.format(nome))
else:
    print('Desculpe mas você não pode doar sangue, obrigado pela colaboração!')
