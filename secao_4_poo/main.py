from pessoa import Pessoa

p1 = Pessoa("amauri", 20)
p1.comer('maça')
p1.falar('POO')
p1.parar_comer()
p1.falar('POO')
p1.comer('alimento')
p1.parar_falar()
p1.falar('assunto')

print('---------------')
p2 = Pessoa('Bob', 29)
p3 = Pessoa('Zé', 32)

p2.falar('POO')
p3.comer('sorvete')
p2.comer('churrasco')

print(p1.ano_atual)
print(p2.ano_atual)
print(Pessoa.ano_atual) # imprimindo a variável atraves da classe
print('-----------------------------------------')

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
