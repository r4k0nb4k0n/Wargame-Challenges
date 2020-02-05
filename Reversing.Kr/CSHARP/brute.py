info = [{"operand": 0, "result": 0} for x in range(12)]
info[0]["operand"] = 16
info[0]["result"] = 74
info[3]["operand"] = 51
info[3]["result"] = 70
info[1]["operand"] = 17
info[1]["result"] = 87
info[2]["operand"] = 33
info[2]["result"] = 77
info[11]["operand"] = 17
info[11]["result"] = 44
info[8]["operand"] = 144
info[8]["result"] = 241
info[4]["operand"] = 68
info[4]["result"] = 29
info[5]["operand"] = 102
info[5]["result"] = 49
info[9]["operand"] = 181
info[9]["result"] = 226
info[7]["operand"] = 160
info[7]["result"] = 238
info[10]["operand"] = 238
info[10]["result"] = 163
info[6]["operand"] = 51
info[6]["result"] = 117

brute = []
for i in range(12):
    for j in range(0, 256):
        if((j ^ info[i]["operand"]) == info[i]["result"]):
            brute += [j]
            break

print("".join([chr(x) for x in brute]))
