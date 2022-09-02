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
    dic_utn.append(hab['Nombre'])  # revisar, tomar objeto entero
    dic_utn.append(hab['Poder'])
    dic_utn = tuple(dic_utn)
    habilidades_UTN.append(dic_utn)
# print(habilidades_UTN)

max_poder = 0  # REVISAR no hardcodear un valor, tomar un valor real
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
# print(temp_list)
'''
lista: [64, 32, 256, 1024, 128, 512]
orden: [32, 64, 128, 256, 512, 1024]

obtengo: [512, 128, 32, 64, 256, 1024]
'''
i = 1
print('habilidades_UTN')
for info in temp_list:
    habilidad = info[0]
    poder = info[1]
    print(f'Habilidad {i}: {habilidad} | Poder: {poder}')
    i += 1
