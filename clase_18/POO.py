class Personaje:
    tipo = 'Personaje'  # Atributo de clase

    def __init__(self, id, nombre, apellido, edad) -> None:
        # Atributos del objeto
        self.id = id
        self._nombre = nombre
        self._apellido = apellido
        self.edad = edad
        self._lista = [id, nombre, apellido, edad]

    @property  # Getter
    # Convierte una función (método) en una propiedad. Por eso, esta función despues se la debe invocar como variable.nombre
    def nombre(self):
        return self._nombre

    @nombre.setter  # Setter
    # Crea una propiedad que puede asignarle un valor a la property (key)
    def set_nombre(self, value):
        self._nombre = value

    # Metodo de instancia. Se lo printea como: print(instancia.descripcion())
    def descripcion(self) -> str:
        return '{0}_{1}'.format(self._nombre, self._apellido)

    # Método especial: Mostrar objeto. Se lo printea como print(intancia)
    def __str__(self) -> str:
        return 'Nombre: {0}; Apellido: {1}'.format(self._nombre, self._apellido)

    # Método especial: Permite utilizar la función len sobre una instancia de esta clase Personaje.
    def __len__(self) -> str:
        return self.edad

    # Método especial: Permite llamar una lista dentro de la clase sin tener que llamar un método
    def __getitem__(self, i):
        return self._lista[i]

    # Método especial: El mismo que el anterior pero permite setera un valor en una posición de una lista dentro de la clase
    def __setitem__(self, i, value):
        self._lista[i] = value

    # Método especial: Consulta si un item se encuentra (in) en una lista de la clase. Devuelve un bool
    def __contains__(self, value):
        return value in self._lista

    # Método especial: Itera sobre una lista
    def __iter__(self):
        for i in range(len(self._lista)):
            yield self._lista[i] # retorna un objeto iterable (debe iterarse con un for por fuera)

# Inheritance
class Poderes(Personaje):
    def __init__(self, id, nombre, apellido, edad, poder):
        Personaje.__init__(self, id, nombre, apellido, edad)  # paso los parametros a la clase padre
        self.poder = poder

    def __str__(self) -> str:
        return 'Nombre: {0}; Poder: {1}'.format(self._nombre, self.poder)


# Asignar atributos a la clase - Instanciar
personaje_A = Personaje(0, 'Marty', 'McFly', 18)
# llamar a un método de la clase:
# personaje_A.set_nombre = 'JORGEE' # setter
# print(personaje_A.descripcion()) # Marty

# ------------- METODOS ESPECIALES ------------- #
# __str__:
# print(personaje_A)  # 'Nombre: Marty; Apellido: McFly'
# método normal:
# print(personaje_A.descripcion())  # 'Marty_McFly'

# __len__:
# print(len(personaje_A))  # '18'

# __getitem__:
# print(personaje_A[2])  # 'McFly'

# __setitem__:
# personaje_A[2] = 'McDown'
# print(personaje_A[2]) #  'McDown'

# __contains__:
# print('Marty' in personaje_A) # True
# print('Marta' in personaje_A) # False

# __iter__:
# for el in personaje_A:
#     print(el)


# ------------- Inheritance ------------- #
personaje_B = Poderes(1, 'Dr.', 'Sofenmacher', 18, 'Volar')
print(personaje_B)

# print(personaje_A._nombre)  # Intentar traer un atributo
# OUTPUT: AttributeError: 'Personaje' object has no attribute '_nombre'
