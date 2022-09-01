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
    dic_utn.append(hab['Nombre'])
    dic_utn.append(hab['Poder'])
    dic_utn = tuple(dic_utn)
    habilidades_UTN.append(dic_utn)
# print(habilidades_UTN)

max_poder = 0
pos = 1
temp_list = []
for tup in habilidades_UTN:
    nro_poder = tup[pos]
    if (nro_poder > max_poder):
        max_poder = nro_poder
        temp_list.append(tup)
    else:
        i = 0
        for hab in temp_list:
            if(nro_poder < hab[pos]):
                # print(i, nro_poder)
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
