# -*- coding: utf-8 -*-

import sys
import json
import pandas as pd
from pandas.io.json import json_normalize

if len(sys.argv) < 2:
    print('Usage: python solution.py [filename] - Executa o desafio 5 usando o nome de arquivo passado')
    sys.exit()
filename = sys.argv[1]

with open(filename, encoding='utf-8') as json_data:
    data = json.load(json_data)

funcionarios = json_normalize(data['funcionarios'])
areas = json_normalize(data['areas'])

# Questao 1
global_max = funcionarios.loc[funcionarios.salario == funcionarios.salario.max()]
for index, row in global_max.iterrows():
    print('global_max|{0}|{1:.2f}'.format(
        ' '.join([row.nome, row.sobrenome]),
        row.salario    
    ))

global_min = funcionarios.loc[funcionarios.salario == funcionarios.salario.min()]
for index, row in global_min.iterrows():
    print('global_min|{0}|{1:.2f}'.format(
        ' '.join([row.nome, row.sobrenome]),
        row.salario    
    ))

print('global_avg|{0:.2f}'.format(
    round(funcionarios.salario.mean(), 2)
))

# Questao 2
area_group = funcionarios.groupby(by='area')
for area, data in area_group:
    area_max = data.loc[data.salario == data.salario.max()]
    for index, row in area_max.iterrows():
        print('area_max|{0}|{1}|{2:.2f}'.format(
            areas.loc[areas.codigo == area].iloc[0].nome,
            ' '.join([row.nome, row.sobrenome]),
            row.salario    
        ))

    area_min = data.loc[data.salario == data.salario.min()]
    for index, row in area_min.iterrows():
        print('area_min|{0}|{1}|{2:.2f}'.format(
            areas.loc[areas.codigo == area].iloc[0].nome,
            ' '.join([row.nome, row.sobrenome]),
            row.salario    
        ))
    
    area_avg = data.loc[data.salario == data.salario.mean()]
    print('area_avg|{0}|{1:.2f}'.format(
            areas.loc[areas.codigo == area].iloc[0].nome,
            data.salario.mean()
        ))

# Questao 3
area_employees = funcionarios['area'].value_counts()

most_employees = area_employees.loc[area_employees == area_employees.max()]
for area in most_employees.index:
    print('most_employees|{0}|{1}'.format(
        areas.loc[areas.codigo == area].iloc[0].nome,
        most_employees[area]
    ))

least_employees = area_employees.loc[area_employees == area_employees.min()]
for area in least_employees.index:
    print('least_employees|{0}|{1}'.format(
        areas.loc[areas.codigo == area].iloc[0].nome,
        least_employees[area]
    ))

# Questao 4
last_names = funcionarios.groupby(by='sobrenome')
for sobrenome, data in last_names:
    if data.shape[0] > 1:
        last_name_max = data.loc[data.salario == data.salario.max()]
        for index, row in last_name_max.iterrows():
            print('last_name_max|{0}|{1}|{2:.2f}'.format(
                sobrenome,
                ' '.join([row.nome, row.sobrenome]),
                row.salario    
            ))