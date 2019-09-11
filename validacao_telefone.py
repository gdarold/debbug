#coding: utf-8


import re


telefone = 'o telefone é (49) 99555-4455 '
telefone +='o telefone do jose é (47) 99898-4904'

pattern = '(\(?[0-9]{2}\)\s[0-9]{4,5}\-?[0-9]{4})'

#resultado = re.search(pattern,telefone) # busca no texto o padrão
resultado = re.findall(pattern,telefone) # busca 

#resultado = re.match(pattern,telefone) procura resultado exato
print(resultado)

#print(telefone)


