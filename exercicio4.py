faturamentoMensal = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

valorTotalMensal = sum(faturamentoMensal.values())

def calculoDePercentual(faturamentoMensal, valorTotalMensal):
    percentuais = {}
    for estado, faturamento in faturamentoMensal.items():
        percentuais[estado] = (faturamento / valorTotalMensal) * 100
    return percentuais

percentualEstado = calculoDePercentual(faturamentoMensal, valorTotalMensal)

for estado, percentual in percentualEstado.items():
    print(f"{estado}: {percentual:.2f}%")