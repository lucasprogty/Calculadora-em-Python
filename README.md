# Calculadora em Python
 Para executar a calculadora voce precisara dos dois arquivos. (Calculadora.py e calculadoraExecutavel.sh).
 no seu terminal de comando digite: bash ./calculadoraExecutavel.sh

 Documentaçao do codigo: 

 
gameOn = True #condiçao inicial para que o codigo sera inicializado e se mantenha.

while gameOn: #enquanto a condiçao "gameOn" nao for mudada
	num1 = float(input('digite um numero:\n'))
	num2 = float(input('digite outro numero:\n'))
	operaçao = input('qual operaçao voce deseja realizar: adiçao, subtraçao, multiplicaçao, divisao\n').lower() #O usuario define qual operaçao sera realizada e qual clausa if sera utilizada.

	if operaçao =='adiçao':
		resultado = num1 + num2
		print(resultado)

	elif operaçao == 'subtraçao':
		resultado = num1 - num2
		print(resultado)

	elif operaçao == 'multiplicaçao':
		resultado = num1 * num2
		print(resultado)

	elif operaçao == 'divisao':
		resultado = num1 / num2
		print(resultado)

	continuar = input('voce deseja continuar: sim ou nao?').lower() #caso o usuario nao deseje continuar a condiçao para que o nosso loop While sera desfeita e o programa sera finalizado.
	if continuar == 'nao':
		gameOn = False
