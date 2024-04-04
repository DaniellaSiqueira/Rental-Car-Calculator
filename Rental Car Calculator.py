km = int(input('Qual a quantidade de Km percorridos com o carro?: '))
dias = int(input('Qual a quantidade de dias alugado?: '))
km_rodado = km * 0.15
dias_alugado = dias * 60
valor_final = km_rodado + dias_alugado
print (f'O valor a pagar é de: {valor_final}')
