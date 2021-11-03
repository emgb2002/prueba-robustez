try:
	numero = int(input("ingrese un numero de tres digitos: "))
	if numero >= 100 and numero <= 999:

		while numero != 0:
			if numero // 10 == 1 or numero % 10 == 1:
				print("el numero tiene el digito 1")
				break
			numero //= 10

		else:
			print("no tiene el digito 1")
	else:
		print("el numero ingresado no tiene 3 digitos")
except ValueError:
	print("Error... Se debe ingresar solo numeros enteros")