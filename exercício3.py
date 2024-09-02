faturamento = [
    100, 200, 320, 0, 300, 50, 40, 0, 450, 150, 380, 150, 330, 0, 50, 60, 
    0, 150, 0, 600, 700, 900, 0, 1000, 1500, 1200, 0, 0, 150, 90
]

def calculo_de_faturamento(faturamento):

    faturamentoValido = []
    for valor in faturamento:
        if valor > 0:
            faturamentoValido.append(valor)

    menorValor = min(faturamentoValido)
    maiorValor = max(faturamentoValido)

    mediaMensal = sum(faturamentoValido) / len(faturamentoValido)

    faturamentoDiario = len([valor for valor in faturamentoValido if valor > mediaMensal])

    return menorValor, maiorValor, faturamentoDiario

menor_valor, maior_valor, faturamento_diario = calculo_de_faturamento(faturamento)

print(f"Menor valor de faturamento em um dia do mês: {menor_valor}")
print(f"Maior valor de faturamento em um dia do mês: {maior_valor}")
print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {faturamento_diario}")