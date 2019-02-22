#EXERCICIO 14
tempC = float(input('Digite a temperatura em graus C°:'))
tempF = float(((tempC/5)*9)+32)
print('{}°C corresponde a {}F°'.format(tempC, round(tempF,2)))

#EXERCICIO 15
dia = float(input('Quantos dias ele foi alugado?'))
km = float(input('Quantos km ele rodou?'))
print('O preço total ficou em R${}'.format(round((dia * 60) + (km * 0.15),2)))