import json

with open('dados.json', 'r') as f:
    dados = json.load(f)

dias_com_valor_zero = []
maior_valor = 0
menor_valor = None
soma_valores = 0
dias_com_valores = 0

for obj in dados:
    dia = obj['dia']
    valor = float(obj['valor'])
    if valor == 0:
        dias_com_valor_zero.append(dia)
    else:
        if menor_valor is None or valor < menor_valor:
            menor_valor = valor
        if valor > maior_valor:
            maior_valor = valor
        soma_valores += valor
        dias_com_valores += 1

media_com_valores = soma_valores / dias_com_valores if dias_com_valores > 0 else 0
media_total = soma_valores / len(dados)

print(f"Quantidade de dias com valor 0: {len(dias_com_valor_zero)}")
print(f"Dias com valor 0: {dias_com_valor_zero}")
print(f"Dia com maior valor arrecadado: {maior_valor}")
print(f"Dia com menor valor arrecadado (excluindo dias com valor 0): {menor_valor}")
print(f"Média somente dos dias com valor: {media_com_valores}")
print(f"Média dos 30 dias: {media_total}")