#la convencion en python es que las variables se escriban en miniscula y snake_case
#Nota: Python no compila, interpreta.

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

#Variables en una sola linea, se puedes hacer PERO no es buena practica.
name, surname, alias = "Matias", "Muñoz", "Mati"
print("Mi nombre es:", name,surname, "y mi alias es:", alias)

#Sistema de inputs, es como un teclado en pantalla

name = input("Cual es tu nombre: ")
age = input("Cuantos años tienes: ")

print(name)
print(age)

