gameOn = True

while gameOn:
	num1 = float(input('digite um numero:\n'))
	num2 = float(input('digite outro numero:\n'))
	operaçao = input('qual operaçao voce deseja realizar: adiçao, subtraçao, multiplicaçao, divisao\n').lower()

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

	continuar = input('voce deseja continuar: sim ou nao?').lower()
	if continuar == 'nao':
		gameOn = False
