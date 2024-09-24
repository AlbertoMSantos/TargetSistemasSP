import json

with open("dados.json") as Target_json:
    dados = json.load(Target_json)
    
faturamentos = []

for i in dados:
    if i["valor"] != 0.0: faturamentos.append(i["valor"])

media = sum(faturamentos) / len(faturamentos)
dias_acima_media = 0
for i in faturamentos:
    if i > media: dias_acima_media = dias_acima_media + 1

print("menor valor de faturamento ocorrido em um dia do mês: ",min(faturamentos))
print("maior valor de faturamento ocorrido em um dia do mês: ",max(faturamentos))
print("número de dias no mês em que o valor de faturamento diário foi superior à média mensal.: ", dias_acima_media)

