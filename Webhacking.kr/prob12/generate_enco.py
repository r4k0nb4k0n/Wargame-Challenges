enco = ''
enco2 = 126
enco3 = 33
ck = None

for i in range(1, 122):
	enco = enco + chr(i) + chr(0)

def enco_(x):
	return ord(enco[x])

ck="="+chr(enco_(240))+chr(enco_(220))+chr(enco_(232))+chr(enco_(192))+chr(enco_(226))+chr(enco_(200))+chr(enco_(204))+chr(enco_(222-2))+chr(enco_(198))+"~~~~~~"+chr(enco2)+chr(enco3)


print("Password is " + ck.replace("=",""))