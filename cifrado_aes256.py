import  pyAesCrypt 
# tamaño del búfer de cifrado / descifrado - 64K 
bufferSize  =  64  *  1024 
contraseña = "carlos"
opc= input ("Desea encriptar s/n  ")
if (opc == 's'):
	# cifrar 
	print ("se realizara un cifrado del documneto")
	contraseña1 = input ("INGRESE LA CONTRASEÑA:  ")
	if(contraseña1 == contraseña):
		pyAesCrypt . encryptFile ( "hola.txt" ,  "hola.aes" ,  contraseña ,  bufferSize )
		print ("Documento cifrado con exito") 
		exit(0)
	
if(opc == 'n'):
	opc2= input ("Desea desencriptar s/n:  ")
	if (opc2 == 's'):
		# desencriptar 
		print ("se realizara un desifrado del documento")
		contraseña1 = input ("INGRESE LA CONTRASEÑA:  ")
		if (contraseña1 == contraseña): 
			pyAesCrypt . decryptFile ( "hola.aes" ,  "hola_desifrado.txt" ,  contraseña ,  bufferSize )
			print ("Documento desencriptado exitosamente")
			exit(0)
		else:
			print("contraseña incorrecta")
			exit(1)
		
	if (opc2 == 'n'):
		print("Programa terminado")
		exit(1)
