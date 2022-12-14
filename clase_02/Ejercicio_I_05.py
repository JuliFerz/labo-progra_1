""" 
Autor: Fernandez, Julian
Divison: H
Ejercicio: Ejercicio_I_05
"""
habilidades = [
    {
        "Nombre": "Vision-X",
        "Poder": 64
    },
    {
        "Nombre": "Vuelo",
        "Poder": 32
    },
    {
        "Nombre": "Inteligencia",
        "Poder": 256
    },
    {
        "Nombre": "Metamorfosis",
        "Poder": 1024
    },
    {
        "Nombre": "Super Velocidad",
        "Poder": 128
    },
    {
        "Nombre": "Magia",
        "Poder": 512
    }
]

habilidades_UTN = []
for hab in habilidades:
    dic_utn = []
    for value in hab.values():
        dic_utn.append(value)
    dic_utn = tuple(dic_utn)
    habilidades_UTN.append(dic_utn)

max_poder = habilidades_UTN[0][1]
pos = 1
temp_list = []
for tup in habilidades_UTN:
    nro_poder = tup[pos]
    if (nro_poder >= max_poder):
        max_poder = nro_poder
        temp_list.append(tup)
    else:
        i = 0
        for hab in temp_list:
            if(nro_poder < hab[pos]):
                temp_list.insert(i, tup)
                break
            i += 1

i = 1
print('habilidades_UTN')
for info in temp_list:
    habilidad = info[0]
    poder = info[1]
    print(f'Habilidad {i}: {habilidad} | Poder: {poder}')
    i += 1
