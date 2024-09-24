
string = "string a ser invertida"
invertida = []
i = 1
while len(string) >= i:
    invertida.append(string[len(string) - i])
    i = i + 1
print(invertida)
