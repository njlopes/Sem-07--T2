num = int(input(''))
quant = 0

unidade = num // 1 % 10
dezena = num // 10 % 10


if unidade % 2 != 0:
    quant = quant + 1
if dezena % 2 != 0:
    quant = quant + 1
else:
    print('Nenhum dígito é ímpar.')

if quant == 1:
    print('Apenas um dígito é ímpar.')
if quant == 2:
    print('Os dois dígitos são ímpares.')




