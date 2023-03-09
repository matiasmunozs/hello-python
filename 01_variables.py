#la convencion en python es que las variables se escriban en miniscula y snake_case
#Nita: Python no compli, interpreta

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable= False
print(my_bool_variable)

#las variables se puede pasar con ,

#concatenacion de variables en un print
print(my_string_variable,my_int_variable,my_bool_variable)
print("Este es el valor de :", my_bool_variable)

#Algunas funciones de sistema

#len()
print(len(my_int_to_str_variable))
print(len(my_string_variable))

#Variables en una sola linea, no es buena practica.
name, surname = "Matias", "Muñoz"
print("Mi nombre es:", name,surname)

#Sistema de inputs, es como un teclado en pantalla

nombre = input("Cual es tu nombre: ")
edad = input("Cuantos años tienes: ")

print(nombre)
print(edad)
