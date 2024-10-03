#ejemplo para calcular el area del triangulo

#definir variables de entrada
base = int(input("ingrese la base: "))
altura = int(input("ingrese la altura: "))

#proceso
def calcularAreaTriangulo(b, a):
    area = (b*a)/2
    return  area

#invocar la funcion
resultado = calcularAreaTriangulo(base, altura)

print(f"el area del triangulo cuya base es {base} y altura es {altura} es: {resultado} ")

#funcion con argumento predeterminado
def my_function(country = "Colombia"):
    print("I am from " + country)

#invocar la funcion
my_function()
my_function("sweden")


#argumento arbitrario
def mostrarEstudiantes(*args):
    print("el estudiante: " +args[2])

#invocamos la funcion
mostrarEstudiantes("Emil", "Tobias", "Linus")

#argumentos de palabra clave
def mostrarCarros(carro1, carro2, carro3):
    print("el carro es: " + carro3)

#invocar
mostrarCarros(carro1 = "BMW", carro3 = "ferrari", carro2 = "Ford")

#argumento arbitrario **kwargs
def mostrarCliente(**kwargs):
    print("su apellido es: " + kwargs["apellido"])

#invocamos
mostrarCliente(nombre = "Tobias", apellido = "Refsnes")


#declaracion de paso
def mifuncion():
    pass

#funciones integradas
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#funcion pow para elevar 7^4
num1 = pow(7, 4)
print(num1)

