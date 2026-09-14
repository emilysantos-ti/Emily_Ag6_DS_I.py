# Solicita o valor total da compra
valor_compra = float(input("Digite o valor da compra: R$ "))

# Verifica qual percentual de desconto deve ser aplicado
if valor_compra < 200:
    percentual = 0.05

elif valor_compra >= 200 and valor_compra < 300:
    percentual = 0.10

else:
    percentual = 0.15

# Calcula o valor do desconto
valor_desconto = valor_compra * percentual

# Calcula o valor final da compra
valor_final = valor_compra - valor_desconto

# Exibe os resultados
print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {percentual * 100:.0f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")
