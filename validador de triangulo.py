# validador de triangulo
n1 = float(input('\033[0;49;97mdigite um comprimento\n'))
n2 = float(input('digite um outro comprimento\n'))
n3 = float(input('digite um outro comprimento\n'))

if n1 < n2+n3 and n2 < n1+n3 and n3 < n1+n2:
    print('\033[0;49;92mForma um Triangulo seu Rapaz')
else:
    print('\033[0;49;31mNão forma um Triangulo seu Rapaz')
# iaearnold
