heroes_para_reclutar = [
    "Batman", "BatWoman", "BatGirl",
    "Wonder Woman", "Aquaman", "Shazam",
    "Superman", "Super Girl", "Power Girl"
]

heroes_info = {
    "Super Girl": {
        "ID": 1,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Volar", "Fuerza", "Velocidad"],
        "Identidad": "Kara Zor-El"
    },
    "Shazam": {
        "ID": 25,
        "Origen": "Tierra",
        "Habilidades": ["Volar", "Fuerza", "Velocidad", "Magia", "Fuerza", "Velocidad"],
        "Identidad": "Billy Batson"
    },
    "Power Girl": {
        "ID": 14,
        "Origen": "Krypton",
        "Habilidades": ["Volar", "Fuerza", "Congelar", "Congelar", "Congelar"],
        "Identidad": "Karen Starr"
    },
    "Wonder Woman": {
        "ID": 29,
        "Origen": "Amazonia",
        "Habilidades": ["Agilidad", "Fuerza", "Lazo de la verdad", "Escudo"],
        "Identidad": "Diana Prince"
    }
}
info_heroes_reclutar = []
for heroe in heroes_para_reclutar:
    heroe_reclutar = {}
    if (heroes_info.get(heroe)):
        # print(f'{heroe}, {heroes_info[heroe]}')  # PRUEBA
        heroe_reclutar['id'] = heroes_info[heroe]['ID']
        heroe_reclutar['codename'] = heroe
        heroe_reclutar['identity'] = heroes_info[heroe]['Identidad']
        heroe_reclutar['origin'] = heroes_info[heroe]['Origen']
        heroe_reclutar['habilities'] = set(heroes_info[heroe]['Habilidades'])
        info_heroes_reclutar.append(heroe_reclutar)
# print(info_heroes_reclutar)

for heroe in info_heroes_reclutar:
    habilidad = ''
    i = 0
    for hab in heroe['habilities']:
        habilidad += f'{hab}'
        habilidad += ' | ' if i + 1 < len(heroe['habilities']) else ''
        # print(i, len(heroe['habilities']))
        i += 1
    print(f'ID: {heroe["id"]}, Codename: {heroe["codename"]}')
    print(f'Identidad: {heroe["identity"]}, Origen {heroe["origin"]}')
    print(f'Habilidades: {heroe["habilities"]}')
    print(f'PRUEBA: {habilidad}')
    print('------------------------')
