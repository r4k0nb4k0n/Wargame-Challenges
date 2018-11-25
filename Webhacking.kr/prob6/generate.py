import base64

idpw = None
idpw = b'admin'

for i in range(1, 21):
	idpw = base64.b64encode(idpw)
	print('base64 encoding ' + str(i) + ' time(s)... ', idpw)

idpw = idpw.decode()

idpw.replace("1", "!")
idpw.replace("2", "@")
idpw.replace("3", "$")
idpw.replace("4", "^")
idpw.replace("5", "&")
idpw.replace("6", "*")
idpw.replace("7", "(")
idpw.replace("8", ")")

print('final is', idpw)