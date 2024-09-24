
lista = {"SP": 67836.43,"RJ": 36678.66,"MG": 29229.88,"ES":27165.48,"Outros": 19849.53}
 
soma = 0
for i, j in lista.items():
    soma = soma + j
for i, j in lista.items():
    print(i,"\b:", round((j/soma)*100,4), "\b%")
