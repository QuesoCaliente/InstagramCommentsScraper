


def ordenar(lista):
    nueva_lista = []
    cantidad_cambios = 0
    while cantidad_cambios != 0 :
        acumulador = 0
        for dato in lista:
            #print(f'iterando en {dato}')
            acumulador = acumulador+1
            longitud_lista = len(lista)

            if acumulador<longitud_lista:
                
                if dato > lista[acumulador]:
                    lista[acumulador], lista[acumulador-1] = dato, lista[acumulador]
                    cantidad_cambios+=1
                else:
                    cantidad_cambios-=1
                print(lista)

    return lista



lista = [1,5,9,10,3,150,20,30,40,7,4,6]


print(ordenar(lista))


# def ordenamiento(lista):
#     indice = len(lista)-1
#     while indice > 0:
#         mayor = indice_max(lista, 0, indice)
#         lista[-1], lista[mayor] = lista[mayor], lista[-1]
#         indice-=1
#     return lista


# def indice_max(lista, inicio, fin):
#     max = inicio
#     for i in range(inicio+1, fin+1):
#         print(f'{lista[i]} - {lista[max]}')
#         if lista[i] > lista[max]:
#             max = i
#     return max

# print(ordenamiento(lista))


def ordenar(lista):
    nueva_lista = []
    inicio=lista[0]

    while len(lista)>0:
        for dato in lista:

            if dato < inicio:
                inicio = dato

        nueva_lista.append(inicio)

        lista.remove(inicio)
        if len(lista) > 0:
            inicio=lista[0]
        print(nueva_lista)


lista = [1,5,9,10,3,20,30,40,7,4,6]
ordenar(lista)