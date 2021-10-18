num = int(input(''))
quant = 0

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10

if unidade % 2 == 0:
    quant = quant + 1

if dezena % 2 == 0:
    quant = quant + 1

if centena % 2 == 0:
    quant = quant + 1

if unidade % 2 != 0:
    quant = 0

if dezena % 2 != 0:
    quant = 0


print(quant)
