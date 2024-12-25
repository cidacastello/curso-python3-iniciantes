# entrada de dados
latas = int(input('Digite a quantidade de latas de refrigerante: '))
preco = float(input('Digite o preço unitário: '))

# processamento
total = latas * preco

# saída
print('Você comprou', latas, 'latas de refrigerante no valor de',preco, 'cada. O valor total da compra é de R$', total)
print('Você comprou ' + str(latas) + ' latas de refrigerante no valor de ' + str(preco) + ' cada. O valor total da compra é de R$ '+ str(total))
# marcador de posição - %
print('Você comprou %d latas de refrigerante no valor de %.2f cada. O valor total da compra é de R$ %.2f' %(latas, preco, total))
# função format
print('Você comprou {} latas de refrigerante no valor de {} cada. O valor total da compra é de R$ {}'.format(latas, preco, total))
# interpolation
print(f'Você comprou {latas} latas de refrigerante no valor de {preco:.2f} cada. O valor total da compra é de R$ {total:.2f}')
print(f'Você comprou {latas} latas de refrigerante no valor de {preco:.2f} cada. O valor total da compra é de R$ {latas*preco:.2f}')