import time
import random
# lista = [14, 5, 20, 10, 23, 15, 7, 16, 29, 21, -102, 99, 0]
lista = [3, 6, 1, 4, 8, 2, 7, 5]

# lista = random.sample(range(1000), 50)


""" def _sort(lista):  # Sort test
    for j in range(len(lista) - 1):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista """


def _sort(lista):  # Sort test
    c_lista = lista.copy()
    for i in range(len(c_lista)):
        # print(c_lista)
        for j in range(len(c_lista)):
            # print(c_lista[i], c_lista[j])
            if c_lista[i] < c_lista[j]:
                c_lista[i], c_lista[j] = c_lista[j], c_lista[i]
    return c_lista

# Medir el tiempo de ejecución:
# inicio = time.time()
# print(_sort(lista))
# fin = time.time()
# print(fin - inicio)


def j_sort(lista: list):  # Sort mio
    max_el = lista[0]
    temp_lista = []
    for el in lista:
        if el >= max_el:
            max_el = el
            temp_lista.append(max_el)
        else:
            i = 0
            for temp_el in temp_lista:
                if el < temp_el:
                    temp_lista.insert(i, el)
                    break
                i += 1

    return temp_lista


# inicio = time.time()
# print(j_sort(lista))
# fin = time.time()
# print(fin - inicio)


# print(s_list(lista))


def q_sort(lista):  # quick sort
    copy_lista = lista.copy()
    random_num = random.choice(copy_lista)
    copy_lista.pop(copy_lista.index(random_num))
    print(f'PIVOTE: {random_num}')

    R_list = []
    L_list = []
    if (len(copy_lista) > 1):
        for el in copy_lista:
            if el > random_num:
                R_list.append(el)
            else:
                L_list.append(el)
    else:
        return lista

    # revisar - recursividad
    L_list = _sort(L_list)
    R_list = _sort(R_list)

    return print(f'RESULTADO: {L_list + [random_num] + R_list}')


inicio = time.time()
retorno = q_sort(lista)
fin = time.time()
print(fin - inicio)
