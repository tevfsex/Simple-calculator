print ("Bem Vindo A Simple Calculator")
print()
print("---Escolha Uma Opção---")
print("""
1.Sumar
2.Restar
3.Multiplicar
4.Dividir
5.Divisāo Decimal""")
print()

Escolha = input("")

if Escolha == "1":
    print()
    print('-Opção "Sumar" Escolhida-')
    P_valor = int(input("Digite Seu Primer Valor: "))
    S_valor = int(input("Digite Seu Segundo Valor: "))
    print()
    print(P_valor + S_valor)
elif Escolha == "2":
    print()
    print('-Opção "Restar" Escolhida-')
    P_valor = int(input("Digite Seu Primer Valor: "))
    S_valor = int(input("Digite Seu Segundo Valor: "))
    print()
    print(P_valor - S_valor)
elif Escolha == "3":
    print()
    print('-Opção "Multiplicar" Escolhida-')
    P_valor = int(input("Digite Seu Primer Valor: "))
    S_valor = int(input("Digite Seu Segundo Valor: "))
    print()
    print(P_valor * S_valor)
elif Escolha == "4":
    print()
    print('-Opção "Dividir" Escolhida-')
    P_valor = int(input("Digite Seu Primer Valor: "))
    S_valor = int(input("Digite Seu Segundo Valor: "))
    print()
    print(P_valor // S_valor)    
elif Escolha == "5":
    print()
    print('-Opção "Divisão Decimal" Escolhida-')
    P_valor = float(input("Digite Seu Primer Valor: "))
    S_valor = float(input("Digite Seu Segundo Valor: "))
    print()
    print(P_valor / S_valor) 
else:
    print("Essa Opção Não Existe.")